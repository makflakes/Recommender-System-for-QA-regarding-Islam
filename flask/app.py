from flask import Flask, request, render_template
from lxml import etree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as skcs
import requests
from bs4 import BeautifulSoup
import requests
from xml.etree import ElementTree as ET
import ast
import pandas as pd

from gpt4all import GPT4All, Embed4All
from openai.embeddings_utils import cosine_similarity

#Converts list to dictionary format to be passed as data to the website renderer
def lists_to_dicts(lists):
    dicts = []
    for lst in lists:
        new_dict = {
            'title': lst[0],
            'url': lst[1],
            'question': lst[2],
            'answer': lst[3]
        }
        dicts.append(new_dict)
    return dicts

#Use for extracting data from the XQuery App API (for token matching) which is wrapped in HTML
def extract_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    divs = soup.find_all('div')
    for div in divs:
        question_tag = div.find('question')
        answer_tag = div.find('answer')
        url_tag = div.find('url')

        if question_tag and answer_tag and url_tag:
            item = {
                'question': question_tag.text.strip(),
                'answer': answer_tag.text.strip(),
                'url': url_tag.text.strip()
            }
            if item not in data:
                data.append(item)
    
    return data

#Used to compute vector siminlarity in GPT4All search
def compute_query_qa_similarity(query, embedder, df):
  embedded_query = embedder.embed(query)
  embedded_qa_pair_embeddings = list(df['gpt4all_embedding'])
  embedded_qa_pair_text = list(df['title'] + '%%' + df['url'] + '%%' + df['question'] +'%%' + df['answer'])
  zipped_qa_pairs = list(zip(embedded_qa_pair_embeddings, embedded_qa_pair_text))
  similarities = [(cosine_similarity(embedded_query, qa_pair_tuple[0]), qa_pair_tuple[1]) for qa_pair_tuple in zipped_qa_pairs] #qa_pair_tuple[0] = embedding
  # re-order list
  similarities_ordered = sorted(similarities, key=lambda tup: tup[0], reverse=True) # tup[0] is the value of cosine similarity
  return similarities_ordered[:5]


'''Preliminary processing to read the XML from database and 
convert it into Required Data Types for easy processing.'''

url = 'http://localhost:8080/exist/rest/db/Islamqa10/islamqa_embeddings.xml'

            # send GET request
response = requests.get(url)
response.raise_for_status()

    # parse the response content as XML
tree = ET.fromstring(response.content)

    # find all 'entry' elements in the XML
entries = tree.findall('.//entry')

    # list to hold all entry data
data = []

    # for each 'entry', get all the necessary details
for entry in entries:
        entry_data = {}
        entry_data['url'] = entry.find('.//url').text if entry.find('.//url') is not None else None
        entry_data['title'] = entry.find('.//title').text if entry.find('.//title') is not None else None
        entry_data['question'] = entry.find('.//question').text if entry.find('.//question') is not None else None
        entry_data['answer'] = entry.find('.//answer').text if entry.find('.//answer') is not None else None
        gpt4all_embedding_element = entry.find('.//gpt4all_embeddings')
        if gpt4all_embedding_element is not None:
            entry_data['gpt4all_embedding'] = ast.literal_eval(gpt4all_embedding_element.text)
        else:
            entry_data['gpt4all_embedding'] = None
        data.append(entry_data)

    # convert the list of dictionaries into a DataFrame
df = pd.DataFrame(data)

# Fetch the XML data from the eXist-db
data = response.text

# Parse the XML data
root = etree.fromstring(data.encode('utf-8'), parser=etree.XMLParser(huge_tree=True))

# Extract the text from the XML elements
entries = root.xpath('//entry')
text_data = [(i, ' '.join(entry.xpath('.//title/text() | .//question/text() | .//answer/text()'))) for i, entry in enumerate(entries)]

# Vectorize the text data (used in sklearn search)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([text[1] for text in text_data])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        searchtype=request.form['searchtype']


'''We have three search types : sklearn, tokenmatching and GPT4All, which require different ways to process data'''

        if searchtype=='sklearn':
        

        # Vectorize the query
            query_vec = vectorizer.transform([query])

        # Calculate cosine similarity
            cosine_similarities = skcs(X, query_vec).flatten()

        # Sort the entries by similarity
            similarities_and_entries = sorted(zip(cosine_similarities, text_data), reverse=True)

        # Retrieve the original XML elements of the top 5 most similar entries
            top_entries = []
            for i in range(5):
                index_of_most_similar_entry = similarities_and_entries[i][1][0]
                xml_of_most_similar_entry = entries[index_of_most_similar_entry]

                url = xml_of_most_similar_entry.xpath('.//url/text()')[0]
                title = xml_of_most_similar_entry.xpath('.//title/text()')[0]
                question = xml_of_most_similar_entry.xpath('.//question/text()')[0]
                answer = xml_of_most_similar_entry.xpath('.//answer/text()')[0]

                top_entries.append({
                    'url': url,
                    'title': title,
                    'question': question,
                    'answer': answer,
                })

        
            return render_template('results.html', entries=top_entries)

        if searchtype=='tokenmatching' :

            print(query.replace(" ", "+"))
            
            website_data = extract_info('http://localhost:8080/exist/rest/db/Islamqa10/onlyquery.xq?queries='+query.replace(" ", "+")) 
            
            return render_template('results.html', entries=website_data)

        if searchtype=='gpt4all':

            #GPT4All Embedder to create embeddings
            embedder = Embed4All()

            results=compute_query_qa_similarity(query, embedder, df)

            results_list=[]

            for articles in results:
                results_list.append(articles[1].split('%%'))

            top5dict = lists_to_dicts(results_list)

            return render_template('results.html', entries=top5dict)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

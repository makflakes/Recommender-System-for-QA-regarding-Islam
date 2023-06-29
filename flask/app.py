from flask import Flask, request, render_template
from lxml import etree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']

        # Fetch the XML data from the eXist-db
        response = requests.get('http://localhost:8080/exist/rest/db/Islamqa10/islamqa_10thousand_500.xml')
        data = response.text

        # Parse the XML data
        root = etree.fromstring(data)

        # Extract the text from the XML elements
        entries = root.xpath('//entry')
        text_data = [(i, ' '.join(entry.xpath('.//question/text() | .//answer/text()'))) for i, entry in enumerate(entries)]

        # Vectorize the text data
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([text[1] for text in text_data])

        # Vectorize the query
        query_vec = vectorizer.transform([query])

        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(X, query_vec).flatten()

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

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

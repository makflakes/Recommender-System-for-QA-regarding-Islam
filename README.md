# **IslamQA : Directing you to the correct Answer**

## **Project Members** :

Mohammed Abdul Khaliq

Ufkun-Bayram Menderes

Murshed Alam Nahid

## Status of Project

- [x] Collect data from website.
   
- [x] Parse data into XML Format.
      
- [x] Upload data into eXist-db database.
      
- [x] Collect statistics using XPath.
      
- [x] Implement XQuery code for Boolean Union Retrieval.
      
- [x] Use GET Requests to gather XML data in python and compute cosine similarity.
      
- [ ] Implement website for Statistics, Boolean and Cosine Similarity.
      
- [ ] OpenAI embeddings for semantic search.
      
- [ ] Set of easy-hard questions to test search capability.

## **Motivation**:
The project aims to develop an advanced search engine in the field of religion that utilizes personal experiences, seeking to provide more personalized, relevant, and intuitive search results, thereby enhancing user interaction and personalization of digital information.



## Setup the database


### 1. eXist-DB database setup

Steps:

1. Download eXist-db by following the instructions at <a href='https://exist-db.org/exist/apps/doc/basic-installation'>eXist-db Installation Guide</a>

2. Start the eXist-db server and 'Open Dashboard'. Select ```eXide - XQuery IDE```.
   
3. Create a "New" file of type XML and upload the dataset present at ```/dataset/islamqa_10thousand_500.xml``` and store it at an appropriate eXist-db path.
   
4. Create a "New" file of type XQuery and upload the file present at ```/xquery/onlyquery.xq``` and store it at the same location as the dataset inside eXist-db.
   
## Querying the results
Make sure the eXist-db server is still running for both these cases.

### Setting up the path in Flask-app:

Steps: 

1. Open the ```flask/app.py``` file in your desired editor.

2. Change Line 67 to point to your database path in exist-db. For instance, we placed our XML file in ```Islamqa10``` folder and renamed it to ```islamqa_embeddings.xml``` :
```
url = 'http://localhost:8080/exist/rest/<insert path here>'
url = 'http://localhost:8080/exist/rest/db/Islamqa10/islamqa_embeddings.xml'
```

3. Similarly, at line 161, you will have to point the path to your ```onlyquery.xq``` file on the exist-db database
```
website_data = extract_info('http://localhost:8080/exist/rest/<insert path here>?queries='+query.replace(" ", "+")) 
website_data = extract_info('http://localhost:8080/exist/rest/db/Islamqa10/onlyquery.xq?queries='+query.replace(" ", "+")) 
```

4. Install the required libraries :
```
pip3 install requirements.txt
```

5. Run the app.py file
```
python3 app.py
```

### 1. Basic Token Search



### 2. Advanced Cosine Similarity Search

Steps:





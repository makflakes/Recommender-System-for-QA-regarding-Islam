# **IslamQA : Directing you to the correct Answer**

### **Project Members** - Mohammed Abdul Khaliq, Ufkun-Bayram Menderes, Murshed Alam Nahid

## Status of Project

- [x] Collect data from website.
   
- [x] Parse data into XML Format.
      
- [x] Upload data into eXist-db database.
      
- [x] Collect statistics using XPath.
      
- [x] Implement XQuery code for Boolean Union Retrieval.
      
- [x] Use GET Requests to gather XML data in python and compute cosine similarity using Sklearn, OpenAI Ada-02 and GPT4All.
      
- [x] Set of easy-hard questions to test search capability (Report).

## **Motivation**:
The project aims to develop an advanced search engine in the field of religion that utilizes personal experiences, seeking to provide more personalized, relevant, and intuitive search results, thereby enhancing user interaction and personalization of digital information.

## Navigating the Repository :

1. ```/data``` contains the main data files in XML and csv format. The csv file is the file created after web scraping while the XML file is the converted csv file with embeddings data and is required to be uploaded to eXist-db.

2. ```/data_scraping_and_conversion``` contains all the code to extract data from website, create vector representation using OpenAI's Ada and GPT4All and to convert the csv to xml.

3. ```/flask``` contains all the necessary files to run the flask app.

4. ```/validation``` contains all the scripts and explanation for the validation process for our XML files.

5. ```/xpath``` contains the scripts for querying our XML Database to gather statistics.

6. ```/xquery``` contains the xquery file that needs to be uploaded onto the eXist-db database. 

## Setup the database


### 1. eXist-DB database setup

Steps:

1. Download eXist-db by following the instructions at <a href='https://exist-db.org/exist/apps/doc/basic-installation'>eXist-db Installation Guide</a>

2. Start the eXist-db server and 'Open Dashboard'. Select ```eXide - XQuery IDE```.
   
3. Create a "New" file of type XML and upload the dataset present at ```/dataset/islamqa_10thousand_500.xml``` and store it at an appropriate eXist-db path.
   
4. Create a "New" file of type XQuery and upload the file present at ```/xquery/onlyquery.xq``` and store it at the same location as the dataset inside eXist-db.
   
##  Setting up the Flask-app:
Make sure the eXist-db server is still running.

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

## Types of Searches :

#### 1. Token matching / Boolean Union Search :

The results displayed will contain the exact words you searched for. If all the words do not exist in the Question, the Answer and the Title section of the data, then such results are not shown.

#### 2. Sklearn Search :

This implementation makes use of sklearn's ```TFIDFVectorizer``` to create vector embeddings for the Title+Question+Answer elements of the XML data. The User query is similarly vectorized and the output results are the top 5 ranked results based on cosine similarity between the Query and the XML data.

#### 3. GPT4All Search :

This implementation makes use of GPT4All's semantic vector representations which create semantic vectors for the Title+Question+Answer elements of the XML data. The User query is similarly made into semantic vector representation using the ```Embedder``` and the output results are the top 5 ranked results based on cosine similarity between the Query and the XML data.

## Extensions over the course content :

1. Making use of a different Database (eXist-db) which was not covered in the lectures and was also not implemented by other teams.

2. Using XQuery for our token matching search feature.

3. Making use of GPT4All/OpenAI's Ada-02 to create and store vector entries in XML format to later query from them.


## Features that didn't make it to the final website :

1. Statistics computed using XPath for theologian and book references were collected by us. However, we still need to work on how and where to best display such stats on the wesbite.

2. OpenAI's semantic search using their 'Ada-02' model has been implemented and is present in the XML data. However, to query such embeddings would require making use of OpenAI API Keys which would require extra security measures to ensure that they dont get leaked when the website is hosted. Additionally, such an implementation on the hosted website would cost us money. Thus, we opt for a similarly sophisticated OpenSource Semantic Search using GPT4All.





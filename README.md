# **IslamQA : Directing you to the correct Answer**
The aim of this project is to collect expert answers for various queries regarding Islam from islamqa.info and to create easier and more accurate methods for users to search through these answers easily.

## Setup the database


### 1. eXist-DB database setup

Steps:
1. Download eXist-db by following the instructions at <a href='https://exist-db.org/exist/apps/doc/basic-installation'>eXist-db Installation Guide</a>
2. Start the eXist-db server and 'Open Dashboard'. Select ```eXide - XQuery IDE```.
3. Create a "New" file of type XML and upload the dataset present at ```/dataset/islamqa_10thousand_500.xml``` and store it at an appropriate eXist-db path.
4. Create a "New" file of type XQuery and upload the file present at ```/xquery/html_query_simple.xq``` and store it at the same location as the dataset inside eXist-db.
   
## Querying the results
Make sure the eXist-db server is still running for both these cases.

### 1. Basic Boolean Search
Steps:
1. Inside the ```eXide - XQuery IDE``` open the ```html_query_simple.xq``` file and change the line 9 ```$doc``` variable to pint to the location of the dataset within eXist-db.
2. Click ```Save``` and then ```Eval``` and ```Run```.
3. Type in any query terms in the search bar and retrieve the results pertaining to the search (the search is case sensitive for now).

### 2. Advanced Cosine Similar Searchity
1. Install the required libraries :
```
pip3 install requirements.txt
```
2. Head into the app.py file and at line 15, change the path to point to the path of your eXist-db dataset.
```
response = requests.get('http://localhost:8080/exist/rest/<path to your database within eXist-db>')
```
3. Run the app.py file
```
python3 app.py
```
4. Enter your query in the search bar and view the results generated by the cosine similarity function.

## Project Members
Mohammed Abdul Khaliq

Murshed Nahid Alam

Ufkun-Bayram Menderes

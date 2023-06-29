# **IslamQA : Driecting you to the correct Answer**

## Setup the database


### 1. eXist-DB database setup

Steps:
1. Download eXist-db by following the instructions at <a href='https://exist-db.org/exist/apps/doc/basic-installation'>eXist-db Installation Guide</a>
2. Start the eXist-db server and 'Open Dashboard'. Select ```eXide - XQuery IDE```.
3. Create a "New" file of type XML and upload the dataset present at ```/dataset/islamqa_10thousand_500.xml``` and store it at an appropriate eXist-db path.
4. Create a "New" file of type XQuery and upload the file present at ```/xquery/html_query_simple.xq``` and store it at the same location as the dataset inside eXist-db.
   
## Querying the results
Make sure the eXist-db server is still running.

### 1. Basic Boolean Search
Steps:
1. Inside the ```eXide - XQuery IDE``` open the ```html_query_simple.xq``` file and change the line 7 ```$doc``` variable to pint to the location of the dataset within eXist-db.
2. Click ```Save``` and then ```Eval``` and ```Run```.
3. Type in any query terms in the search bar and retrieve the results pertaining to the search (the search is case sensitive for now).

### 2. Advanced Cosine Similar Searchity

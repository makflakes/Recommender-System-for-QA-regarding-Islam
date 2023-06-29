xquery version "3.1";
declare namespace output = "http://www.w3.org/2010/xslt-xquery-serialization";
declare option output:method "html5";
declare option output:media-type "text/html";
import module namespace request = "http://exist-db.org/xquery/request";

let $addressee := request:get-parameter("addressee", " ")
let $queryWords := tokenize(lower-case($addressee), '\W+')
let $doc := doc('/db/Islamqa10/islamqa_10thousand_500.xml')/data

return
(: https://getbootstrap.com/docs/3.3/getting-started/ :)
    <html>
        <head>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>

<!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
            
        </head>
        <body>
            <div class="container">
                <h1>IslamQA : Directing you to the correct Answer</h1>
                <p>Query: { $addressee }</p>
                <form method="get">
                    <input type="text" name="addressee" class="form-control"/>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </div>
            
            
        
        {
            for $entry in $doc/entry
            where every $word in $queryWords satisfies contains(lower-case($entry/question), $word) or contains(lower-case($entry/answer), $word)
            return
            <div class="container">
                <div class="card">
                
                <h4>URL: <a href="url">{$entry/url}</a></h4>
                <h3>Question:</h3> <p> {$entry/question}</p>
                <h5>Answer : </h5><p> {$entry/answer}</p>
                
                </div>
                
            </div>
        }
    </body>
    </html>

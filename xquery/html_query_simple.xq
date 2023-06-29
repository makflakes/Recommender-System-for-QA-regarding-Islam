xquery version "3.1";
declare namespace output = "http://www.w3.org/2010/xslt-xquery-serialization";
declare option output:method "html5";
declare option output:media-type "text/html";
import module namespace request = "http://exist-db.org/xquery/request";
let $addressee := request:get-parameter("addressee", "hajj")

let $doc := doc('/db/Islamqa10/islamqa_10thousand_500.xml')/data

return
(: https://getbootstrap.com/docs/3.3/getting-started/ :)
    <html>
        <head>
            <meta charset="utf-8"/>
            <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
            <title>Title</title>
<!-- Latest compiled and minified CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>
<!-- Optional theme -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous"/>
<!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"/>
        </head>
        
        <body>
            <div class="container">
                <h1>IslamQA : Directing you to the correct answer</h1>
                <p>Enter a topic: { $addressee }</p>
                <form method="get">
                    <input type="text" name="addressee" class="form-control"/>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
            </div>
        {
            for $entry in $doc/entry
            where contains($entry/question, $addressee) or contains($entry/answer, $addressee) or contains($entry/title, $addressee)
            return 
            <div class="container">
                <div class="row">
                <div class="column">
                <h4>URL: <a href="url">{$entry/url}</a></h4>
                <h3>Question: {$entry/question}</h3>
                <p>Answer: {$entry/answer}</p>
                <p></p>
                </div>
                </div>
                
            </div>
        }
    </body>
    </html>

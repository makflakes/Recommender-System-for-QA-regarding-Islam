xquery version "3.1";

(: code to extract XML elements that match the tokens in the query using XQuery :)
declare namespace output = "http://www.w3.org/2010/xslt-xquery-serialization";
declare option output:method "html5";
declare option output:media-type "text/html";
import module namespace request = "http://exist-db.org/xquery/request";

let $queries := request:get-parameter("queries", " ") (: reveives the input query from the URL or input field :)
let $queryWords := tokenize(lower-case($queries), '\W+')  (: tokenizes the input query  :)
let $doc := doc('/db/Islamqa10/islamqa_embeddings.xml')/data  (: Enter your dataset path here :)

return
(: https://getbootstrap.com/docs/3.3/getting-started/ :)
    <html>
        
        <body>

        
        {
            (: Loops over the entire dataset matching every word in $queryWords with the <question> as well as the <answer> fields of XML Database :)
            for $entry in $doc/entry
            where every $word in $queryWords satisfies contains(lower-case($entry/question), $word) or contains(lower-case($entry/answer) , $word)
            return
            <div >
                <div>
                    
                %%{$entry/url}%% {$entry/question}%% {$entry/answer}
                
                </div>
                
            </div>
        }
    </body>
    </html>

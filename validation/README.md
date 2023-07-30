
### XML Schema:
The XML Schema defines the structure and constraints for an XML
document. The schema specifies the following:
```
<?xml version="1.0" encoding="UTF-8"?>
```
Like the internal DTD, this
line specifies the XML version (1.0) and the character encoding
(UTF-8) used in the document.
```
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
```
This line declares the XML Schema namespace (xmlns) with the prefix "xs"
and associates it with the XML Schema Definition (XSD) namespace
("http://www.w3.org/2001/XMLSchema").

The root element of the XML document should be named "data." The
"data" element has a complex type, meaning it can contain multiple
occurrences of the "entry" element. The child elements of the "data"
element must appear in a specific sequence.

The "entry" element also has a complex type, meaning it can contain
child elements. Each "entry" element should have child elements in
the following sequence: "url," "title," "question," and "answer."

The "url" element should contain a valid URI.
The "title," "question," and "answer" elements should contain string
values.

Two additional lines were added in the xml file so that the XML
document associates an XML Schema file ("schema.xsd") with the
document and provides information for the XML parser to locate and
validate the XML against the specified schema rules.

**Validation command for XML Schema:
```
xmllint --schema islamqa_final_1500.xsd schema_islamqa_final_1500.xml
```

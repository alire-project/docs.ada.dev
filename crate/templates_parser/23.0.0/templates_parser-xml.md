---
crate: templates_parser
layout: gnatdoc
gnatdoc: {
name: "Templates_Parser.XML",
qualified_name: "Templates_Parser.XML",
signature: "templates_parser.xml",
enclosing: "templates_parser",
is_private: false,
documentation: "This API provides a way to save a Translate_Set as an XML document.\nThere is special rules to know about composite tags.\n\nComposite tags :\n\n   If a tag named TAG exists, then the name TAG_DESCRIPTION is used as a\n   description for this specific tag.\n\nComposite tags (more than one nested level)\n\n   If a tag named TAG exists, then the names TAG_DIM[n]_LABELS is used as\n   a set of labels for the tag's nth axis. In this case TAG_DIM[n]_LABELS\n   must be a vector tag, each entry corresponds to a label on this\n   axis. Also TAG_DIM[n]_DESCRIPTION is used as a description for this\n   axis.\n\nHere is the DTD :\n\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!--Description of a tag or dimension (ex: year)-->\n<!ELEMENT Description (#PCDATA)>\n<!--a dimension-->\n<!ELEMENT Dim (Description, Labels)>\n<!ATTLIST Dim\n    n CDATA #REQUIRED\n>\n<!--entry of a CompositeTag-->\n<!ELEMENT Entry (ind+, V)>\n<!--label of an indice of a dimension (ex: 2000)-->\n<!ELEMENT Label (#PCDATA)>\n<!ATTLIST Label\n    ind CDATA #REQUIRED\n>\n<!--list of labels of one dimension (ex: 1999, 2000, 2001)-->\n<!ELEMENT Labels (Label+)>\n<!--alias and information-->\n<!ELEMENT Tag (Name, Description)>\n<!--tagged data to be published in templates-->\n<!ELEMENT Tagged (SimpleTag*, CompositeTag*)>\n<!--simple variable value-->\n<!ELEMENT V (#PCDATA)>\n<!ELEMENT ind (#PCDATA)>\n<!ATTLIST ind\n    n CDATA #REQUIRED\n>\n<!--identification name for this tag-->\n<!ELEMENT Name (#PCDATA)>\n<!--Tag with no dimension (simple variable)-->\n<!ELEMENT SimpleTag (Tag, V)>\n<!--Tag with one or more dimensions-->\n<!ELEMENT CompositeTag (Tag, Dim+, Entry)>",
documentation_snippet: "",
}
---

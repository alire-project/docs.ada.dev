---
crate: lace_xml
layout: gnatdoc
gnatdoc: {
name: "XML",
qualified_name: "XML",
signature: "xml",
enclosing: "",
is_private: false,
documentation: "- Attribute type",
documentation_snippet: "",
array_types:    [
       {
       name: "Attributes_t",
       qualified_name: "XML.Attributes_t",
       signature: "xml.attributes_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes_t    is array (Positive range <>) of aliased Attribute_t;",
       }   ,
       {
       name: "Elements",
       qualified_name: "XML.Elements",
       signature: "xml.elements",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Elements is array (Positive range <>) of access Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Attribute_t",
       qualified_name: "XML.Attribute_t",
       signature: "xml.attribute_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attribute_t     is tagged private;",
       }   ,
       {
       name: "Element",
       qualified_name: "XML.Element",
       signature: "xml.element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element  is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Attributes_view",
       qualified_name: "XML.Attributes_view",
       signature: "xml.attributes_view",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes_view is access all Attributes_t;",
       }   ,
   ]
,}
---

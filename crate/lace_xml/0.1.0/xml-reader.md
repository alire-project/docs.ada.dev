---
crate: lace_xml
layout: gnatdoc
gnatdoc: {
name: "XML.Reader",
qualified_name: "XML.Reader",
signature: "xml.reader",
enclosing: "xml",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parser",
       qualified_name: "XML.Reader.Parser",
       signature: "xml.reader.parser",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parser is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Character_Data_Handler",
       qualified_name: "XML.Reader.Character_Data_Handler",
       signature: "xml.reader.character_data_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Character_Data_Handler is access procedure (Data:  in unbounded_String);",
       }   ,
       {
       name: "End_Element_Handler",
       qualified_name: "XML.Reader.End_Element_Handler",
       signature: "xml.reader.end_element_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type End_Element_Handler   is access procedure (Name : in     unbounded_String);",
       }   ,
       {
       name: "Start_Element_Handler",
       qualified_name: "XML.Reader.Start_Element_Handler",
       signature: "xml.reader.start_element_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Start_Element_Handler is access procedure (Name : in     unbounded_String;\n                                                Atts : in XML.Attributes_view);",
       }   ,
   ]
,}
---

---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Xml",
qualified_name: "Agpl.Xml",
signature: "agpl.xml",
enclosing: "agpl",
is_private: false,
documentation: "Xml related functions",
documentation_snippet: "",
array_types:    [
       {
       name: "Node_Array",
       qualified_name: "Agpl.Xml.Node_Array",
       signature: "agpl.xml.node_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Array is array (Integer range <>) of Node;",
       }   ,
   ]
,access_types:    [
       {
       name: "Document_access",
       qualified_name: "Agpl.Xml.Document_access",
       signature: "agpl.xml.document_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Document_access is access all Document;",
       }   ,
       {
       name: "Node_access",
       qualified_name: "Agpl.Xml.Node_access",
       signature: "agpl.xml.node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_access is access all Node;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Document",
       qualified_name: "Agpl.Xml.Document",
       signature: "agpl.xml.document",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Document is Node;",
       }   ,
       {
       name: "Node",
       qualified_name: "Agpl.Xml.Node",
       signature: "agpl.xml.node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Node is Dom.Core.Node;",
       }   ,
       {
       name: "Node_Vector",
       qualified_name: "Agpl.Xml.Node_Vector",
       signature: "agpl.xml.node_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Node_Vector is Node_Vectors.Vector;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_node",
       qualified_name: "Agpl.Xml.Null_node",
       signature: "agpl.xml.null_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_node : constant Node := null;",
       }   ,
   ]
,}
---

---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Document",
qualified_name: "Gnoga.Gui.Document",
signature: "gnoga.gui.document",
enclosing: "gnoga.gui",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Document_Type\n-----------------------------------------------------------------------\n  Document_Type is the class encapsulating the DOM's root document node\n  To use, access via Window_Type.Document",
documentation_snippet: "",
simple_types:    [
       {
       name: "Ready_State_Type",
       qualified_name: "Gnoga.Gui.Document.Ready_State_Type",
       signature: "gnoga.gui.document.ready_state_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ready_State_Type is (Uninitialized, Loading, Interactive, Complete);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Document_Type",
       qualified_name: "Gnoga.Gui.Document.Document_Type",
       signature: "gnoga.gui.document.document_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Document_Type is new Gnoga.Gui.Base.Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Document_Access",
       qualified_name: "Gnoga.Gui.Document.Document_Access",
       signature: "gnoga.gui.document.document_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Document_Access is access all Document_Type;",
       }   ,
       {
       name: "Pointer_To_Document_Class",
       qualified_name: "Gnoga.Gui.Document.Pointer_To_Document_Class",
       signature: "gnoga.gui.document.pointer_to_document_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Document_Class is access all Document_Type'Class;",
       }   ,
   ]
,}
---

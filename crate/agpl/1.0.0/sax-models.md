---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Sax.Models",
qualified_name: "Sax.Models",
signature: "sax.models",
enclosing: "sax",
is_private: false,
documentation: "This package implements the content models as described in the DTDs.\nThey are not strictly part of the SAX 2.0 standard, however they are\nused to simply the handling in users' applications.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Content_Spec",
       qualified_name: "Sax.Models.Content_Spec",
       signature: "sax.models.content_spec",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Character_Data\n  Characters, but no child node  (#PCDATA)\n@enum Element_Ref\n  A specific child\n@enum Any_Of\n  child is one of many choices\n@enum Sequence\n  a sequence of elements (order is imposed)\n@enum Repeat\n  A repeated element\n@enum Empty\n  Element must be empty  (EMPTY)\n@enum Anything\n  Content is not described, and can be anything (ANY)",
       documentation_snippet: "type Content_Spec is\n  (Character_Data,\n   Element_Ref,\n   Any_Of,\n   Sequence,\n   Repeat,\n   Empty,\n   Anything\n  );",
       }   ,
       {
       name: "Model_State",
       qualified_name: "Sax.Models.Model_State",
       signature: "sax.models.model_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model_State is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Element_Model_Array",
       qualified_name: "Sax.Models.Element_Model_Array",
       signature: "sax.models.element_model_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Model_Array is array (Natural range <>) of Element_Model_Ptr;",
       }   ,
   ]
,record_types:    [
       {
       name: "Element_Model",
       qualified_name: "Sax.Models.Element_Model",
       signature: "sax.models.element_model",
       enclosing: "",
       is_private: false,
       documentation: "Type used to describe the model used for an element, as described in\nthe DTD (see 3.2.* in XML specifications). For instance, the following\nmodel \"(#PCDATA|emph)*\" is translated to:\n   (Content => Repeat,\n    Min     => 0,\n    Max     => Positive'Last,\n    Elem    => (Content => Any_Of,\n                Choices => (0 => (Content => Character_Data),\n                            1 => (Content => Element,\n                                  Name    => \"emp\"))))\n\n@field Content\n@field Name\n  Name of the element\n@field List\n  all the possible choices\n@field Min\n@field Max\n@field Elem",
       documentation_snippet: "type Element_Model (Content : Content_Spec) is record\n   case Content is\n      when Character_Data | Empty | Anything => null;\n      when Element_Ref =>\n         Name : Unicode.CES.Byte_Sequence_Access;\n      when Any_Of | Sequence =>\n         List : Element_Model_Array_Ptr;\n      when Repeat =>\n         Min : Natural;\n         Max : Positive;\n         Elem : Element_Model_Ptr;\n   end case;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Element_Model_Array_Ptr",
       qualified_name: "Sax.Models.Element_Model_Array_Ptr",
       signature: "sax.models.element_model_array_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Model_Array_Ptr is access Element_Model_Array;",
       }   ,
       {
       name: "Element_Model_Ptr",
       qualified_name: "Sax.Models.Element_Model_Ptr",
       signature: "sax.models.element_model_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Model_Ptr is access Element_Model;",
       }   ,
   ]
,}
---

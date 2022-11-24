---
crate: wayland_ada_scanner
layout: gnatdoc
gnatdoc: {
name: "Aida.Deepend.XML_DOM_Parser",
qualified_name: "Aida.Deepend.XML_DOM_Parser",
signature: "aida.deepend.xml_dom_parser",
enclosing: "aida.deepend",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2018 - 2019 Joakim Strandberg <joakim@mequinox.se>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Attribute",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Attribute",
       signature: "aida.deepend.xml_dom_parser.attribute",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attribute is limited private;",
       }   ,
       {
       name: "Attribute_Index",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Attribute_Index",
       signature: "aida.deepend.xml_dom_parser.attribute_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attribute_Index is new Positive;",
       }   ,
       {
       name: "Node_Kind_Id",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Node_Kind_Id",
       signature: "aida.deepend.xml_dom_parser.node_kind_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Kind_Id is\n  (\n   Node_Kind_Tag,\n   Node_Kind_Comment,\n   Node_Kind_CDATA,\n   Node_Kind_Text\n  );",
       }   ,
       {
       name: "XML_Tag",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.XML_Tag",
       signature: "aida.deepend.xml_dom_parser.xml_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type XML_Tag is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Attributes_Ref",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Attributes_Ref",
       signature: "aida.deepend.xml_dom_parser.attributes_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes_Ref\n  (\n   Element : not null access constant Attribute_Vectors.Vector\n  )\nis limited null record with Implicit_Dereference => Element;",
       }   ,
       {
       name: "Child_Nodes_Ref",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Child_Nodes_Ref",
       signature: "aida.deepend.xml_dom_parser.child_nodes_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Child_Nodes_Ref\n  (\n   Element : not null access constant Node_Vectors.Vector\n  )\nis limited null record with Implicit_Dereference => Element;",
       }   ,
       {
       name: "Node",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Node",
       signature: "aida.deepend.xml_dom_parser.node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node (Id : Node_Kind_Id := Node_Kind_Tag) is record\n   case Id is\n      when Node_Kind_Tag  =>\n         Tag : aliased XML_Tag;\n      when Node_Kind_Comment |\n           Node_Kind_CDATA |\n           Node_Kind_Text =>\n         Text : not null String_Ptr := Empty_String'Access;\n   end case;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Attribute_Ptr",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Attribute_Ptr",
       signature: "aida.deepend.xml_dom_parser.attribute_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attribute_Ptr is access all Attribute;",
       }   ,
       {
       name: "Node_Ptr",
       qualified_name: "Aida.Deepend.XML_DOM_Parser.Node_Ptr",
       signature: "aida.deepend.xml_dom_parser.node_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Ptr is access all Node;",
       }   ,
   ]
,}
---

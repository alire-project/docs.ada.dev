---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Indefinite_Multiordered_Maps",
qualified_name: "Agpl.Containers.Indefinite_Multiordered_Maps",
signature: "agpl.containers.indefinite_multiordered_maps",
enclosing: "agpl.containers",
is_private: false,
documentation: "A table with two indexing/ordering key types\n\n@formal Key_Type\n@formal Indices\n@formal Element_Type\n@formal \"<\"\n@formal \"=\"",
documentation_snippet: "",
array_types:    [
       {
       name: "Key_Array",
       qualified_name: "Agpl.Containers.Indefinite_Multiordered_Maps.Key_Array",
       signature: "agpl.containers.indefinite_multiordered_maps.key_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_Array is array (Indices) of Key_Type;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cursor",
       qualified_name: "Agpl.Containers.Indefinite_Multiordered_Maps.Cursor",
       signature: "agpl.containers.indefinite_multiordered_maps.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor (Index : Indices) is tagged private;",
       }   ,
       {
       name: "Map",
       qualified_name: "Agpl.Containers.Indefinite_Multiordered_Maps.Map",
       signature: "agpl.containers.indefinite_multiordered_maps.map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Map is tagged private;",
       }   ,
   ]
,}
---

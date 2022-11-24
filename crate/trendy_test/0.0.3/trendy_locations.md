---
crate: trendy_test
layout: gnatdoc
gnatdoc: {
name: "Trendy_Locations",
qualified_name: "Trendy_Locations",
signature: "trendy_locations",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Source_Location",
       qualified_name: "Trendy_Locations.Source_Location",
       signature: "trendy_locations.source_location",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Location is record\n    File : Char_Ptr;\n    Line : Natural;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Char_Ptr",
       qualified_name: "Trendy_Locations.Char_Ptr",
       signature: "trendy_locations.char_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Char_Ptr is Interfaces.C.Strings.chars_ptr;",
       }   ,
   ]
,}
---

---
crate: pygamer_simulator
layout: gnatdoc
gnatdoc: {
name: "simulator_assets",
qualified_name: "simulator_assets",
signature: "simulator_assets",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Format_Type",
       qualified_name: "simulator_assets.Format_Type",
       signature: "simulator_assets.format_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Format_Type is (FILE_RAW, FILE_GZIP);",
       }   ,
   ]
,record_types:    [
       {
       name: "Content_Type",
       qualified_name: "simulator_assets.Content_Type",
       signature: "simulator_assets.content_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Content_Type is record\n   Name    : Name_Access;\n   Content : Content_Access;\n   Modtime : Interfaces.C.long := 0;\n   Format  : Format_Type := FILE_RAW;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Content_Access",
       qualified_name: "simulator_assets.Content_Access",
       signature: "simulator_assets.content_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Content_Access is access constant Ada.Streams.Stream_Element_Array;",
       }   ,
       {
       name: "Name_Access",
       qualified_name: "simulator_assets.Name_Access",
       signature: "simulator_assets.name_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Name_Access is access constant String;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Content",
       qualified_name: "simulator_assets.Null_Content",
       signature: "simulator_assets.null_content",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Content : constant Content_Type;",
       }   ,
   ]
,}
---

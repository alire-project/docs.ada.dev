---
crate: adacl
layout: gnatdoc
gnatdoc: {
name: "AdaCL.OS.Low_Level",
qualified_name: "AdaCL.OS.Low_Level",
signature: "adacl.os.low_level",
enclosing: "adacl.os",
is_private: false,
documentation: "\nOperating System Tools. Start extrnal Programm.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Known_OS",
       qualified_name: "AdaCL.OS.Low_Level.Known_OS",
       signature: "adacl.os.low_level.known_os",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Known_OS is (Windows, MacOS, Linux);",
       }   ,
   ]
,record_types:    [
       {
       name: "Pipe_Type",
       qualified_name: "AdaCL.OS.Low_Level.Pipe_Type",
       signature: "adacl.os.low_level.pipe_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pipe_Type is record\n   Input  : GNAT.OS_Lib.File_Descriptor;\n   Output : GNAT.OS_Lib.File_Descriptor;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "This_OS",
       qualified_name: "AdaCL.OS.Low_Level.This_OS",
       signature: "adacl.os.low_level.this_os",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "This_OS : constant Known_OS;",
       }   ,
   ]
,}
---

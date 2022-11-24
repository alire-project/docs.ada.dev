---
crate: ada_fuse
layout: gnatdoc
gnatdoc: {
name: "Fuse.General",
qualified_name: "Fuse.General",
signature: "fuse.general",
enclosing: "fuse",
is_private: false,
documentation: "Log, Errors\n\n@formal Log_Level\n@formal Log_File_Name",
documentation_snippet: "",
simple_types:    [
       {
       name: "Dir_Buffer_Type",
       qualified_name: "Fuse.General.Dir_Buffer_Type",
       signature: "fuse.general.dir_buffer_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Dir_Buffer_Type is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Fill_Dir_Access",
       qualified_name: "Fuse.General.Fill_Dir_Access",
       signature: "fuse.general.fill_dir_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fill_Dir_Access is access procedure\n  (Buffer   : Dir_Buffer_Type;\n   Name     : String;\n   St_Buf   : System.Stat_Access;\n   Offset   : Natural);",
       }   ,
   ]
,}
---

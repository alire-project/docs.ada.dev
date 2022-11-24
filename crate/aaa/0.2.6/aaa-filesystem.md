---
crate: aaa
layout: gnatdoc
gnatdoc: {
name: "AAA.Filesystem",
qualified_name: "AAA.Filesystem",
signature: "aaa.filesystem",
enclosing: "aaa",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Replacer",
       qualified_name: "AAA.Filesystem.Replacer",
       signature: "aaa.filesystem.replacer",
       enclosing: "",
       is_private: false,
       documentation: "A scoped type to ensure that a file is updated and replaced without\ntrouble. In case of failure, the original file remains untouched. So\nwhat happens is: 1) A copy to a temp file is made. 2) This file is\nmodified and can be tested as the client sees fit. 3) If the new file is\nproper, the old one is renamed to .prev and the new one takes its place.",
       documentation_snippet: "type Replacer (<>) is tagged limited private;",
       }   ,
       {
       name: "Temp_File",
       qualified_name: "AAA.Filesystem.Temp_File",
       signature: "aaa.filesystem.temp_file",
       enclosing: "",
       is_private: false,
       documentation: "A RAII scoped type to manage a temporary file name.\nCreates an instance with a unique file name. This does nothing on disk.\nThe user is responsible for using the temp file name as they see fit.\nThe file is deleted once an object of this type goes out of scope.\nIf the file/folder was never created on disk nothing will happen.",
       documentation_snippet: "type Temp_File (<>) is tagged limited private;",
       }   ,
   ]
,}
---

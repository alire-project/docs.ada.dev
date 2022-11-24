---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Unix_Text_IO",
qualified_name: "SAL.Unix_Text_IO",
signature: "sal.unix_text_io",
enclosing: "sal",
is_private: false,
documentation: "Abstract :\n\nReplacement for subset of Ada.Text_IO, using Unix line endings\non all platforms.\n\nFor very large files, this is significantly faster than Text_IO\noutput followed by dos2unix.\n\nCopyright (C) 2020 Free Software Foundation All Rights Reserved.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.",
documentation_snippet: "",
simple_types:    [
       {
       name: "File_Mode",
       qualified_name: "SAL.Unix_Text_IO.File_Mode",
       signature: "sal.unix_text_io.file_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Mode is (In_File, Out_File, Append_File);",
       }   ,
       {
       name: "File_Type",
       qualified_name: "SAL.Unix_Text_IO.File_Type",
       signature: "sal.unix_text_io.file_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Type is limited private;",
       }   ,
   ]
,}
---

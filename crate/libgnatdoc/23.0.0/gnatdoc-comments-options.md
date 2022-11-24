---
crate: libgnatdoc
layout: gnatdoc
gnatdoc: {
name: "GNATdoc.Comments.Options",
qualified_name: "GNATdoc.Comments.Options",
signature: "gnatdoc.comments.options",
enclosing: "gnatdoc.comments",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                    GNAT Documentation Generation Tool                    --\n                                                                          --\n                       Copyright (C) 2022, AdaCore                        --\n                                                                          --\n This is free software;  you can redistribute it  and/or modify it  under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  This software is distributed in the hope  that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public --\n License for  more details.  You should have  received  a copy of the GNU --\n General  Public  License  distributed  with  this  software;   see  file --\n COPYING3.  If not, go to http://www.gnu.org/licenses for a complete copy --\n of the license.                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Documentation_Style",
       qualified_name: "GNATdoc.Comments.Options.Documentation_Style",
       signature: "gnatdoc.comments.options.documentation_style",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum GNAT\n  Advanced GNAT style of the documentation comments\n@enum Leading\n  Simple leading style of the documentation comments",
       documentation_snippet: "type Documentation_Style is\n  (GNAT,\n   Leading);",
       }   ,
   ]
,record_types:    [
       {
       name: "Extractor_Options",
       qualified_name: "GNATdoc.Comments.Options.Extractor_Options",
       signature: "gnatdoc.comments.options.extractor_options",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Style\n  Style of the documentation comments.\n@field Fallback",
       documentation_snippet: "type Extractor_Options is record\n   Style    : Documentation_Style := GNAT;\n   Fallback : Boolean             := False;\nend record;",
       }   ,
   ]
,}
---

---
crate: libgnatdoc
layout: gnatdoc
gnatdoc: {
name: "GNATdoc.Comments",
qualified_name: "GNATdoc.Comments",
signature: "gnatdoc.comments",
enclosing: "gnatdoc",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                    GNAT Documentation Generation Tool                    --\n                                                                          --\n                       Copyright (C) 2022, AdaCore                        --\n                                                                          --\n This is free software;  you can redistribute it  and/or modify it  under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  This software is distributed in the hope  that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public --\n License for  more details.  You should have  received  a copy of the GNU --\n General  Public  License  distributed  with  this  software;   see  file --\n COPYING3.  If not, go to http://www.gnu.org/licenses for a complete copy --\n of the license.                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Section_Kind",
       qualified_name: "GNATdoc.Comments.Section_Kind",
       signature: "gnatdoc.comments.section_kind",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Raw\n  Raw text of the documentation, extracted from\n                        comments\n@enum Snippet\n  Code snippet\n@enum Breif\n  Breif description of the entity\n                        ??? not supported\n@enum Description\n  Full description of the entity\n@enum Formal\n  Formal parameter of the generic entity\n@enum Enumeration_Literal\n  Literal of the enumeration type\n@enum Field\n  Record component of discriminant\n@enum Parameter\n  Description of the parameter\n@enum Returns\n  Description of the return value\n@enum Raised_Exception\n  Description of the raised exception",
       documentation_snippet: "type Section_Kind is\n  (Raw,\n   Snippet,\n   Breif,\n   Description,\n   Formal,\n   Enumeration_Literal,\n   Field,\n   Parameter,\n   Returns,\n   Raised_Exception);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Section",
       qualified_name: "GNATdoc.Comments.Section",
       signature: "gnatdoc.comments.section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Section is tagged limited private;",
       }   ,
       {
       name: "Structured_Comment",
       qualified_name: "GNATdoc.Comments.Structured_Comment",
       signature: "gnatdoc.comments.structured_comment",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Structured_Comment is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Section_Access",
       qualified_name: "GNATdoc.Comments.Section_Access",
       signature: "gnatdoc.comments.section_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Section_Access is access all Section'Class;",
       }   ,
       {
       name: "Structured_Comment_Access",
       qualified_name: "GNATdoc.Comments.Structured_Comment_Access",
       signature: "gnatdoc.comments.structured_comment_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Structured_Comment_Access is access all Structured_Comment'Class;",
       }   ,
   ]
,}
---

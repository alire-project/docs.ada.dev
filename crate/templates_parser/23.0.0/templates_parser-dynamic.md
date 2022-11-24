---
crate: templates_parser
layout: gnatdoc
gnatdoc: {
name: "Dynamic",
qualified_name: "Templates_Parser.Dynamic",
signature: "templates_parser.dynamic",
enclosing: "templates_parser",
is_private: false,
documentation: "------------\n Lazy_Tag --\n------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Path",
       qualified_name: "Templates_Parser.Dynamic.Path",
       signature: "templates_parser.dynamic.path",
       enclosing: "",
       is_private: false,
       documentation: "A Path gives the full position of a given element in the cursor tag",
       documentation_snippet: "type Path is array (Positive range <>) of Natural;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cursor_Tag",
       qualified_name: "Templates_Parser.Dynamic.Cursor_Tag",
       signature: "templates_parser.dynamic.cursor_tag",
       enclosing: "",
       is_private: false,
       documentation: "In some cases it is difficult and not efficient to have to map all\nAda data into a template Tag. A Cursor_Tag object gives the ability\nto iterate through a data structure which is living on the Ada side\nonly.",
       documentation_snippet: "type Cursor_Tag is abstract tagged private;",
       }   ,
       {
       name: "Lazy_Tag",
       qualified_name: "Templates_Parser.Dynamic.Lazy_Tag",
       signature: "templates_parser.dynamic.lazy_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lazy_Tag is abstract tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Cursor_Tag_Access",
       qualified_name: "Templates_Parser.Dynamic.Cursor_Tag_Access",
       signature: "templates_parser.dynamic.cursor_tag_access",
       enclosing: "",
       is_private: false,
       documentation: "In some cases it is difficult and not efficient to have to map all\nAda data into a template Tag. A Cursor_Tag object gives the ability\nto iterate through a data structure which is living on the Ada side\nonly.",
       documentation_snippet: "type Cursor_Tag_Access is access all Cursor_Tag'Class;",
       }   ,
       {
       name: "Lazy_Tag_Access",
       qualified_name: "Templates_Parser.Dynamic.Lazy_Tag_Access",
       signature: "templates_parser.dynamic.lazy_tag_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lazy_Tag_Access is access all Lazy_Tag'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Cursor_Tag",
       qualified_name: "Templates_Parser.Dynamic.Null_Cursor_Tag",
       signature: "templates_parser.dynamic.null_cursor_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Cursor_Tag : constant Cursor_Tag_Access;",
       }   ,
       {
       name: "Null_Lazy_Tag",
       qualified_name: "Templates_Parser.Dynamic.Null_Lazy_Tag",
       signature: "templates_parser.dynamic.null_lazy_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Lazy_Tag : constant Lazy_Tag_Access;",
       }   ,
   ]
,}
---

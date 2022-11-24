---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Text_IO",
qualified_name: "Iterators.Text_IO",
signature: "iterators.text_io",
enclosing: "iterators",
is_private: false,
documentation: "Read a file as a sequence of lines",
documentation_snippet: "",
simple_types:    [
       {
       name: "Ada_Cursor",
       qualified_name: "Iterators.Text_IO.Ada_Cursor",
       signature: "iterators.text_io.ada_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ada_Cursor is limited private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Ada_Iterator",
       qualified_name: "Iterators.Text_IO.Ada_Iterator",
       signature: "iterators.text_io.ada_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ada_Iterator (<>) is new\n  Ada.Finalization.Limited_Controlled\n  and Ada_Iterator_Interfaces.Forward_Iterator\nwith private with\n  Constant_Indexing  => Element,\n  Default_Iterator   => Iterate,\n  Iterator_Element   => String;",
       }   ,
   ]
,}
---

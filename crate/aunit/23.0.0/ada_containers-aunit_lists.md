---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "Ada_Containers.AUnit_Lists",
qualified_name: "Ada_Containers.AUnit_Lists",
signature: "ada_containers.aunit_lists",
enclosing: "ada_containers",
is_private: false,
documentation: "Some Ada2005 constructs have also been removed so that user tests can be\ncompiled in Ada95.\n\n@formal Element_Type\n@formal \"=\"",
documentation_snippet: "",
packages:    [
       {
       name: "Generic_Sorting",
       qualified_name: "Ada_Containers.AUnit_Lists.Generic_Sorting",
       signature: "ada_containers.aunit_lists.generic_sorting",
       enclosing: "ada_containers.aunit_lists",
       is_private: false,
       documentation: "procedure Reverse_Iterate\n  (Container : List;\n   Process   : not null access procedure (Position : Cursor));\n\n@formal \"<\"",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Cursor",
       qualified_name: "Ada_Containers.AUnit_Lists.Cursor",
       signature: "ada_containers.aunit_lists.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "List",
       qualified_name: "Ada_Containers.AUnit_Lists.List",
       signature: "ada_containers.aunit_lists.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Iterator",
       qualified_name: "Ada_Containers.AUnit_Lists.Iterator",
       signature: "ada_containers.aunit_lists.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator is access procedure (Position : Cursor);",
       }   ,
   ]
,constants:    [
       {
       name: "No_Element",
       qualified_name: "Ada_Containers.AUnit_Lists.No_Element",
       signature: "ada_containers.aunit_lists.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---

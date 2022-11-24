---
crate: dir_iterators
layout: gnatdoc
gnatdoc: {
name: "Dir_Iterators.Recursive",
qualified_name: "Dir_Iterators.Recursive",
signature: "dir_iterators.recursive",
enclosing: "dir_iterators",
is_private: false,
documentation: "A simple type to return each directory entry.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "Dir_Iterators.Recursive.Cursor",
       signature: "dir_iterators.recursive.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Reference_Type",
       qualified_name: "Dir_Iterators.Recursive.Reference_Type",
       signature: "dir_iterators.recursive.reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference_Type\n   (Element : not null access constant Ada.Directories\n       .Directory_Entry_Type)\nis null record with\n    Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Recursive_Dir_Iterator",
       qualified_name: "Dir_Iterators.Recursive.Recursive_Dir_Iterator",
       signature: "dir_iterators.recursive.recursive_dir_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recursive_Dir_Iterator(Filter : access function\n   (Dir_Entry : Ada.Directories.Directory_Entry_Type) return Boolean) is\n   new Ada.Finalization.Limited_Controlled and\n      Recursive_Dir_Iterator_Interfaces.Forward_Iterator with private;",
       }   ,
       {
       name: "Recursive_Dir_Walk",
       qualified_name: "Dir_Iterators.Recursive.Recursive_Dir_Walk",
       signature: "dir_iterators.recursive.recursive_dir_walk",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recursive_Dir_Walk (Filter : Filter_Function) is\n   tagged limited private with\n    Default_Iterator  => Iterate,\n    Iterator_Element  => Reference_Type,\n    Constant_Indexing => Element_Value;",
       }   ,
   ]
,access_types:    [
       {
       name: "Filter_Function",
       qualified_name: "Dir_Iterators.Recursive.Filter_Function",
       signature: "dir_iterators.recursive.filter_function",
       enclosing: "",
       is_private: false,
       documentation: "A function used to prune directories or files from the search results.\n\n@param Dir_Entry\n\n@return",
       documentation_snippet: "type Filter_Function is access function\n   (Dir_Entry : Ada.Directories.Directory_Entry_Type) return Boolean;",
       }   ,
   ]
,}
---

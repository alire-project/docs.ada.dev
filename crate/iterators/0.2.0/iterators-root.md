---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Root",
qualified_name: "Iterators.Root",
signature: "iterators.root",
enclosing: "iterators",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Const_Ref",
       qualified_name: "Iterators.Root.Const_Ref",
       signature: "iterators.root.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref (Element : access constant Any_Element) is limited null record with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Iterator_Reference",
       qualified_name: "Iterators.Root.Iterator_Reference",
       signature: "iterators.root.iterator_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator_Reference (Ptr : access Iterator'Class) is limited null record\n  with Implicit_Dereference => Ptr;",
       }   ,
       {
       name: "Reference",
       qualified_name: "Iterators.Root.Reference",
       signature: "iterators.root.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference (Element : access Any_Element) is limited null record with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Iterator",
       qualified_name: "Iterators.Root.Iterator",
       signature: "iterators.root.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator is interface with\n  Constant_Indexing => Get_Const_Ref,\n  Variable_Indexing => Get_Var_Ref,\n  Default_Iterator => Iterate,\n  Iterator_Element => Any_Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cursor",
       qualified_name: "Iterators.Root.Cursor",
       signature: "iterators.root.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is tagged private;",
       }   ,
       {
       name: "Holder",
       qualified_name: "Iterators.Root.Holder",
       signature: "iterators.root.holder",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Holder is new Holders.Holder with null record;",
       }   ,
       {
       name: "List",
       qualified_name: "Iterators.Root.List",
       signature: "iterators.root.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is new Lists.List with null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Elements",
       qualified_name: "Iterators.Root.Elements",
       signature: "iterators.root.elements",
       enclosing: "",
       is_private: false,
       documentation: "Work around visibility bug.",
       documentation_snippet: "subtype Elements is Any_Element;",
       }   ,
   ]
,}
---

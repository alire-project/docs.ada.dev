---
crate: optional
layout: gnatdoc
gnatdoc: {
name: "Optional.Values",
qualified_name: "Optional.Values",
signature: "optional.values",
enclosing: "optional",
is_private: false,
documentation: "Reference types\n\n@formal Element_Type\n@formal Image",
documentation_snippet: "",
record_types:    [
       {
       name: "Const_Ref",
       qualified_name: "Optional.Values.Const_Ref",
       signature: "optional.values.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref (Ptr : access constant Element_Type) is\nlimited null record with Implicit_Dereference => Ptr;",
       }   ,
       {
       name: "Var_Ref",
       qualified_name: "Optional.Values.Var_Ref",
       signature: "optional.values.var_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Var_Ref (Ptr : access Element_Type) is\nlimited null record with Implicit_Dereference => Ptr;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Optional",
       qualified_name: "Optional.Values.Optional",
       signature: "optional.values.optional",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Optional is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty",
       qualified_name: "Optional.Values.Empty",
       signature: "optional.values.empty",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty : constant Optional;",
       }   ,
   ]
,}
---

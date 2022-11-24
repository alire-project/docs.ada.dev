---
crate: aaa
layout: gnatdoc
gnatdoc: {
name: "AAA.Containers.Indefinite_Holders",
qualified_name: "AAA.Containers.Indefinite_Holders",
signature: "aaa.containers.indefinite_holders",
enclosing: "aaa.containers",
is_private: false,
documentation: "Simple holder to work around GNAT holders bug\n\n@formal Held",
documentation_snippet: "",
record_types:    [
       {
       name: "Const_Ref_Value",
       qualified_name: "AAA.Containers.Indefinite_Holders.Const_Ref_Value",
       signature: "aaa.containers.indefinite_holders.const_ref_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref_Value (Element : access constant Held) is limited null record\n  with Implicit_Dereference => Element;",
       }   ,
       {
       name: "Reference_Value",
       qualified_name: "AAA.Containers.Indefinite_Holders.Reference_Value",
       signature: "aaa.containers.indefinite_holders.reference_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference_Value (Element : access Held) is limited null record with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Holder",
       qualified_name: "AAA.Containers.Indefinite_Holders.Holder",
       signature: "aaa.containers.indefinite_holders.holder",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Holder is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Holder",
       qualified_name: "AAA.Containers.Indefinite_Holders.Empty_Holder",
       signature: "aaa.containers.indefinite_holders.empty_holder",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Holder : constant Holder;",
       }   ,
   ]
,}
---

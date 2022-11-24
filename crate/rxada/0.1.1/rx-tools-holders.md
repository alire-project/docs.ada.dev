---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Tools.Holders",
qualified_name: "Rx.Tools.Holders",
signature: "rx.tools.holders",
enclosing: "rx.tools",
is_private: false,
documentation: "\n@formal Indef\n@formal Id\n  Debug purposes only",
documentation_snippet: "",
record_types:    [
       {
       name: "Const_Ref",
       qualified_name: "Rx.Tools.Holders.Const_Ref",
       signature: "rx.tools.holders.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref (Actual : access constant Indef) is limited null record\n	with Implicit_Dereference => Actual;",
       }   ,
       {
       name: "Reference",
       qualified_name: "Rx.Tools.Holders.Reference",
       signature: "rx.tools.holders.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference (Actual : access Indef) is limited null record\n	with Implicit_Dereference => Actual;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Definite",
       qualified_name: "Rx.Tools.Holders.Definite",
       signature: "rx.tools.holders.definite",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Definite is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Indef_Access",
       qualified_name: "Rx.Tools.Holders.Indef_Access",
       signature: "rx.tools.holders.indef_access",
       enclosing: "",
       is_private: false,
       documentation: "for Indef_Access'Storage_Pool use Debug.Debug_Pool;",
       documentation_snippet: "type Indef_Access is access Indef;",
       }   ,
   ]
,}
---

---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Tools.Shared_Data",
qualified_name: "Rx.Tools.Shared_Data",
signature: "rx.tools.shared_data",
enclosing: "rx.tools",
is_private: false,
documentation: "Your typical refcounted thread-safe access type\n\n@formal Item\n@formal Item_Access\n@formal Debug_Name",
documentation_snippet: "",
simple_types:    [
       {
       name: "Const_Ref",
       qualified_name: "Rx.Tools.Shared_Data.Const_Ref",
       signature: "rx.tools.shared_data.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref (Actual : access constant Item) is limited private\n  with Implicit_Dereference => Actual;",
       }   ,
       {
       name: "Ref",
       qualified_name: "Rx.Tools.Shared_Data.Ref",
       signature: "rx.tools.shared_data.ref",
       enclosing: "",
       is_private: false,
       documentation: "UNSAFE unless Item is actually synchronized itself\nThis should ideally be moved to a separate package with a synchronized interface",
       documentation_snippet: "type Ref (Actual : access Item) is limited private\n  with Implicit_Dereference => Actual;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Proxy",
       qualified_name: "Rx.Tools.Shared_Data.Proxy",
       signature: "rx.tools.shared_data.proxy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proxy is tagged private;",
       }   ,
   ]
,}
---

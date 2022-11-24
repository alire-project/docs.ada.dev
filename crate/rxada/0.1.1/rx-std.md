---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Std",
qualified_name: "Rx.Std",
signature: "rx.std",
enclosing: "rx",
is_private: false,
documentation: "Instances and default visibility for some predefined types\nAlso default sources/operators from ReactiveX documentation",
documentation_snippet: "",
packages:    [
       {
       name: "Casts",
       qualified_name: "Rx.Std.Casts",
       signature: "rx.std.casts",
       enclosing: "rx.std",
       is_private: false,
       documentation: "Casts for predefined types",
       documentation_snippet: "",
       }   ,
       {
       name: "Images",
       qualified_name: "Rx.Std.Images",
       signature: "rx.std.images",
       enclosing: "rx.std",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,subtypes:    [
       {
       name: "Printable_Character",
       qualified_name: "Rx.Std.Printable_Character",
       signature: "rx.std.printable_character",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Printable_Character is Character range Character'Val (16#20#) .. Character'Val (16#7E#);",
       }   ,
       {
       name: "Subscription",
       qualified_name: "Rx.Std.Subscription",
       signature: "rx.std.subscription",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Subscription is Rx.Subscriptions.Subscription;",
       }   ,
   ]
,}
---

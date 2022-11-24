---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Sax.Locators",
qualified_name: "Sax.Locators",
signature: "sax.locators",
enclosing: "sax",
is_private: false,
documentation: "-----------------------------------------------\n General Locator interface as defined in SAX --\n-----------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Locator",
       qualified_name: "Sax.Locators.Locator",
       signature: "sax.locators.locator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Locator is abstract tagged private;",
       }   ,
       {
       name: "Locator_Impl",
       qualified_name: "Sax.Locators.Locator_Impl",
       signature: "sax.locators.locator_impl",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Locator_Impl is new Locator with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Locator_Access",
       qualified_name: "Sax.Locators.Locator_Access",
       signature: "sax.locators.locator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Locator_Access is access all Locator'Class;",
       }   ,
       {
       name: "Locator_Impl_Access",
       qualified_name: "Sax.Locators.Locator_Impl_Access",
       signature: "sax.locators.locator_impl_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Locator_Impl_Access is access all Locator_Impl'Class;",
       }   ,
   ]
,}
---

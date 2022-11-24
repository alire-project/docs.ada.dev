---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Locales",
qualified_name: "ASF.Locales",
signature: "asf.locales",
enclosing: "asf",
is_private: false,
documentation: "To keep the implementation simple, the maximum list of supported locales by the\napplication is limited to 32.  Most applications support 1 or 2 languages.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Factory",
       qualified_name: "ASF.Locales.Factory",
       signature: "asf.locales.factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory is limited private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Bundle",
       qualified_name: "ASF.Locales.Bundle",
       signature: "asf.locales.bundle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bundle is new Util.Properties.Bundles.Manager\n  and Util.Beans.Basic.Readonly_Bean with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Bundle_Access",
       qualified_name: "ASF.Locales.Bundle_Access",
       signature: "asf.locales.bundle_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bundle_Access is access all Bundle;",
       }   ,
   ]
,constants:    [
       {
       name: "MAX_SUPPORTED_LOCALES",
       qualified_name: "ASF.Locales.MAX_SUPPORTED_LOCALES",
       signature: "asf.locales.max_supported_locales",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_SUPPORTED_LOCALES : constant Positive := 32;",
       }   ,
   ]
,}
---

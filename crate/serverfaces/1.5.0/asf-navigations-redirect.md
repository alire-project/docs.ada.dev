---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Navigations.Redirect",
qualified_name: "ASF.Navigations.Redirect",
signature: "asf.navigations.redirect",
enclosing: "asf.navigations",
is_private: false,
documentation: "------------------------------\nRedirect page navigator\n------------------------------\nThe <b>Redirect_Navigator</b> handles the redirection rule for the navigation.\nThe redirection view can contain EL expressions that will be evaluated when the\nredirect rule is executed.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Redirect_Navigator",
       qualified_name: "ASF.Navigations.Redirect.Redirect_Navigator",
       signature: "asf.navigations.redirect.redirect_navigator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Redirect_Navigator is new Navigation_Case with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Redirect_Navigator_Access",
       qualified_name: "ASF.Navigations.Redirect.Redirect_Navigator_Access",
       signature: "asf.navigations.redirect.redirect_navigator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Redirect_Navigator_Access is access all Redirect_Navigator'Class;",
       }   ,
   ]
,}
---

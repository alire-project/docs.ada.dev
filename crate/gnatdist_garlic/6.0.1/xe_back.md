---
crate: gnatdist_garlic
layout: gnatdoc
gnatdoc: {
name: "XE_Back",
qualified_name: "XE_Back",
signature: "xe_back",
enclosing: "",
is_private: false,
documentation: "This package and its children define all the routines to generate stubs\n(object files), skeleton files (object files), PCS units (source and\nobject files) and eventually executable files.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Backend",
       qualified_name: "XE_Back.Backend",
       signature: "xe_back.backend",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Backend is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Backend_Access",
       qualified_name: "XE_Back.Backend_Access",
       signature: "xe_back.backend_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Backend_Access is access all Backend'Class;",
       }   ,
   ]
,variables:    [
       {
       name: "PCS_Conf_Unit",
       qualified_name: "XE_Back.PCS_Conf_Unit",
       signature: "xe_back.pcs_conf_unit",
       enclosing: "",
       is_private: false,
       documentation: "Define a PCS unit that gnatdist has to automatically configure\non the main partition.",
       documentation_snippet: "PCS_Conf_Unit : Name_Id := No_Name;",
       }   ,
   ]
,}
---

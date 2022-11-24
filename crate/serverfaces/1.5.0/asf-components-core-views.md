---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Components.Core.Views",
qualified_name: "ASF.Components.Core.Views",
signature: "asf.components.core.views",
enclosing: "asf.components.core",
is_private: false,
documentation: "Name of the facet that holds the metadata information\n(we use the same name as JSF 2 specification).",
documentation_snippet: "",
tagged_types:    [
       {
       name: "UIView",
       qualified_name: "ASF.Components.Core.Views.UIView",
       signature: "asf.components.core.views.uiview",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIView is new Core.UIComponentBase with private;",
       }   ,
       {
       name: "UIViewAction",
       qualified_name: "ASF.Components.Core.Views.UIViewAction",
       signature: "asf.components.core.views.uiviewaction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewAction is new Html.Forms.UICommand with private;",
       }   ,
       {
       name: "UIViewMetaData",
       qualified_name: "ASF.Components.Core.Views.UIViewMetaData",
       signature: "asf.components.core.views.uiviewmetadata",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewMetaData is new UIView with private;",
       }   ,
       {
       name: "UIViewParameter",
       qualified_name: "ASF.Components.Core.Views.UIViewParameter",
       signature: "asf.components.core.views.uiviewparameter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewParameter is new Html.Forms.UIInput with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "UIView_Access",
       qualified_name: "ASF.Components.Core.Views.UIView_Access",
       signature: "asf.components.core.views.uiview_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIView_Access is access all UIView'Class;",
       }   ,
       {
       name: "UIViewAction_Access",
       qualified_name: "ASF.Components.Core.Views.UIViewAction_Access",
       signature: "asf.components.core.views.uiviewaction_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewAction_Access is access all UIViewAction'Class;",
       }   ,
       {
       name: "UIViewMetaData_Access",
       qualified_name: "ASF.Components.Core.Views.UIViewMetaData_Access",
       signature: "asf.components.core.views.uiviewmetadata_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewMetaData_Access is access all UIViewMetaData'Class;",
       }   ,
       {
       name: "UIViewParameter_Access",
       qualified_name: "ASF.Components.Core.Views.UIViewParameter_Access",
       signature: "asf.components.core.views.uiviewparameter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIViewParameter_Access is access all UIViewParameter'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "METADATA_FACET_NAME",
       qualified_name: "ASF.Components.Core.Views.METADATA_FACET_NAME",
       signature: "asf.components.core.views.metadata_facet_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "METADATA_FACET_NAME : constant String := \"javax_faces_metadata\";",
       }   ,
   ]
,}
---

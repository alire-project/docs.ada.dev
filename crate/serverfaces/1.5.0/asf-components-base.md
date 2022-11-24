---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Components.Base",
qualified_name: "ASF.Components.Base",
signature: "asf.components.base",
enclosing: "asf.components",
is_private: false,
documentation: "The <bASF.Components</b> describes the components that form the\ntree view.  Each component has attributes and children.  Children\nrepresent sub-components and attributes control the rendering and\nbehavior of the component.\n\nThe component tree is created from the <b>ASF.Views</b> tag nodes\nfor each request.  Unlike tag nodes, the component tree is not shared.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "ASF.Components.Base.Cursor",
       signature: "asf.components.base.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "UIComponent_List",
       qualified_name: "ASF.Components.Base.UIComponent_List",
       signature: "asf.components.base.uicomponent_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponent_List is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "UIComponent_Array",
       qualified_name: "ASF.Components.Base.UIComponent_Array",
       signature: "asf.components.base.uicomponent_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponent_Array is array (Natural range <>) of UIComponent_Access;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "UIComponent",
       qualified_name: "ASF.Components.Base.UIComponent",
       signature: "asf.components.base.uicomponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponent is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "UIComponent_Access",
       qualified_name: "ASF.Components.Base.UIComponent_Access",
       signature: "asf.components.base.uicomponent_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponent_Access is access all UIComponent'Class;",
       }   ,
       {
       name: "UIComponent_Array_Access",
       qualified_name: "ASF.Components.Base.UIComponent_Array_Access",
       signature: "asf.components.base.uicomponent_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponent_Array_Access is access UIComponent_Array;",
       }   ,
   ]
,}
---

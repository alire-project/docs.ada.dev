---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Components.Core",
qualified_name: "ASF.Components.Core",
signature: "asf.components.core",
enclosing: "asf.components",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "UIParameter_Access_Array",
       qualified_name: "ASF.Components.Core.UIParameter_Access_Array",
       signature: "asf.components.core.uiparameter_access_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIParameter_Access_Array is array (Natural range <>) of UIParameter_Access;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "UIComponentBase",
       qualified_name: "ASF.Components.Core.UIComponentBase",
       signature: "asf.components.core.uicomponentbase",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComponentBase is new Base.UIComponent with null record;",
       }   ,
       {
       name: "UILeaf",
       qualified_name: "ASF.Components.Core.UILeaf",
       signature: "asf.components.core.uileaf",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UILeaf is new UIComponentBase with private;",
       }   ,
       {
       name: "UIParameter",
       qualified_name: "ASF.Components.Core.UIParameter",
       signature: "asf.components.core.uiparameter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIParameter is new UILeaf with private;",
       }   ,
       {
       name: "UIText",
       qualified_name: "ASF.Components.Core.UIText",
       signature: "asf.components.core.uitext",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIText is new Base.UIComponent with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "UIParameter_Access",
       qualified_name: "ASF.Components.Core.UIParameter_Access",
       signature: "asf.components.core.uiparameter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIParameter_Access is access all UIParameter'Class;",
       }   ,
       {
       name: "UIText_Access",
       qualified_name: "ASF.Components.Core.UIText_Access",
       signature: "asf.components.core.uitext_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIText_Access is access all UIText'Class;",
       }   ,
   ]
,}
---

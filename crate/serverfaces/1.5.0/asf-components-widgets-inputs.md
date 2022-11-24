---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Components.Widgets.Inputs",
qualified_name: "ASF.Components.Widgets.Inputs",
signature: "asf.components.widgets.inputs",
enclosing: "asf.components.widgets",
is_private: false,
documentation: "  ------------------------------\n  Input component\n  ------------------------------\n  The AWA input component overrides the ASF input component to build a compact component\n  that displays a label, the input field and the associated error message if necessary.\n\n  The generated HTML looks like:\n\n  <dl class='... awa-error'>\n    <dt>title <i>required</i></dt>\n    <dd><input type='text' ...> <em/>\n        <span class='...'>message</span>\n    </dd>\n  </dl>",
documentation_snippet: "",
tagged_types:    [
       {
       name: "UIComplete",
       qualified_name: "ASF.Components.Widgets.Inputs.UIComplete",
       signature: "asf.components.widgets.inputs.uicomplete",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComplete is new UIInput with private;",
       }   ,
       {
       name: "UIInput",
       qualified_name: "ASF.Components.Widgets.Inputs.UIInput",
       signature: "asf.components.widgets.inputs.uiinput",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIInput is new ASF.Components.Html.Forms.UIInput with null record;",
       }   ,
       {
       name: "UIInputDate",
       qualified_name: "ASF.Components.Widgets.Inputs.UIInputDate",
       signature: "asf.components.widgets.inputs.uiinputdate",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIInputDate is new UIInput with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "UIComplete_Access",
       qualified_name: "ASF.Components.Widgets.Inputs.UIComplete_Access",
       signature: "asf.components.widgets.inputs.uicomplete_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIComplete_Access is access all UIInput'Class;",
       }   ,
       {
       name: "UIInput_Access",
       qualified_name: "ASF.Components.Widgets.Inputs.UIInput_Access",
       signature: "asf.components.widgets.inputs.uiinput_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIInput_Access is access all UIInput'Class;",
       }   ,
       {
       name: "UIInputDate_Access",
       qualified_name: "ASF.Components.Widgets.Inputs.UIInputDate_Access",
       signature: "asf.components.widgets.inputs.uiinputdate_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UIInputDate_Access is access all UIInputDate'Class;",
       }   ,
   ]
,}
---

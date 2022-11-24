---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Methods.Func_1",
qualified_name: "EL.Methods.Func_1",
signature: "el.methods.func_1",
enclosing: "el.methods",
is_private: false,
documentation: "Returns True if the method is a valid method which accepts the arguments\ndefined by the package instantiation.\n\n@formal Param1_Type\n@formal Return_Type",
documentation_snippet: "",
packages:    [
       {
       name: "Bind",
       qualified_name: "EL.Methods.Func_1.Bind",
       signature: "el.methods.func_1.bind",
       enclosing: "el.methods.func_1",
       is_private: false,
       documentation: "Method that <b>Execute</b> will invoke.\n\n@formal Name\n  The bean type\n@formal Bean\n  The bean method to invoke\n@formal Method",
       documentation_snippet: "",
constants:           [
              {
              name: "F_NAME",
              qualified_name: "EL.Methods.Func_1.Bind.F_NAME",
              signature: "el.methods.func_1.bind.f_name",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "F_NAME : aliased constant String := Name;",
              }          ,
              {
              name: "Proxy",
              qualified_name: "EL.Methods.Func_1.Bind.Proxy",
              signature: "el.methods.func_1.bind.proxy",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Proxy  : aliased constant Binding\n  := Binding '(Name => F_NAME'Access,\n               Method => Method_Access'Access);",
              }          ,
          ]
,       }   ,
   ]
,tagged_types:    [
       {
       name: "Binding",
       qualified_name: "EL.Methods.Func_1.Binding",
       signature: "el.methods.func_1.binding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding is new Method_Binding with record\n   Method : Proxy_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Binding_Access",
       qualified_name: "EL.Methods.Func_1.Binding_Access",
       signature: "el.methods.func_1.binding_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Access is access constant Binding;",
       }   ,
       {
       name: "Proxy_Access",
       qualified_name: "EL.Methods.Func_1.Proxy_Access",
       signature: "el.methods.func_1.proxy_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proxy_Access is\n  access function (O : in Util.Beans.Basic.Readonly_Bean'Class;\n                   P : in Param1_Type) return Return_Type;",
       }   ,
   ]
,}
---

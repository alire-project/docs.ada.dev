---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Factory",
qualified_name: "ASF.Factory",
signature: "asf.factory",
enclosing: "asf",
is_private: false,
documentation: "------------------------------\nList of bindings\n------------------------------\nThe binding array defines a set of XML entity names that represent\na library accessible through a XML name-space.  The binding array\nmust be sorted on the binding name.  The <b>Check</b> procedure will\nverify this assumption when the bindings are registered in the factory.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Component_Factory",
       qualified_name: "ASF.Factory.Component_Factory",
       signature: "asf.factory.component_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Component_Factory is limited private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Binding_Array",
       qualified_name: "ASF.Factory.Binding_Array",
       signature: "asf.factory.binding_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Array is array (Natural range <>) of aliased ASF.Views.Nodes.Binding_Type;",
       }   ,
   ]
,record_types:    [
       {
       name: "Factory_Bindings",
       qualified_name: "ASF.Factory.Factory_Bindings",
       signature: "asf.factory.factory_bindings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory_Bindings is limited record\n   URI      : ASF.Views.Nodes.Name_Access;\n   Bindings : Binding_Array_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Binding_Array_Access",
       qualified_name: "ASF.Factory.Binding_Array_Access",
       signature: "asf.factory.binding_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Array_Access is access constant Binding_Array;",
       }   ,
       {
       name: "Factory_Bindings_Access",
       qualified_name: "ASF.Factory.Factory_Bindings_Access",
       signature: "asf.factory.factory_bindings_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory_Bindings_Access is access constant Factory_Bindings;",
       }   ,
   ]
,}
---

---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Beans",
qualified_name: "ASF.Beans",
signature: "asf.beans",
enclosing: "asf",
is_private: false,
documentation: "Defines the scope of the bean instance.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Bean_Factory",
       qualified_name: "ASF.Beans.Bean_Factory",
       signature: "asf.beans.bean_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bean_Factory is limited private;",
       }   ,
       {
       name: "Scope_Type",
       qualified_name: "ASF.Beans.Scope_Type",
       signature: "asf.beans.scope_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Scope_Type is\n  (\n   APPLICATION_SCOPE,\n   SESSION_SCOPE,\n   REQUEST_SCOPE,\n   ANY_SCOPE);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Class_Binding",
       qualified_name: "ASF.Beans.Class_Binding",
       signature: "asf.beans.class_binding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Class_Binding is abstract new Util.Refs.Ref_Entity with null record;",
       }   ,
       {
       name: "Parameter_Bean",
       qualified_name: "ASF.Beans.Parameter_Bean",
       signature: "asf.beans.parameter_bean",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter_Bean is new Util.Refs.Ref_Entity with record\n   Params : EL.Beans.Param_Vectors.Vector;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Class_Binding_Access",
       qualified_name: "ASF.Beans.Class_Binding_Access",
       signature: "asf.beans.class_binding_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Class_Binding_Access is access all Class_Binding'Class;",
       }   ,
       {
       name: "Create_Bean_Access",
       qualified_name: "ASF.Beans.Create_Bean_Access",
       signature: "asf.beans.create_bean_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Bean_Access is access function return Util.Beans.Basic.Readonly_Bean_Access;",
       }   ,
       {
       name: "Parameter_Bean_Access",
       qualified_name: "ASF.Beans.Parameter_Bean_Access",
       signature: "asf.beans.parameter_bean_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter_Bean_Access is access all Parameter_Bean;",
       }   ,
   ]
,}
---

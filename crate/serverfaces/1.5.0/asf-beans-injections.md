---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Beans.Injections",
qualified_name: "ASF.Beans.Injections",
signature: "asf.beans.injections",
enclosing: "asf.beans",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Inject_Array_Type",
       qualified_name: "ASF.Beans.Injections.Inject_Array_Type",
       signature: "asf.beans.injections.inject_array_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inject_Array_Type is array (Positive) of Inject_Type;",
       }   ,
   ]
,record_types:    [
       {
       name: "Inject_Type",
       qualified_name: "ASF.Beans.Injections.Inject_Type",
       signature: "asf.beans.injections.inject_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inject_Type is record\n   Handler : Injection_Handler;\n   Name    : Util.Strings.Name_Access;\n   Param   : Util.Strings.Name_Access;\n   Pos     : Natural := 0;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Injection_Handler",
       qualified_name: "ASF.Beans.Injections.Injection_Handler",
       signature: "asf.beans.injections.injection_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Injection_Handler is not null access\n  procedure (Bean       : in out Util.Beans.Basic.Bean'Class;\n             Descriptor : in Inject_Type;\n             Request    : in ASF.Requests.Request'Class);",
       }   ,
   ]
,}
---

---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Objects",
qualified_name: "ADO.Objects",
signature: "ado.objects",
enclosing: "ado",
is_private: false,
documentation: "The object was modified by a another transaction.\nThis exception is raised by 'Save'.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object_Key",
       qualified_name: "ADO.Objects.Object_Key",
       signature: "ado.objects.object_key",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Key (Of_Type  : Object_Key_Type;\n                 Of_Class : Schemas.Class_Mapping_Access) is private;",
       }   ,
       {
       name: "Object_Key_Type",
       qualified_name: "ADO.Objects.Object_Key_Type",
       signature: "ado.objects.object_key_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Key_Type is (KEY_INTEGER, KEY_STRING);",
       }   ,
       {
       name: "Session_Proxy",
       qualified_name: "ADO.Objects.Session_Proxy",
       signature: "ado.objects.session_proxy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Proxy is limited private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Modified_Map",
       qualified_name: "ADO.Objects.Modified_Map",
       signature: "ado.objects.modified_map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Modified_Map is array (Column_Index range 1 .. 64) of Boolean;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object_Record",
       qualified_name: "ADO.Objects.Object_Record",
       signature: "ado.objects.object_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Record (Key_Type : Object_Key_Type;\n                    Of_Class : ADO.Schemas.Class_Mapping_Access) is abstract\n    new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Object_Ref",
       qualified_name: "ADO.Objects.Object_Ref",
       signature: "ado.objects.object_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Ref is abstract\n   new Ada.Finalization.Controlled and Util.Beans.Basic.Readonly_Bean with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Record_Access",
       qualified_name: "ADO.Objects.Object_Record_Access",
       signature: "ado.objects.object_record_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Record_Access is access all Object_Record'Class;",
       }   ,
       {
       name: "Session_Proxy_Access",
       qualified_name: "ADO.Objects.Session_Proxy_Access",
       signature: "ado.objects.session_proxy_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Proxy_Access is access all Session_Proxy;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Column_Index",
       qualified_name: "ADO.Objects.Column_Index",
       signature: "ado.objects.column_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Column_Index is ADO.Schemas.Column_Index;",
       }   ,
   ]
,}
---

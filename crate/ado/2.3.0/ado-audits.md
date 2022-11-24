---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Audits",
qualified_name: "ADO.Audits",
signature: "ado.audits",
enclosing: "ado",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Audit_Index",
       qualified_name: "ADO.Audits.Audit_Index",
       signature: "ado.audits.audit_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Index is new Positive range 1 .. ADO.Configs.MAX_COLUMNS;",
       }   ,
       {
       name: "Audit_Info_Index",
       qualified_name: "ADO.Audits.Audit_Info_Index",
       signature: "ado.audits.audit_info_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Info_Index is new Positive range 1 .. ADO.Configs.MAX_COLUMNS;",
       }   ,
   ]
,array_types:    [
       {
       name: "Audit_Array",
       qualified_name: "ADO.Audits.Audit_Array",
       signature: "ado.audits.audit_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Array is array (Audit_Info_Index range <>) of Audit_Info;",
       }   ,
       {
       name: "Column_Index_Array",
       qualified_name: "ADO.Audits.Column_Index_Array",
       signature: "ado.audits.column_index_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Index_Array is array (Audit_Index range <>) of Column_Index;",
       }   ,
   ]
,record_types:    [
       {
       name: "Audit_Info",
       qualified_name: "ADO.Audits.Audit_Info",
       signature: "ado.audits.audit_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Info is limited record\n   Field     : Column_Index := 0;\n   Old_Value : UBO.Object;\n   New_Value : UBO.Object;\nend record;",
       }   ,
       {
       name: "Auditable_Mapping",
       qualified_name: "ADO.Audits.Auditable_Mapping",
       signature: "ado.audits.auditable_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auditable_Mapping (Of_Class : ADO.Schemas.Class_Mapping_Access;\n                        Count    : Audit_Index)\nis tagged limited record\n   Members : Column_Index_Array (1 .. Count);\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Audit_Manager",
       qualified_name: "ADO.Audits.Audit_Manager",
       signature: "ado.audits.audit_manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Manager is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Auditable_Object_Record",
       qualified_name: "ADO.Audits.Auditable_Object_Record",
       signature: "ado.audits.auditable_object_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auditable_Object_Record (Key_Type   : Object_Key_Type;\n                              Of_Class   : Class_Mapping_Access;\n                              With_Audit : Auditable_Mapping_Access) is abstract\n    new ADO.Objects.Object_Record with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Audit_Manager_Access",
       qualified_name: "ADO.Audits.Audit_Manager_Access",
       signature: "ado.audits.audit_manager_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audit_Manager_Access is access all Audit_Manager'Class;",
       }   ,
       {
       name: "Auditable_Mapping_Access",
       qualified_name: "ADO.Audits.Auditable_Mapping_Access",
       signature: "ado.audits.auditable_mapping_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Auditable_Mapping_Access is access constant Auditable_Mapping'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class_Mapping_Access",
       qualified_name: "ADO.Audits.Class_Mapping_Access",
       signature: "ado.audits.class_mapping_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class_Mapping_Access is ADO.Schemas.Class_Mapping_Access;",
       }   ,
       {
       name: "Column_Index",
       qualified_name: "ADO.Audits.Column_Index",
       signature: "ado.audits.column_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Column_Index is ADO.Schemas.Column_Index;",
       }   ,
       {
       name: "Object_Key_Type",
       qualified_name: "ADO.Audits.Object_Key_Type",
       signature: "ado.audits.object_key_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Object_Key_Type is ADO.Objects.Object_Key_Type;",
       }   ,
   ]
,}
---

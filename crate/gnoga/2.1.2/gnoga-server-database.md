---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Database",
qualified_name: "Gnoga.Server.Database",
signature: "gnoga.server.database",
enclosing: "gnoga.server",
is_private: false,
documentation: "Abstract class for database access. Use one of the specific implementations\nfor MySQL, SQLLite, etc.",
documentation_snippet: "",
record_types:    [
       {
       name: "Field_Description",
       qualified_name: "Gnoga.Server.Database.Field_Description",
       signature: "gnoga.server.database.field_description",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Field_Description is record\n   Column_Name   : String;\n   Data_Type     : String;\n   Can_Be_Null   : Boolean;\n   Default_Value : String;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Connection",
       qualified_name: "Gnoga.Server.Database.Connection",
       signature: "gnoga.server.database.connection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection is limited interface;",
       }   ,
       {
       name: "Recordset",
       qualified_name: "Gnoga.Server.Database.Recordset",
       signature: "gnoga.server.database.recordset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recordset is interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Connection_Access",
       qualified_name: "Gnoga.Server.Database.Connection_Access",
       signature: "gnoga.server.database.connection_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection_Access is access all Connection'Class;",
       }   ,
       {
       name: "Recordset_Access",
       qualified_name: "Gnoga.Server.Database.Recordset_Access",
       signature: "gnoga.server.database.recordset_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Recordset_Access is access all Recordset'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Field_Description_Array_Type",
       qualified_name: "Gnoga.Server.Database.Field_Description_Array_Type",
       signature: "gnoga.server.database.field_description_array_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Field_Description_Array_Type is Field_Description_Arrays.Vector;",
       }   ,
   ]
,}
---

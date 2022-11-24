---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Parameters",
qualified_name: "ADO.Parameters",
signature: "ado.parameters",
enclosing: "ado",
is_private: false,
documentation: "---------------------------------------------------------------------\n  ADO Parameters -- Parameters for queries\n  Copyright (C) 2010, 2011, 2012, 2013, 2015, 2017, 2019, 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parameter_Type",
       qualified_name: "ADO.Parameters.Parameter_Type",
       signature: "ado.parameters.parameter_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter_Type is (T_NULL, T_STRING, T_TOKEN, T_LIST, T_DATE, T_LONG_INTEGER,\n                        T_INTEGER, T_BOOLEAN, T_LONG_FLOAT, T_BLOB);",
       }   ,
       {
       name: "Token",
       qualified_name: "ADO.Parameters.Token",
       signature: "ado.parameters.token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token is new String;",
       }   ,
   ]
,record_types:    [
       {
       name: "Parameter",
       qualified_name: "ADO.Parameters.Parameter",
       signature: "ado.parameters.parameter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parameter (T   : Parameter_Type;\n                Len : Natural;\n                Value_Len : Natural) is\n   record\n      Position : Natural := 0;\n      Name     : String (1 .. Len);\n      case T is\n      when T_NULL =>\n         null;\n      when T_LONG_INTEGER =>\n         Long_Num : Long_Long_Integer := 0;\n      when T_INTEGER =>\n         Num : Integer;\n      when T_BOOLEAN =>\n         Bool : Boolean;\n      when T_LONG_FLOAT =>\n         Float : Long_Float;\n      when T_DATE =>\n         Time : Ada.Calendar.Time;\n      when T_BLOB =>\n         Data : ADO.Blob_Ref;\n      when others =>\n         Str : String (1 .. Value_Len);\n      end case;\n   end record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Expander",
       qualified_name: "ADO.Parameters.Expander",
       signature: "ado.parameters.expander",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expander is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Abstract_List",
       qualified_name: "ADO.Parameters.Abstract_List",
       signature: "ado.parameters.abstract_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Abstract_List is abstract new Ada.Finalization.Controlled with private;",
       }   ,
       {
       name: "List",
       qualified_name: "ADO.Parameters.List",
       signature: "ado.parameters.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is new Abstract_List with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Abstract_List_Access",
       qualified_name: "ADO.Parameters.Abstract_List_Access",
       signature: "ado.parameters.abstract_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Abstract_List_Access is access all Abstract_List'Class;",
       }   ,
       {
       name: "Expander_Access",
       qualified_name: "ADO.Parameters.Expander_Access",
       signature: "ado.parameters.expander_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expander_Access is access all Expander'Class;",
       }   ,
   ]
,}
---

---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Statements",
qualified_name: "ADO.Statements",
signature: "ado.statements",
enclosing: "ado",
is_private: false,
documentation: "---------------------------------------------------------------------\n  ado-statements -- Database statements\n  Copyright (C) 2009 - 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Delete_Statement",
       qualified_name: "ADO.Statements.Delete_Statement",
       signature: "ado.statements.delete_statement",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Delete_Statement is new Statement with private;",
       }   ,
       {
       name: "Insert_Statement",
       qualified_name: "ADO.Statements.Insert_Statement",
       signature: "ado.statements.insert_statement",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Insert_Statement is new Update_Statement with private;",
       }   ,
       {
       name: "Query_Statement",
       qualified_name: "ADO.Statements.Query_Statement",
       signature: "ado.statements.query_statement",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Statement is new Statement with private;",
       }   ,
       {
       name: "Statement",
       qualified_name: "ADO.Statements.Statement",
       signature: "ado.statements.statement",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Statement is abstract new ADO.Parameters.Abstract_List with private;",
       }   ,
       {
       name: "Update_Statement",
       qualified_name: "ADO.Statements.Update_Statement",
       signature: "ado.statements.update_statement",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Update_Statement is new Statement with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Delete_Statement_Access",
       qualified_name: "ADO.Statements.Delete_Statement_Access",
       signature: "ado.statements.delete_statement_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Delete_Statement_Access is access all Delete_Statement'Class;",
       }   ,
       {
       name: "Insert_Statement_Access",
       qualified_name: "ADO.Statements.Insert_Statement_Access",
       signature: "ado.statements.insert_statement_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Insert_Statement_Access is access all Insert_Statement'Class;",
       }   ,
       {
       name: "Query_Statement_Access",
       qualified_name: "ADO.Statements.Query_Statement_Access",
       signature: "ado.statements.query_statement_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Statement_Access is access all Query_Statement'Class;",
       }   ,
       {
       name: "Statement_Access",
       qualified_name: "ADO.Statements.Statement_Access",
       signature: "ado.statements.statement_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Statement_Access is access all Statement'Class;",
       }   ,
       {
       name: "Update_Statement_Access",
       qualified_name: "ADO.Statements.Update_Statement_Access",
       signature: "ado.statements.update_statement_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Update_Statement_Access is access all Update_Statement'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Query_String",
       qualified_name: "ADO.Statements.Query_String",
       signature: "ado.statements.query_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Query_String is String;",
       }   ,
   ]
,}
---

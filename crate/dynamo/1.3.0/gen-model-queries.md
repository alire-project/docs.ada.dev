---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.Queries",
qualified_name: "Gen.Model.Queries",
signature: "gen.model.queries",
enclosing: "gen.model",
is_private: false,
documentation: "------------------------------\nSort definition\n------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Query_Definition",
       qualified_name: "Gen.Model.Queries.Query_Definition",
       signature: "gen.model.queries.query_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Definition is new Gen.Model.Tables.Table_Definition with record\n   Sorts_Bean     : UBO.Object;\n   Sorts          : aliased Sort_List.List_Definition;\nend record;",
       }   ,
       {
       name: "Query_File_Definition",
       qualified_name: "Gen.Model.Queries.Query_File_Definition",
       signature: "gen.model.queries.query_file_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_File_Definition is new Query_Definition with record\n   File_Name      : UString;\n   Sha1           : Util.Encoders.SHA1.Digest;\n   Queries        : aliased Gen.Model.Tables.Table_List.List_Definition;\n   Queries_Bean   : UBO.Object;\nend record;",
       }   ,
       {
       name: "Sort_Definition",
       qualified_name: "Gen.Model.Queries.Sort_Definition",
       signature: "gen.model.queries.sort_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sort_Definition is new Definition with record\n   Sql    : UString;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Query_Definition_Access",
       qualified_name: "Gen.Model.Queries.Query_Definition_Access",
       signature: "gen.model.queries.query_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_Definition_Access is access all Query_Definition'Class;",
       }   ,
       {
       name: "Query_File_Definition_Access",
       qualified_name: "Gen.Model.Queries.Query_File_Definition_Access",
       signature: "gen.model.queries.query_file_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Query_File_Definition_Access is access all Query_File_Definition'Class;",
       }   ,
       {
       name: "Sort_Definition_Access",
       qualified_name: "Gen.Model.Queries.Sort_Definition_Access",
       signature: "gen.model.queries.sort_definition_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sort_Definition_Access is access all Sort_Definition'Class;",
       }   ,
   ]
,}
---

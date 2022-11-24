---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Config_Files",
qualified_name: "SAL.Config_Files",
signature: "sal.config_files",
enclosing: "sal",
is_private: false,
documentation: "Almost any package that does file IO will not be preelaborable.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Configuration_Type",
       qualified_name: "SAL.Config_Files.Configuration_Type",
       signature: "sal.config_files.configuration_type",
       enclosing: "",
       is_private: false,
       documentation: "Limited because it probably contains a file object.",
       documentation_snippet: "type Configuration_Type is limited private;",
       }   ,
       {
       name: "Duplicate_Key_Type",
       qualified_name: "SAL.Config_Files.Duplicate_Key_Type",
       signature: "sal.config_files.duplicate_key_type",
       enclosing: "",
       is_private: false,
       documentation: "See design comments above.\n\n@enum Raise_Exception\n@enum Keep_First\n@enum Keep_Last",
       documentation_snippet: "type Duplicate_Key_Type is (Raise_Exception, Keep_First, Keep_Last);",
       }   ,
       {
       name: "Iterator_Type",
       qualified_name: "SAL.Config_Files.Iterator_Type",
       signature: "sal.config_files.iterator_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator_Type is private;",
       }   ,
       {
       name: "Missing_Key_Type",
       qualified_name: "SAL.Config_Files.Missing_Key_Type",
       signature: "sal.config_files.missing_key_type",
       enclosing: "",
       is_private: false,
       documentation: "See design comments above.\n\n@enum Raise_Exception\n@enum Ignore",
       documentation_snippet: "type Missing_Key_Type is (Raise_Exception, Ignore);",
       }   ,
   ]
,access_types:    [
       {
       name: "Configuration_Access_Type",
       qualified_name: "SAL.Config_Files.Configuration_Access_Type",
       signature: "sal.config_files.configuration_access_type",
       enclosing: "",
       is_private: false,
       documentation: "For including a Configuration_Type component in a non-limited\ntype.",
       documentation_snippet: "type Configuration_Access_Type is access all Configuration_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Iterator",
       qualified_name: "SAL.Config_Files.Null_Iterator",
       signature: "sal.config_files.null_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Iterator : constant Iterator_Type;",
       }   ,
   ]
,}
---

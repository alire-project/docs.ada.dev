---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Client.Files",
qualified_name: "Gnoga.Client.Files",
signature: "gnoga.client.files",
enclosing: "gnoga.client",
is_private: false,
documentation: "Files API is inspired by https://developer.mozilla.org/en-US/docs/Web/API/FileReader.\nSome comments come from FileReader documentation.",
documentation_snippet: "",
simple_types:    [
       {
       name: "State_Type",
       qualified_name: "Gnoga.Client.Files.State_Type",
       signature: "gnoga.client.files.state_type",
       enclosing: "",
       is_private: false,
       documentation: "  EMPTY    No data has been loaded yet.\n  LOADING  Data is currently being loaded.\n  DONE     The entire read request has been completed.\n-----------------------------------------------------------------------\n  File_Reader_Type - Creation Methods\n-----------------------------------------------------------------------\n\n@enum Empty\n@enum Loading\n@enum Done",
       documentation_snippet: "type State_Type is (Empty, Loading, Done);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "File_Reader_Type",
       qualified_name: "Gnoga.Client.Files.File_Reader_Type",
       signature: "gnoga.client.files.file_reader_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Reader_Type is new Gnoga.Gui.Base.Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "File_Reader_Access",
       qualified_name: "Gnoga.Client.Files.File_Reader_Access",
       signature: "gnoga.client.files.file_reader_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Reader_Access is access all File_Reader_Type;",
       }   ,
       {
       name: "File_Reader_Event",
       qualified_name: "Gnoga.Client.Files.File_Reader_Event",
       signature: "gnoga.client.files.file_reader_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Reader_Event is access procedure\n  (Object : in out Gnoga.Gui.Base.Base_Type'Class;\n   Event  : in     String);",
       }   ,
       {
       name: "Pointer_To_File_Reader_Class",
       qualified_name: "Gnoga.Client.Files.Pointer_To_File_Reader_Class",
       signature: "gnoga.client.files.pointer_to_file_reader_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_File_Reader_Class is access all File_Reader_Type'Class;",
       }   ,
   ]
,}
---

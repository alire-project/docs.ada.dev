---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.File_Readers",
qualified_name: "Langkit_Support.File_Readers",
signature: "langkit_support.file_readers",
enclosing: "langkit_support",
is_private: false,
documentation: "This packages provides an interface to abstract away the action of reading\na source file to parse. Depending on use cases, it allows to override\nbytes-to-text decoding and preprocess sources (before actual\nlexing/parsing).",
documentation_snippet: "",
record_types:    [
       {
       name: "Decoded_File_Contents",
       qualified_name: "Langkit_Support.File_Readers.Decoded_File_Contents",
       signature: "langkit_support.file_readers.decoded_file_contents",
       enclosing: "",
       is_private: false,
       documentation: "The \"Buffer (First .. Last)\" slice contains the decoded file contents as\na sequence of codepoints. We keep track of First/Last indexes in\naddition to Ada's Buffer'First/'Last attributes because source buffers\nmay be oversized.\n\n@field Buffer\n@field First\n@field Last",
       documentation_snippet: "type Decoded_File_Contents is record\n   Buffer : Text_Access;\n   First  : Positive;\n   Last   : Natural;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "File_Reader_Interface",
       qualified_name: "Langkit_Support.File_Readers.File_Reader_Interface",
       signature: "langkit_support.file_readers.file_reader_interface",
       enclosing: "",
       is_private: false,
       documentation: "Interface to override how source files are fetched and decoded",
       documentation_snippet: "type File_Reader_Interface is interface;",
       }   ,
   ]
,subtypes:    [
       {
       name: "File_Reader_Reference",
       qualified_name: "Langkit_Support.File_Readers.File_Reader_Reference",
       signature: "langkit_support.file_readers.file_reader_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype File_Reader_Reference is File_Reader_References.Ref;",
       }   ,
   ]
,variables:    [
       {
       name: "No_File_Reader_Reference",
       qualified_name: "Langkit_Support.File_Readers.No_File_Reader_Reference",
       signature: "langkit_support.file_readers.no_file_reader_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_File_Reader_Reference : File_Reader_Reference renames\n   File_Reader_References.Null_Ref;",
       }   ,
   ]
,}
---

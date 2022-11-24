---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Filesystem.FAT",
qualified_name: "Filesystem.FAT",
signature: "filesystem.fat",
enclosing: "filesystem",
is_private: false,
documentation: "This packages provide a low level driver for the FAT file system\narchitecture. It is recommended to _not_ use this interface directly but to\naccess the file system using the File_IO package. For more info, see the\nfile system chapter of the documentation.",
documentation_snippet: "",
simple_types:    [
       {
       name: "FAT_Name",
       qualified_name: "Filesystem.FAT.FAT_Name",
       signature: "filesystem.fat.fat_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FAT_Name is private;",
       }   ,
       {
       name: "FAT_Version",
       qualified_name: "Filesystem.FAT.FAT_Version",
       signature: "filesystem.fat.fat_version",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FAT_Version is\n  (FAT16,\n   FAT32);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "FAT_Filesystem",
       qualified_name: "Filesystem.FAT.FAT_Filesystem",
       signature: "filesystem.fat.fat_filesystem",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FAT_Filesystem is limited new Filesystem_Driver with private;",
       }   ,
       {
       name: "FAT_Node",
       qualified_name: "Filesystem.FAT.FAT_Node",
       signature: "filesystem.fat.fat_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FAT_Node is new Node_Handle with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "FAT_Filesystem_Access",
       qualified_name: "Filesystem.FAT.FAT_Filesystem_Access",
       signature: "filesystem.fat.fat_filesystem_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FAT_Filesystem_Access is access all FAT_Filesystem;",
       }   ,
   ]
,constants:    [
       {
       name: "MAX_DIR_HANDLES",
       qualified_name: "Filesystem.FAT.MAX_DIR_HANDLES",
       signature: "filesystem.fat.max_dir_handles",
       enclosing: "",
       is_private: false,
       documentation: "Maximum number of handles opened simultaneously.",
       documentation_snippet: "MAX_DIR_HANDLES     : constant := 10;",
       }   ,
       {
       name: "MAX_FILE_HANDLES",
       qualified_name: "Filesystem.FAT.MAX_FILE_HANDLES",
       signature: "filesystem.fat.max_file_handles",
       enclosing: "",
       is_private: false,
       documentation: "Maximum number of handles opened simultaneously.",
       documentation_snippet: "MAX_FILE_HANDLES    : constant := 10;",
       }   ,
       {
       name: "MAX_FILENAME_LENGTH",
       qualified_name: "Filesystem.FAT.MAX_FILENAME_LENGTH",
       signature: "filesystem.fat.max_filename_length",
       enclosing: "",
       is_private: false,
       documentation: "Maximum size of a file or directory name",
       documentation_snippet: "MAX_FILENAME_LENGTH : constant := 255;",
       }   ,
       {
       name: "MAX_VOLUMES",
       qualified_name: "Filesystem.FAT.MAX_VOLUMES",
       signature: "filesystem.fat.max_volumes",
       enclosing: "",
       is_private: false,
       documentation: "Maximum number of mounted volumes",
       documentation_snippet: "MAX_VOLUMES         : constant := 1;",
       }   ,
   ]
,}
---

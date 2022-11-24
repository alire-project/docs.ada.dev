---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "File_IO",
qualified_name: "File_IO",
signature: "file_io",
enclosing: "",
is_private: false,
documentation: "This package provides a user friendly interface to the file system. For\nmore info, see the file system chapter of the documentation.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Directory_Descriptor",
       qualified_name: "File_IO.Directory_Descriptor",
       signature: "file_io.directory_descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Directory_Descriptor is limited private;",
       }   ,
       {
       name: "File_Descriptor",
       qualified_name: "File_IO.File_Descriptor",
       signature: "file_io.file_descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Descriptor is limited private;",
       }   ,
       {
       name: "File_Mode",
       qualified_name: "File_IO.File_Mode",
       signature: "file_io.file_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Mode is (Read_Only, Write_Only, Read_Write);",
       }   ,
       {
       name: "File_Size",
       qualified_name: "File_IO.File_Size",
       signature: "file_io.file_size",
       enclosing: "",
       is_private: false,
       documentation: "Modern fs all support 64-bit file size. Only old or limited ones support\nmax 32-bit (FAT in particular). So let's see big and not limit ourselves\nin this API with 32-bit only.",
       documentation_snippet: "type File_Size is new HAL.UInt64;",
       }   ,
       {
       name: "Seek_Mode",
       qualified_name: "File_IO.Seek_Mode",
       signature: "file_io.seek_mode",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum From_Start\n  Seek from the end of the file, backward\n@enum From_End\n  Seek from the current position, forward\n@enum Forward\n  Seek from the current position, backward\n@enum Backward",
       documentation_snippet: "type Seek_Mode is\n  (\n   From_Start,\n   From_End,\n   Forward,\n   Backward);",
       }   ,
       {
       name: "Status_Code",
       qualified_name: "File_IO.Status_Code",
       signature: "file_io.status_code",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum OK\n@enum Non_Empty_Directory\n@enum Disk_Error\n  A hardware error occurred in the low level disk I/O\n@enum Disk_Full\n@enum Internal_Error\n@enum Drive_Not_Ready\n@enum No_Such_File\n@enum No_Such_Path\n@enum Not_Mounted\n  The mount point is invalid\n@enum Invalid_Name\n@enum Access_Denied\n@enum Already_Exists\n@enum Invalid_Object_Entry\n@enum Write_Protected\n@enum Invalid_Drive\n@enum No_Filesystem\n  The volume is not a FAT volume\n@enum Locked\n@enum Too_Many_Open_Files\n  All available handles are used\n@enum Invalid_Parameter\n@enum Input_Output_Error\n@enum No_MBR_Found\n@enum No_Partition_Found\n@enum No_More_Entries\n@enum Read_Only_File_System\n@enum Operation_Not_Permitted",
       documentation_snippet: "type Status_Code is\n  (OK,\n   Non_Empty_Directory,\n   Disk_Error,\n   Disk_Full,\n   Internal_Error,\n   Drive_Not_Ready,\n   No_Such_File,\n   No_Such_Path,\n   Not_Mounted,\n   Invalid_Name,\n   Access_Denied,\n   Already_Exists,\n   Invalid_Object_Entry,\n   Write_Protected,\n   Invalid_Drive,\n   No_Filesystem,\n   Locked,\n   Too_Many_Open_Files,\n   Invalid_Parameter,\n   Input_Output_Error,\n   No_MBR_Found,\n   No_Partition_Found,\n   No_More_Entries,\n   Read_Only_File_System,\n   Operation_Not_Permitted);",
       }   ,
   ]
,record_types:    [
       {
       name: "Directory_Entry",
       qualified_name: "File_IO.Directory_Entry",
       signature: "file_io.directory_entry",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Directory_Entry (Name_Length : Natural) is record\n   Name         : String (1 .. Name_Length);\n   Subdirectory : Boolean;\n   Read_Only    : Boolean;\n   Hidden       : Boolean;\n   Symlink      : Boolean;\n   Size         : File_Size;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Mount_Path",
       qualified_name: "File_IO.Mount_Path",
       signature: "file_io.mount_path",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mount_Path is String\n  with Dynamic_Predicate => Mount_Path'Length <= Max_Mount_Name_Length;",
       }   ,
   ]
,constants:    [
       {
       name: "Invalid_Dir_Entry",
       qualified_name: "File_IO.Invalid_Dir_Entry",
       signature: "file_io.invalid_dir_entry",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Dir_Entry : constant Directory_Entry;",
       }   ,
       {
       name: "Max_Mount_Name_Length",
       qualified_name: "File_IO.Max_Mount_Name_Length",
       signature: "file_io.max_mount_name_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Mount_Name_Length : constant := ADL_Config.Max_Mount_Name_Length;",
       }   ,
       {
       name: "Max_Mount_Points",
       qualified_name: "File_IO.Max_Mount_Points",
       signature: "file_io.max_mount_points",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Mount_Points : constant := ADL_Config.Max_Mount_Points;",
       }   ,
   ]
,}
---

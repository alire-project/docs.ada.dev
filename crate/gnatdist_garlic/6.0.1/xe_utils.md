---
crate: gnatdist_garlic
layout: gnatdoc
gnatdoc: {
name: "XE_Utils",
qualified_name: "XE_Utils",
signature: "xe_utils",
enclosing: "",
is_private: false,
documentation: "--------------------\n Global Variables --\n--------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Exit_Code_Type",
       qualified_name: "XE_Utils.Exit_Code_Type",
       signature: "xe_utils.exit_code_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum E_Success\n  No warnings or errors\n@enum E_Fatal\n  Fatal (serious) error",
       documentation_snippet: "type Exit_Code_Type is\n  (E_Success,\n   E_Fatal);",
       }   ,
   ]
,array_types:    [
       {
       name: "File_Name_List",
       qualified_name: "XE_Utils.File_Name_List",
       signature: "xe_utils.file_name_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Name_List is array (Natural range <>) of File_Name_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "ADB_Suffix",
       qualified_name: "XE_Utils.ADB_Suffix",
       signature: "xe_utils.adb_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADB_Suffix    : constant String := \".adb\";",
       }   ,
       {
       name: "ADS_Suffix",
       qualified_name: "XE_Utils.ADS_Suffix",
       signature: "xe_utils.ads_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADS_Suffix    : constant String := \".ads\";",
       }   ,
       {
       name: "ALI_Suffix",
       qualified_name: "XE_Utils.ALI_Suffix",
       signature: "xe_utils.ali_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ALI_Suffix    : constant String := \".ali\";",
       }   ,
       {
       name: "Cfg_Suffix",
       qualified_name: "XE_Utils.Cfg_Suffix",
       signature: "xe_utils.cfg_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Cfg_Suffix    : constant String := \".cfg\";",
       }   ,
       {
       name: "Exe_Suffix",
       qualified_name: "XE_Utils.Exe_Suffix",
       signature: "xe_utils.exe_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Exe_Suffix    : constant String := Get_Executable_Suffix.all;",
       }   ,
       {
       name: "No_Args",
       qualified_name: "XE_Utils.No_Args",
       signature: "xe_utils.no_args",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Args : constant Argument_List (1 .. 0) := (others => null);",
       }   ,
       {
       name: "Obj_Suffix",
       qualified_name: "XE_Utils.Obj_Suffix",
       signature: "xe_utils.obj_suffix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Obj_Suffix    : constant String := Get_Object_Suffix.all;",
       }   ,
       {
       name: "Root",
       qualified_name: "XE_Utils.Root",
       signature: "xe_utils.root",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Root          : constant String := \"dsa\";",
       }   ,
   ]
,variables:    [
       {
       name: "ADB_Suffix_Id",
       qualified_name: "XE_Utils.ADB_Suffix_Id",
       signature: "xe_utils.adb_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADB_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "ADS_Suffix_Id",
       qualified_name: "XE_Utils.ADS_Suffix_Id",
       signature: "xe_utils.ads_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADS_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "ALI_Suffix_Id",
       qualified_name: "XE_Utils.ALI_Suffix_Id",
       signature: "xe_utils.ali_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ALI_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "Cfg_Suffix_Id",
       qualified_name: "XE_Utils.Cfg_Suffix_Id",
       signature: "xe_utils.cfg_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Cfg_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "E_Current_Dir",
       qualified_name: "XE_Utils.E_Current_Dir",
       signature: "xe_utils.e_current_dir",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "E_Current_Dir : String_Access;",
       }   ,
       {
       name: "Exe_Suffix_Id",
       qualified_name: "XE_Utils.Exe_Suffix_Id",
       signature: "xe_utils.exe_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Exe_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "I_Current_Dir",
       qualified_name: "XE_Utils.I_Current_Dir",
       signature: "xe_utils.i_current_dir",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "I_Current_Dir : String_Access;",
       }   ,
       {
       name: "I_Stub_Dir",
       qualified_name: "XE_Utils.I_Stub_Dir",
       signature: "xe_utils.i_stub_dir",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "I_Stub_Dir    : String_Access;",
       }   ,
       {
       name: "Obj_Suffix_Id",
       qualified_name: "XE_Utils.Obj_Suffix_Id",
       signature: "xe_utils.obj_suffix_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Obj_Suffix_Id : File_Name_Type;",
       }   ,
       {
       name: "Part_Main_ALI_Name",
       qualified_name: "XE_Utils.Part_Main_ALI_Name",
       signature: "xe_utils.part_main_ali_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Part_Main_ALI_Name : File_Name_Type;",
       }   ,
       {
       name: "Part_Main_Obj_Name",
       qualified_name: "XE_Utils.Part_Main_Obj_Name",
       signature: "xe_utils.part_main_obj_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Part_Main_Obj_Name : File_Name_Type;",
       }   ,
       {
       name: "Part_Main_Src_Name",
       qualified_name: "XE_Utils.Part_Main_Src_Name",
       signature: "xe_utils.part_main_src_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Part_Main_Src_Name : File_Name_Type;",
       }   ,
       {
       name: "Part_Prj_File_Name",
       qualified_name: "XE_Utils.Part_Prj_File_Name",
       signature: "xe_utils.part_prj_file_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Part_Prj_File_Name : File_Name_Type;",
       }   ,
       {
       name: "PWD_Id",
       qualified_name: "XE_Utils.PWD_Id",
       signature: "xe_utils.pwd_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PWD_Id        : File_Name_Type;",
       }   ,
       {
       name: "Stub_Dir",
       qualified_name: "XE_Utils.Stub_Dir",
       signature: "xe_utils.stub_dir",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Stub_Dir      : String_Access;",
       }   ,
       {
       name: "Stub_Dir_Name",
       qualified_name: "XE_Utils.Stub_Dir_Name",
       signature: "xe_utils.stub_dir_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Stub_Dir_Name : File_Name_Type;",
       }   ,
   ]
,}
---

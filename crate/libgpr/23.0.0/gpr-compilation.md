---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Compilation",
qualified_name: "GPR.Compilation",
signature: "gpr.compilation",
enclosing: "gpr",
is_private: false,
documentation: "This is the root package for the compilation support. It handles the local\nand distributed compilation modes.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Process_Kind",
       qualified_name: "GPR.Compilation.Process_Kind",
       signature: "gpr.compilation.process_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process_Kind is (Local, Remote);",
       }   ,
       {
       name: "Remote_Id",
       qualified_name: "GPR.Compilation.Remote_Id",
       signature: "gpr.compilation.remote_id",
       enclosing: "",
       is_private: false,
       documentation: "Represent a remote process id, this number is unique across all slaves.\nSuch number if created by the slaves using a slave id (unique number)\nand a compilation number. Bother numbers are 32bits value:\n\n   63                 32  31                     0\n    |    [slave id]      |  [compilation number] |",
       documentation_snippet: "type Remote_Id is mod 2 ** 64;",
       }   ,
   ]
,record_types:    [
       {
       name: "File_Data",
       qualified_name: "GPR.Compilation.File_Data",
       signature: "gpr.compilation.file_data",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Path_Name\n@field Timestamp\n  YYYYMMDDhhmmss\n@field Is_Executable",
       documentation_snippet: "type File_Data is record\n   Path_Name     : Ada.Strings.Unbounded.Unbounded_String;\n   Timestamp     : Time_Stamp_Type;\n   Is_Executable : Boolean;\nend record;",
       }   ,
       {
       name: "Id",
       qualified_name: "GPR.Compilation.Id",
       signature: "gpr.compilation.id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Id (Kind : Process_Kind := Local) is record\n   case Kind is\n      when Local  => Pid   : GNAT.OS_Lib.Process_Id;\n      when Remote => R_Pid : Remote_Id;\n   end case;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Shared_Counter_Access",
       qualified_name: "GPR.Compilation.Shared_Counter_Access",
       signature: "gpr.compilation.shared_counter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Shared_Counter_Access is access Shared_Counter;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Port",
       qualified_name: "GPR.Compilation.Default_Port",
       signature: "gpr.compilation.default_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Port : constant := 8484;",
       }   ,
       {
       name: "Invalid_Process",
       qualified_name: "GPR.Compilation.Invalid_Process",
       signature: "gpr.compilation.invalid_process",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Process : constant Id := (Local, Pid => GNAT.OS_Lib.Invalid_Pid);",
       }   ,
       {
       name: "Opts_Sep",
       qualified_name: "GPR.Compilation.Opts_Sep",
       signature: "gpr.compilation.opts_sep",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Opts_Sep : constant Character := Ada.Characters.Latin_1.HT;",
       }   ,
   ]
,}
---

---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Makeutl",
qualified_name: "Makeutl",
signature: "makeutl",
enclosing: "",
is_private: false,
documentation: "This package contains various subprograms used by the builders, in\nparticular those subprograms related to project management and build\nqueue management.",
documentation_snippet: "",
packages:    [
       {
       name: "Mains",
       qualified_name: "Makeutl.Mains",
       signature: "makeutl.mains",
       enclosing: "makeutl",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
       {
       name: "Queue",
       qualified_name: "Makeutl.Queue",
       signature: "makeutl.queue",
       enclosing: "makeutl",
       is_private: false,
       documentation: "The queue of sources to be checked for compilation. There can be a\nsingle such queue per application.",
       documentation_snippet: "",
record_types:           [
              {
              name: "Source_Info",
              qualified_name: "Makeutl.Queue.Source_Info",
              signature: "makeutl.queue.source_info",
              enclosing: "",
              is_private: false,
              documentation: "Information about files stored in the queue. The exact information\ndepends on the builder, and in particular whether it only supports\nproject-based files (in which case we have a full Source_Id record).\n\n@field Format\n@field Tree\n@field Id\n@field Closure\n@field File\n@field Unit\n@field Index\n@field Project\n@field Sid",
              documentation_snippet: "type Source_Info (Format : Source_Info_Format := Format_Gprbuild) is\n   record\n      case Format is\n         when Format_Gprbuild =>\n            Tree    : Project_Tree_Ref := No_Project_Tree;\n            Id      : Source_Id        := No_Source;\n            Closure : Boolean          := False;\n         when Format_Gnatmake =>\n            File    : File_Name_Type := No_File;\n            Unit    : Unit_Name_Type := No_Unit_Name;\n            Index   : Int            := 0;\n            Project : Project_Id     := No_Project;\n            Sid     : Source_Id      := No_Source;\n      end case;\n   end record;",
              }          ,
          ]
,constants:           [
              {
              name: "No_Source_Info",
              qualified_name: "Makeutl.Queue.No_Source_Info",
              signature: "makeutl.queue.no_source_info",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "No_Source_Info : constant Source_Info :=\n                   (Format_Gprbuild, null, null, False);",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Activity_Type",
       qualified_name: "Makeutl.Activity_Type",
       signature: "makeutl.activity_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Activity_Type is (Compilation, Executable_Binding, SAL_Binding);",
       }   ,
       {
       name: "Source_Info_Format",
       qualified_name: "Makeutl.Source_Info_Format",
       signature: "makeutl.source_info_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Info_Format is (Format_Gprbuild, Format_Gnatmake);",
       }   ,
   ]
,array_types:    [
       {
       name: "Name_Ids",
       qualified_name: "Makeutl.Name_Ids",
       signature: "makeutl.name_ids",
       enclosing: "",
       is_private: false,
       documentation: "Name_Ids is used for list of language names in procedure Get_Directories\nbelow.",
       documentation_snippet: "type Name_Ids is array (Positive range <>) of Name_Id;",
       }   ,
   ]
,record_types:    [
       {
       name: "Binding_Data_Record",
       qualified_name: "Makeutl.Binding_Data_Record",
       signature: "makeutl.binding_data_record",
       enclosing: "",
       is_private: false,
       documentation: "Data for a language that have a binder driver\n\n@field Language\n@field Language_Name\n@field Binder_Driver_Name\n@field Binder_Driver_Path\n@field Binder_Prefix\n@field Next",
       documentation_snippet: "type Binding_Data_Record is record\n   Language           : Language_Ptr;\n   Language_Name      : Name_Id;\n   Binder_Driver_Name : File_Name_Type;\n   Binder_Driver_Path : String_Access;\n   Binder_Prefix      : Name_Id;\n   Next               : Binding_Data;\nend record;",
       }   ,
       {
       name: "Main_Info",
       qualified_name: "Makeutl.Main_Info",
       signature: "makeutl.main_info",
       enclosing: "",
       is_private: false,
       documentation: "\n@field File\n  Always canonical casing\n@field Index\n@field Location\n@field Source\n@field Project\n@field Tree",
       documentation_snippet: "type Main_Info is record\n   File      : File_Name_Type;\n   Index     : Int := 0;\n   Location  : Source_Ptr := No_Location;\n   Source    : Prj.Source_Id := No_Source;\n   Project   : Project_Id;\n   Tree      : Project_Tree_Ref;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Builder_Project_Tree_Data",
       qualified_name: "Makeutl.Builder_Project_Tree_Data",
       signature: "makeutl.builder_project_tree_data",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Binding\n@field There_Are_Binder_Drivers\n  True when there is a binder driver. Set by Get_Configuration when\n  an attribute Language_Processing'Binder_Driver is declared.\n  Reset to False if there are no sources of the languages with binder\n  drivers.\n@field Number_Of_Mains\n  Number of main units in this project tree\n@field Closure_Needed\n  If True, we need to add the closure of the file we just compiled to\n  the queue. If False, it is assumed that all files are already on the\n  queue so we do not waste time computing the closure.\n@field Need_Compilation\n@field Need_Binding\n@field Need_Linking",
       documentation_snippet: "type Builder_Project_Tree_Data is new Project_Tree_Appdata with record\n   Binding : Binding_Data;\n   There_Are_Binder_Drivers : Boolean := False;\n   Number_Of_Mains : Natural := 0;\n   Closure_Needed : Boolean := False;\n   Need_Compilation : Boolean := True;\n   Need_Binding     : Boolean := True;\n   Need_Linking     : Boolean := True;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Binding_Data",
       qualified_name: "Makeutl.Binding_Data",
       signature: "makeutl.binding_data",
       enclosing: "",
       is_private: false,
       documentation: "Data for a language that have a binder driver",
       documentation_snippet: "type Binding_Data is access Binding_Data_Record;",
       }   ,
       {
       name: "Builder_Data_Access",
       qualified_name: "Makeutl.Builder_Data_Access",
       signature: "makeutl.builder_data_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Builder_Data_Access is access all Builder_Project_Tree_Data;",
       }   ,
       {
       name: "Fail_Proc",
       qualified_name: "Makeutl.Fail_Proc",
       signature: "makeutl.fail_proc",
       enclosing: "",
       is_private: false,
       documentation: "Pointer to procedure which outputs a failure message\n\n@param S",
       documentation_snippet: "type Fail_Proc is access procedure (S : String);",
       }   ,
   ]
,constants:    [
       {
       name: "Ada_Only",
       qualified_name: "Makeutl.Ada_Only",
       signature: "makeutl.ada_only",
       enclosing: "",
       is_private: false,
       documentation: "Used to invoke Get_Directories in gnatmake",
       documentation_snippet: "Ada_Only : constant Name_Ids := (1 => Name_Ada);",
       }   ,
       {
       name: "Create_Map_File_Switch",
       qualified_name: "Makeutl.Create_Map_File_Switch",
       signature: "makeutl.create_map_file_switch",
       enclosing: "",
       is_private: false,
       documentation: "Switch to create a map file when an executable is linked",
       documentation_snippet: "Create_Map_File_Switch : constant String := \"--create-map-file\";",
       }   ,
       {
       name: "Default_Config_Name",
       qualified_name: "Makeutl.Default_Config_Name",
       signature: "makeutl.default_config_name",
       enclosing: "",
       is_private: false,
       documentation: "Name of the configuration file used by gprbuild and generated by\ngprconfig by default.",
       documentation_snippet: "Default_Config_Name : constant String := \"default.cgpr\";",
       }   ,
       {
       name: "Keep_Temp_Files_Option",
       qualified_name: "Makeutl.Keep_Temp_Files_Option",
       signature: "makeutl.keep_temp_files_option",
       enclosing: "",
       is_private: false,
       documentation: "Switch to suppress deletion of temp files created by the builder.\nNote that debug switch -gnatdn also has this effect.",
       documentation_snippet: "Keep_Temp_Files_Option : constant String := \"--keep-temp-files\";",
       }   ,
       {
       name: "No_Exit_Message_Option",
       qualified_name: "Makeutl.No_Exit_Message_Option",
       signature: "makeutl.no_exit_message_option",
       enclosing: "",
       is_private: false,
       documentation: "Switch to suppress exit error message when there are compilation\nfailures. This is useful when a tool, such as gnatprove, silently calls\nthe builder and does not want to pollute its output with error messages\ncoming from the builder. This is an internal switch.",
       documentation_snippet: "No_Exit_Message_Option : constant String := \"--no-exit-message\";",
       }   ,
       {
       name: "No_Main_Info",
       qualified_name: "Makeutl.No_Main_Info",
       signature: "makeutl.no_main_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Main_Info : constant Main_Info :=\n                 (No_File, 0, No_Location, No_Source, No_Project, null);",
       }   ,
       {
       name: "No_Names",
       qualified_name: "Makeutl.No_Names",
       signature: "makeutl.no_names",
       enclosing: "",
       is_private: false,
       documentation: "Name_Ids is used for list of language names in procedure Get_Directories\nbelow.",
       documentation_snippet: "No_Names : constant Name_Ids := (1 .. 0 => No_Name);",
       }   ,
       {
       name: "On_Windows",
       qualified_name: "Makeutl.On_Windows",
       signature: "makeutl.on_windows",
       enclosing: "",
       is_private: false,
       documentation: "True when on Windows",
       documentation_snippet: "On_Windows : constant Boolean := Directory_Separator = '\\';",
       }   ,
       {
       name: "Single_Compile_Per_Obj_Dir_Switch",
       qualified_name: "Makeutl.Single_Compile_Per_Obj_Dir_Switch",
       signature: "makeutl.single_compile_per_obj_dir_switch",
       enclosing: "",
       is_private: false,
       documentation: "Switch to forbid simultaneous compilations for the same object directory\nwhen project files are used.",
       documentation_snippet: "Single_Compile_Per_Obj_Dir_Switch : constant String :=\n                                      \"--single-compile-per-obj-dir\";",
       }   ,
       {
       name: "Source_Info_Option",
       qualified_name: "Makeutl.Source_Info_Option",
       signature: "makeutl.source_info_option",
       enclosing: "",
       is_private: false,
       documentation: "Switch to indicate the source info file",
       documentation_snippet: "Source_Info_Option : constant String := \"--source-info=\";",
       }   ,
       {
       name: "Subdirs_Option",
       qualified_name: "Makeutl.Subdirs_Option",
       signature: "makeutl.subdirs_option",
       enclosing: "",
       is_private: false,
       documentation: "Switch used to indicate that the real directories (object, exec,\nlibrary, ...) are subdirectories of those in the project file.",
       documentation_snippet: "Subdirs_Option : constant String := \"--subdirs=\";",
       }   ,
       {
       name: "Unchecked_Shared_Lib_Imports",
       qualified_name: "Makeutl.Unchecked_Shared_Lib_Imports",
       signature: "makeutl.unchecked_shared_lib_imports",
       enclosing: "",
       is_private: false,
       documentation: "Command line switch to allow shared library projects to import projects\nthat are not shared library projects.",
       documentation_snippet: "Unchecked_Shared_Lib_Imports : constant String :=\n                                 \"--unchecked-shared-lib-imports\";",
       }   ,
   ]
,variables:    [
       {
       name: "Load_Standard_Base",
       qualified_name: "Makeutl.Load_Standard_Base",
       signature: "makeutl.load_standard_base",
       enclosing: "",
       is_private: false,
       documentation: "False when gprbuild is called with --db-",
       documentation_snippet: "Load_Standard_Base : Boolean := True;",
       }   ,
       {
       name: "Root_Environment",
       qualified_name: "Makeutl.Root_Environment",
       signature: "makeutl.root_environment",
       enclosing: "",
       is_private: false,
       documentation: "The environment coming from environment variables and command line\nswitches. When we do not have an aggregate project, this is used for\nparsing the project tree. When we have an aggregate project, this is\nused to parse the aggregate project; the latter then generates another\nenvironment (with additional external values and project path) to parse\nthe aggregated projects.",
       documentation_snippet: "Root_Environment : Prj.Tree.Environment;",
       }   ,
   ]
,}
---
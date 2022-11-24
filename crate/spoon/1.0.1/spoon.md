---
crate: spoon
layout: gnatdoc
gnatdoc: {
name: "Spoon",
qualified_name: "Spoon",
signature: "spoon",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2022 onox <denkpadje@gmail.com>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Argument",
       qualified_name: "Spoon.Argument",
       signature: "spoon.argument",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Argument (<>) is limited private;",
       }   ,
       {
       name: "Exit_State",
       qualified_name: "Spoon.Exit_State",
       signature: "spoon.exit_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exit_State is (Error, Exited, Crashed, Terminated);",
       }   ,
       {
       name: "Exit_Status",
       qualified_name: "Spoon.Exit_Status",
       signature: "spoon.exit_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Exit_Status is new Integer;",
       }   ,
       {
       name: "Group_ID",
       qualified_name: "Spoon.Group_ID",
       signature: "spoon.group_id",
       enclosing: "",
       is_private: false,
       documentation: "2 or higher (see man killpg(3))",
       documentation_snippet: "type Group_ID   is range 2 .. Positive'Last;",
       }   ,
       {
       name: "IDs_Kind",
       qualified_name: "Spoon.IDs_Kind",
       signature: "spoon.ids_kind",
       enclosing: "",
       is_private: false,
       documentation: "Real will drop effective IDs if parent is a setuid binary\n\n@enum Inherit\n@enum Real",
       documentation_snippet: "type IDs_Kind is (Inherit, Real);",
       }   ,
       {
       name: "Output_Kind",
       qualified_name: "Spoon.Output_Kind",
       signature: "spoon.output_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Output_Kind is (Standard_Output, Standard_Error);",
       }   ,
       {
       name: "Process_Group_Kind",
       qualified_name: "Spoon.Process_Group_Kind",
       signature: "spoon.process_group_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process_Group_Kind is (Inherit, Same_As_PID, Custom);",
       }   ,
       {
       name: "Process_ID",
       qualified_name: "Spoon.Process_ID",
       signature: "spoon.process_id",
       enclosing: "",
       is_private: false,
       documentation: "2 or higher (see man killpg(3))",
       documentation_snippet: "type Process_ID is range 1 .. Positive'Last;",
       }   ,
       {
       name: "Program_Kind",
       qualified_name: "Spoon.Program_Kind",
       signature: "spoon.program_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Program_Kind is (File_Path, Name);",
       }   ,
   ]
,array_types:    [
       {
       name: "Argument_Array",
       qualified_name: "Spoon.Argument_Array",
       signature: "spoon.argument_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Argument_Array is array (Positive range <>) of not null Argument_Access;",
       }   ,
   ]
,record_types:    [
       {
       name: "Attributes",
       qualified_name: "Spoon.Attributes",
       signature: "spoon.attributes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes\n  (IDs   : IDs_Kind;\n   Group : Process_Group_Kind) is\nrecord\n   case Group is\n      when Custom => Group_ID : Spoon.Group_ID;\n      when others => null;\n   end case;\nend record;",
       }   ,
       {
       name: "Result",
       qualified_name: "Spoon.Result",
       signature: "spoon.result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Result (State : Exit_State) is record\n   case State is\n      when Error =>\n         Error_Code : Integer;\n      when Exited =>\n         Exit_Status : Spoon.Exit_Status;\n      when Crashed | Terminated =>\n         Signal : Positive;\n   end case;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Output_Capturer",
       qualified_name: "Spoon.Output_Capturer",
       signature: "spoon.output_capturer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Output_Capturer is protected interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Process",
       qualified_name: "Spoon.Process",
       signature: "spoon.process",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process (<>) is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Argument_Access",
       qualified_name: "Spoon.Argument_Access",
       signature: "spoon.argument_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Argument_Access is access all Argument\n  with Size => Standard'Address_Size;",
       }   ,
   ]
,constants:    [
       {
       name: "Success",
       qualified_name: "Spoon.Success",
       signature: "spoon.success",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Success : constant Exit_Status;",
       }   ,
   ]
,}
---

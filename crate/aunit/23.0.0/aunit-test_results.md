---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Test_Results",
qualified_name: "AUnit.Test_Results",
signature: "aunit.test_results",
enclosing: "aunit",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                         GNAT COMPILER COMPONENTS                         --\n                                                                          --\n                    A U N I T . T E S T _ R E S U L T S                   --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                       Copyright (C) 2000-2011, AdaCore                   --\n                                                                          --\n GNAT is free software;  you can  redistribute it  and/or modify it under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  GNAT is distributed in the hope that it will be useful, but WITH- --\n OUT ANY WARRANTY;  without even the  implied warranty of MERCHANTABILITY --\n or FITNESS FOR A PARTICULAR PURPOSE.                                     --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n GNAT is maintained by AdaCore (http://www.adacore.com)                   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Test_Error",
       qualified_name: "AUnit.Test_Results.Test_Error",
       signature: "aunit.test_results.test_error",
       enclosing: "",
       is_private: false,
       documentation: "Description of unexpected exceptions\n\n@field Exception_Name\n@field Exception_Message\n@field Traceback",
       documentation_snippet: "type Test_Error is record\n   Exception_Name    : Message_String;\n   Exception_Message : Message_String;\n   Traceback         : Message_String;\nend record;",
       }   ,
       {
       name: "Test_Failure",
       qualified_name: "AUnit.Test_Results.Test_Failure",
       signature: "aunit.test_results.test_failure",
       enclosing: "",
       is_private: false,
       documentation: "Description of a test routine failure\n\n@field Message\n@field Source_Name\n@field Line",
       documentation_snippet: "type Test_Failure is record\n   Message     : Message_String;\n   Source_Name : Message_String;\n   Line        : Natural;\nend record;",
       }   ,
       {
       name: "Test_Result",
       qualified_name: "AUnit.Test_Results.Test_Result",
       signature: "aunit.test_results.test_result",
       enclosing: "",
       is_private: false,
       documentation: "Decription of a test routine result\n\n@field Test_Name\n@field Routine_Name\n@field Failure\n@field Error\n@field Elapsed",
       documentation_snippet: "type Test_Result is record\n   Test_Name    : Message_String;\n   Routine_Name : Message_String;\n   Failure      : Test_Failure_Access;\n   Error        : Test_Error_Access;\n   Elapsed      : Time := Null_Time;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Result",
       qualified_name: "AUnit.Test_Results.Result",
       signature: "aunit.test_results.result",
       enclosing: "",
       is_private: false,
       documentation: "Record result. A result object is associated with the execution of a\ntop-level test suite",
       documentation_snippet: "type Result is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Error_Access",
       qualified_name: "AUnit.Test_Results.Test_Error_Access",
       signature: "aunit.test_results.test_error_access",
       enclosing: "",
       is_private: false,
       documentation: "Description of unexpected exceptions",
       documentation_snippet: "type Test_Error_Access is access all Test_Error;",
       }   ,
       {
       name: "Test_Failure_Access",
       qualified_name: "AUnit.Test_Results.Test_Failure_Access",
       signature: "aunit.test_results.test_failure_access",
       enclosing: "",
       is_private: false,
       documentation: "Description of a test routine failure",
       documentation_snippet: "type Test_Failure_Access is access all Test_Failure;",
       }   ,
   ]
,}
---

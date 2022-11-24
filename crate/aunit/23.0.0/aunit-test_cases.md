---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Test_Cases",
qualified_name: "AUnit.Test_Cases",
signature: "aunit.test_cases",
enclosing: "aunit",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                         GNAT COMPILER COMPONENTS                         --\n                                                                          --\n                      A U N I T . T E S T _ C A S E S                     --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                       Copyright (C) 2000-2011, AdaCore                   --\n                                                                          --\n GNAT is free software;  you can  redistribute it  and/or modify it under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  GNAT is distributed in the hope that it will be useful, but WITH- --\n OUT ANY WARRANTY;  without even the  implied warranty of MERCHANTABILITY --\n or FITNESS FOR A PARTICULAR PURPOSE.                                     --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n GNAT is maintained by AdaCore (http://www.adacore.com)                   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Registration",
       qualified_name: "AUnit.Test_Cases.Registration",
       signature: "aunit.test_cases.registration",
       enclosing: "aunit.test_cases",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
       {
       name: "Specific_Test_Case_Registration",
       qualified_name: "AUnit.Test_Cases.Specific_Test_Case_Registration",
       signature: "aunit.test_cases.specific_test_case_registration",
       enclosing: "aunit.test_cases",
       is_private: false,
       documentation: "Specific Test Case registration\n\n@formal Specific_Test_Case",
       documentation_snippet: "",
access_types:           [
              {
              name: "Specific_Test_Routine",
              qualified_name: "AUnit.Test_Cases.Specific_Test_Case_Registration.Specific_Test_Routine",
              signature: "aunit.test_cases.specific_test_case_registration.specific_test_routine",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Specific_Test_Routine is access procedure\n  (Test : in out Specific_Test_Case'Class);",
              }          ,
          ]
,       }   ,
   ]
,record_types:    [
       {
       name: "Routine_Spec",
       qualified_name: "AUnit.Test_Cases.Routine_Spec",
       signature: "aunit.test_cases.routine_spec",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Routine_Spec is record\n   Routine      : Test_Routine;\n   Routine_Name : Message_String;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Test_Case",
       qualified_name: "AUnit.Test_Cases.Test_Case",
       signature: "aunit.test_cases.test_case",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case is abstract new AUnit.Simple_Test_Cases.Test_Case with\n  private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Case_Access",
       qualified_name: "AUnit.Test_Cases.Test_Case_Access",
       signature: "aunit.test_cases.test_case_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Case_Access is access all Test_Case'Class;",
       }   ,
       {
       name: "Test_Routine",
       qualified_name: "AUnit.Test_Cases.Test_Routine",
       signature: "aunit.test_cases.test_routine",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Test_Routine is access procedure (Test : in out Test_Case'Class);",
       }   ,
   ]
,}
---

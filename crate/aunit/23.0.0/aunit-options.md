---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Options",
qualified_name: "AUnit.Options",
signature: "aunit.options",
enclosing: "aunit",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                         GNAT COMPILER COMPONENTS                         --\n                                                                          --\n                         A U N I T . O P T I O N S                        --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                       Copyright (C) 2009-2013, AdaCore                   --\n                                                                          --\n GNAT is free software;  you can  redistribute it  and/or modify it under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  GNAT is distributed in the hope that it will be useful, but WITH- --\n OUT ANY WARRANTY;  without even the  implied warranty of MERCHANTABILITY --\n or FITNESS FOR A PARTICULAR PURPOSE.                                     --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n GNAT is maintained by AdaCore (http://www.adacore.com)                   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "AUnit_Options",
       qualified_name: "AUnit.Options.AUnit_Options",
       signature: "aunit.options.aunit_options",
       enclosing: "",
       is_private: false,
       documentation: "Options used to determine how a test should be run.\n\n@field Global_Timer\n@field Test_Case_Timer\n@field Report_Successes\n@field Filter",
       documentation_snippet: "type AUnit_Options is record\n   Global_Timer     : Boolean := False;\n   Test_Case_Timer  : Boolean := False;\n   Report_Successes : Boolean := True;\n   Filter           : AUnit.Test_Filters.Test_Filter_Access := null;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Options",
       qualified_name: "AUnit.Options.Default_Options",
       signature: "aunit.options.default_options",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Options : constant AUnit_Options :=\n  (Global_Timer     => False,\n   Test_Case_Timer  => False,\n   Report_Successes => True,\n   Filter           => null);",
       }   ,
   ]
,}
---

---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Time_Measure",
qualified_name: "AUnit.Time_Measure",
signature: "aunit.time_measure",
enclosing: "aunit",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                         GNAT COMPILER COMPONENTS                         --\n                                                                          --\n                     A U N I T . T I M E _ M E A S U R E                  --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                    Copyright (C) 2006-2019, AdaCore                      --\n                                                                          --\n GNAT is free software;  you can  redistribute it  and/or modify it under --\n terms of the  GNU General Public License as published  by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  GNAT is distributed in the hope that it will be useful, but WITH- --\n OUT ANY WARRANTY;  without even the  implied warranty of MERCHANTABILITY --\n or FITNESS FOR A PARTICULAR PURPOSE.                                     --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n GNAT is maintained by AdaCore (http://www.adacore.com)                   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "AUnit_Duration",
       qualified_name: "AUnit.Time_Measure.AUnit_Duration",
       signature: "aunit.time_measure.aunit_duration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type AUnit_Duration is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Time",
       qualified_name: "AUnit.Time_Measure.Time",
       signature: "aunit.time_measure.time",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Time is record\n   Start : Ada.Calendar.Time;\n   Stop  : Ada.Calendar.Time;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Time",
       qualified_name: "AUnit.Time_Measure.Null_Time",
       signature: "aunit.time_measure.null_time",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Time : constant Time := (Start => Ada.Calendar.Time_Of (1901, 1, 1),\n                              Stop  => Ada.Calendar.Time_Of (1901, 1, 1));",
       }   ,
   ]
,}
---

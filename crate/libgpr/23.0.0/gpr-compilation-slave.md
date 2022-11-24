---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Compilation.Slave",
qualified_name: "GPR.Compilation.Slave",
signature: "gpr.compilation.slave",
enclosing: "gpr.compilation",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                           GPR PROJECT MANAGER                            --\n                                                                          --\n          Copyright (C) 2012-2018, Free Software Foundation, Inc.         --\n                                                                          --\n This library is free software;  you can redistribute it and/or modify it --\n under terms of the  GNU General Public License  as published by the Free --\n Software  Foundation;  either version 3,  or (at your  option) any later --\n version. This library is distributed in the hope that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE.                            --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Slave_Data",
       qualified_name: "GPR.Compilation.Slave.Slave_Data",
       signature: "gpr.compilation.slave.slave_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Slave_Data is record\n   Host : Unbounded_String;\n   Port : GNAT.Sockets.Port_Type;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Slave_Data",
       qualified_name: "GPR.Compilation.Slave.No_Slave_Data",
       signature: "gpr.compilation.slave.no_slave_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Slave_Data : constant Slave_Data :=\n                  (Port => GNAT.Sockets.Port_Type'Last, others => <>);",
       }   ,
   ]
,variables:    [
       {
       name: "Root_Dir",
       qualified_name: "GPR.Compilation.Slave.Root_Dir",
       signature: "gpr.compilation.slave.root_dir",
       enclosing: "",
       is_private: false,
       documentation: "Root directory from where the sources are to be synchronized with the\nslaves. This is by default the directory containing the main project\nfile. The value is changed with the Root_Dir attribute value of the\nproject file's Remote package.",
       documentation_snippet: "Root_Dir     : Unbounded_String;",
       }   ,
       {
       name: "Slaves_Data",
       qualified_name: "GPR.Compilation.Slave.Slaves_Data",
       signature: "gpr.compilation.slave.slaves_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Slaves_Data : Slaves_N.Vector;",
       }   ,
   ]
,}
---

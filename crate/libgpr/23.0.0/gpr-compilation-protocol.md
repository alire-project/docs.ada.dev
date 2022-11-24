---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Compilation.Protocol",
qualified_name: "GPR.Compilation.Protocol",
signature: "gpr.compilation.protocol",
enclosing: "gpr.compilation",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                           GPR PROJECT MANAGER                            --\n                                                                          --\n          Copyright (C) 2012-2020, Free Software Foundation, Inc.         --\n                                                                          --\n This library is free software;  you can redistribute it and/or modify it --\n under terms of the  GNU General Public License  as published by the Free --\n Software  Foundation;  either version 3,  or (at your  option) any later --\n version. This library is distributed in the hope that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE.                            --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Command_Kind",
       qualified_name: "GPR.Compilation.Protocol.Command_Kind",
       signature: "gpr.compilation.protocol.command_kind",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum EX\n  execute a command\n@enum AK\n  acknowledge received command (with pid)\n@enum TS\n  a file timestamp\n@enum ES\n  end of file timestamp\n@enum FL\n  a file, content being rewritten from builder/slave PATH\n@enum FR\n  a RAW file, no rewrite taking place\n@enum OK\n  compilation ok (with optional pid)\n@enum KO\n  compilation failed (with optional pid)\n@enum CX\n  master context\n@enum CU\n  clean-up request\n@enum DP\n  display output\n@enum EC\n  end of compilation\n@enum SI\n  a signal as been detected (like EC but no ACK needed)\n@enum SY\n  synchronization requested\n@enum IR\n  information requested\n@enum PG\n  PING just to know if the slave is listening",
       documentation_snippet: "type Command_Kind is\n  (EX,\n   AK,\n   TS,\n   ES,\n   FL,\n   FR,\n   OK,\n   KO,\n   CX,\n   CU,\n   DP,\n   EC,\n   SI,\n   SY,\n   IR,\n   PG);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Command",
       qualified_name: "GPR.Compilation.Protocol.Command",
       signature: "gpr.compilation.protocol.command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command is tagged private;",
       }   ,
       {
       name: "Communication_Channel",
       qualified_name: "GPR.Compilation.Protocol.Communication_Channel",
       signature: "gpr.compilation.protocol.communication_channel",
       enclosing: "",
       is_private: false,
       documentation: "A communication channel, this channel is used for any communication\nbetween the build master and the slaves.",
       documentation_snippet: "type Communication_Channel is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Any_OS",
       qualified_name: "GPR.Compilation.Protocol.Any_OS",
       signature: "gpr.compilation.protocol.any_os",
       enclosing: "",
       is_private: false,
       documentation: "Used when OS check is not necessary, for example gprclean does not need\nthis check. It is safe to clean-up a Solaris slave from a Windows\nmaster.",
       documentation_snippet: "Any_OS : constant String := \"any\";",
       }   ,
       {
       name: "CD_Path_Tag",
       qualified_name: "GPR.Compilation.Protocol.CD_Path_Tag",
       signature: "gpr.compilation.protocol.cd_path_tag",
       enclosing: "",
       is_private: false,
       documentation: "The string replacing the compiler root directory, see Set_Rewrite below",
       documentation_snippet: "CD_Path_Tag   : constant String := \"<2>\";",
       }   ,
       {
       name: "Invalid_Pid",
       qualified_name: "GPR.Compilation.Protocol.Invalid_Pid",
       signature: "gpr.compilation.protocol.invalid_pid",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Pid : constant := -1;",
       }   ,
       {
       name: "No_Channel",
       qualified_name: "GPR.Compilation.Protocol.No_Channel",
       signature: "gpr.compilation.protocol.no_channel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Channel : constant Communication_Channel;",
       }   ,
       {
       name: "WD_Path_Tag",
       qualified_name: "GPR.Compilation.Protocol.WD_Path_Tag",
       signature: "gpr.compilation.protocol.wd_path_tag",
       enclosing: "",
       is_private: false,
       documentation: "The string replacing root working diretory of full path name, see\nSet_Rewrite below.",
       documentation_snippet: "WD_Path_Tag : constant String := \"<1>\";",
       }   ,
   ]
,}
---

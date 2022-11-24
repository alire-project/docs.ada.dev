---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Command_Line",
qualified_name: "Command_Line",
signature: "command_line",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                        Copyright (C) 2017, AdaCore                       --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Arguments",
       qualified_name: "Command_Line.Arguments",
       signature: "command_line.arguments",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Arguments (Number_Of_Args : Natural) is tagged private;",
       }   ,
       {
       name: "Command",
       qualified_name: "Command_Line.Command",
       signature: "command_line.command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Command",
       qualified_name: "Command_Line.Any_Command",
       signature: "command_line.any_command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Command is access all Command'Class;",
       }   ,
       {
       name: "Put_Line_Procedure",
       qualified_name: "Command_Line.Put_Line_Procedure",
       signature: "command_line.put_line_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Put_Line_Procedure is not null access procedure (Str : String);",
       }   ,
       {
       name: "Put_Procedure",
       qualified_name: "Command_Line.Put_Procedure",
       signature: "command_line.put_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Put_Procedure is not null access procedure (Str : String);",
       }   ,
       {
       name: "String_Access",
       qualified_name: "Command_Line.String_Access",
       signature: "command_line.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is access constant String;",
       }   ,
   ]
,}
---

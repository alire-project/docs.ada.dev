---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Commands",
qualified_name: "Gen.Commands",
signature: "gen.commands",
enclosing: "gen",
is_private: false,
documentation: "---------------------------------------------------------------------\n  gen-commands -- Commands for dynamo\n  Copyright (C) 2011, 2012, 2017, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
subtypes:    [
       {
       name: "Argument_List",
       qualified_name: "Gen.Commands.Argument_List",
       signature: "gen.commands.argument_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Argument_List is Util.Commands.Argument_List;",
       }   ,
       {
       name: "Command",
       qualified_name: "Gen.Commands.Command",
       signature: "gen.commands.command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Command is Drivers.Command_Type;",
       }   ,
       {
       name: "Command_Access",
       qualified_name: "Gen.Commands.Command_Access",
       signature: "gen.commands.command_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Command_Access is Drivers.Command_Access;",
       }   ,
   ]
,variables:    [
       {
       name: "Driver",
       qualified_name: "Gen.Commands.Driver",
       signature: "gen.commands.driver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Driver : Drivers.Driver_Type;",
       }   ,
   ]
,}
---

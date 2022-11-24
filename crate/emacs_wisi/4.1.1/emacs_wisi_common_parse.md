---
crate: emacs_wisi
layout: gnatdoc
gnatdoc: {
name: "Emacs_Wisi_Common_Parse",
qualified_name: "Emacs_Wisi_Common_Parse",
signature: "emacs_wisi_common_parse",
enclosing: "",
is_private: false,
documentation: "Abstract :\n\nCommon utilities for Gen_Emacs_Wisi_*_Parse\n\nCopyright (C) 2018 - 2022 Free Software Foundation, Inc.\n\nThis program is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or (at\nyour option) any later version. This program is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without even\nthe implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR\nPURPOSE. See the GNU General Public License for more details. You\nshould have received a copy of the GNU General Public License\ndistributed with this program; see file COPYING. If not, write to\nthe Free Software Foundation, 51 Franklin Street, Suite 500, Boston,\nMA 02110-1335, USA.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parse_Kind",
       qualified_name: "Emacs_Wisi_Common_Parse.Parse_Kind",
       signature: "emacs_wisi_common_parse.parse_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parse_Kind is (Partial, Incremental, Full);",
       }   ,
   ]
,record_types:    [
       {
       name: "Parse_Params",
       qualified_name: "Emacs_Wisi_Common_Parse.Parse_Params",
       signature: "emacs_wisi_common_parse.parse_params",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Kind\n  See Get_Parse_Params in body for what elisp this must match.\n@field Source_File_Name\n@field Verbosity\n@field Task_Count\n@field Zombie_Limit\n@field Enqueue_Limit\n@field Max_Parallel\n@field Language_Params\n@field Post_Parse_Action\n@field Begin_Byte_Pos\n  Source file byte position of first char sent; start parse here.\n@field End_Byte_Pos\n  Byte position of last char sent.\n  Emacs convention; after last char\n@field Goal_Byte_Pos\n  Byte position of end of desired parse region; terminate parse at\n  or after here.\n@field Begin_Char_Pos\n  Corresponding char positions; end is 0 if buffer empty.\n@field End_Char_Pos\n  Corresponding char positions; end is 0 if buffer empty.\n@field Goal_Char_Pos\n  Corresponding char positions; end is 0 if buffer empty.\n@field Begin_Line\n  Line containing Begin_Byte_Pos\n@field Begin_Indent\n  Indentation of Line_Begin\n@field Partial_Parse_Active\n@field Changes\n@field Byte_Count\n@field Full_End_Char_Pos\n  0 if buffer empty.",
       documentation_snippet: "type Parse_Params (Kind : Parse_Kind) is record\n   Source_File_Name  : Ada.Strings.Unbounded.Unbounded_String;\n   Verbosity     : Ada.Strings.Unbounded.Unbounded_String;\n   Task_Count    : Integer;\n   Zombie_Limit  : Integer;\n   Enqueue_Limit : Integer;\n   Max_Parallel  : Integer;\n   Language_Params : Ada.Strings.Unbounded.Unbounded_String;\n   case Kind is\n   when Partial =>\n      Post_Parse_Action : Wisi.Post_Parse_Action_Type;\n      Begin_Byte_Pos : Integer;\n      End_Byte_Pos : Integer;\n      Goal_Byte_Pos : Integer;\n      Begin_Char_Pos : WisiToken.Buffer_Pos;\n      End_Char_Pos   : WisiToken.Base_Buffer_Pos;\n      Goal_Char_Pos  : WisiToken.Buffer_Pos;\n      Begin_Line : WisiToken.Line_Number_Type;\n      Begin_Indent : Integer;\n      Partial_Parse_Active : Boolean;\n   when Incremental =>\n      Changes : Wisi.Parse_Context.Change_Lists.List;\n   when Full =>\n      Byte_Count        : Integer;\n      Full_End_Char_Pos : WisiToken.Base_Buffer_Pos;\n   end case;\nend record;",
       }   ,
       {
       name: "Post_Parse_Params",
       qualified_name: "Emacs_Wisi_Common_Parse.Post_Parse_Params",
       signature: "emacs_wisi_common_parse.post_parse_params",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Source_File_Name\n@field Verbosity\n@field Post_Parse_Action\n@field Begin_Byte_Pos\n  Region to execute action in.\n  Emacs convention; end is after last char\n@field Begin_Char_Pos\n  Region to execute action in.\n  Emacs convention; end is after last char\n@field End_Byte_Pos\n  Region to execute action in.\n  Emacs convention; end is after last char\n@field End_Char_Pos\n  Region to execute action in.\n  Emacs convention; end is after last char\n@field Language_Params",
       documentation_snippet: "type Post_Parse_Params is record\n   Source_File_Name  : Ada.Strings.Unbounded.Unbounded_String;\n   Verbosity         : Ada.Strings.Unbounded.Unbounded_String;\n   Post_Parse_Action : Wisi.Post_Parse_Action_Type;\n   Begin_Byte_Pos : Integer;\n   Begin_Char_Pos : Integer;\n   End_Byte_Pos   : Integer;\n   End_Char_Pos   : Integer;\n   Language_Params : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
       {
       name: "Process_Start_Params",
       qualified_name: "Emacs_Wisi_Common_Parse.Process_Start_Params",
       signature: "emacs_wisi_common_parse.process_start_params",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process_Start_Params is record\n   Recover_Log_File_Name : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
       {
       name: "Refactor_Params",
       qualified_name: "Emacs_Wisi_Common_Parse.Refactor_Params",
       signature: "emacs_wisi_common_parse.refactor_params",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Refactor_Action\n  Language-specific\n@field Source_File_Name\n@field Edit_Begin\n  Source file byte position at start of expression to refactor.\n@field Verbosity",
       documentation_snippet: "type Refactor_Params is record\n   Refactor_Action  : Wisi.Refactor_Action;\n   Source_File_Name : Ada.Strings.Unbounded.Unbounded_String;\n   Edit_Begin : WisiToken.Buffer_Pos;\n   Verbosity : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Prompt",
       qualified_name: "Emacs_Wisi_Common_Parse.Prompt",
       signature: "emacs_wisi_common_parse.prompt",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Prompt : constant String := \";;> \";",
       }   ,
       {
       name: "Protocol_Version",
       qualified_name: "Emacs_Wisi_Common_Parse.Protocol_Version",
       signature: "emacs_wisi_common_parse.protocol_version",
       enclosing: "",
       is_private: false,
       documentation: "Protocol_Version defines the data sent between elisp and the\nbackground process, except for the language-specific parameters,\nwhich are defined by the Language_Protocol_Version parameter to\nParse_Stream, below.\n\nThis value must match wisi-process-parse.el\nwisi-process-parse-protocol-version.\n\nSee wisi-process-parse.el functions, and this package body, for\nthe implementation of the protocol.\n\nOnly changes once per wisi release. Increment as soon as required,\nrecord new version in NEWS-wisi.text. If working on a branch and\nmain has already incremented, increment again, in case main is\nreleased before branch is merged; leave two \"increment protocol\"\nlines in NEWS-wisi.text to indicate the issue.",
       documentation_snippet: "Protocol_Version : constant String := \"6\";",
       }   ,
   ]
,}
---

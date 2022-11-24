---
crate: emacs_wisi
layout: gnatdoc
gnatdoc: {
name: "Wisi.Parse_Context",
qualified_name: "Wisi.Parse_Context",
signature: "wisi.parse_context",
enclosing: "wisi",
is_private: false,
documentation: "Abstract :\n\nParse context for one source file.\n\nCopyright (C) 2020 - 2022 Free Software Foundation All Rights Reserved.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.",
documentation_snippet: "",
record_types:    [
       {
       name: "Change",
       qualified_name: "Wisi.Parse_Context.Change",
       signature: "wisi.parse_context.change",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Begin_Byte_Pos\n  inserted or deleted\n@field Begin_Char_Pos\n@field Inserted_End_Byte_Pos\n@field Inserted_End_Char_Pos\n  emacs convention: end is after last inserted char\n@field Inserted_Text\n@field Deleted_Bytes\n@field Deleted_Chars",
       documentation_snippet: "type Change is record\n   Begin_Byte_Pos        : WisiToken.Buffer_Pos;\n   Begin_Char_Pos        : WisiToken.Buffer_Pos;\n   Inserted_End_Byte_Pos : WisiToken.Buffer_Pos;\n   Inserted_End_Char_Pos : WisiToken.Buffer_Pos;\n   Inserted_Text         : Ada.Strings.Unbounded.Unbounded_String;\n   Deleted_Bytes         : Natural;\n   Deleted_Chars         : Natural;\nend record;",
       }   ,
       {
       name: "Parse_Context",
       qualified_name: "Wisi.Parse_Context.Parse_Context",
       signature: "wisi.parse_context.parse_context",
       enclosing: "",
       is_private: false,
       documentation: "\n@field File_Name\n  Text_Buffer is encoded in UTF-8. Text_Buffer may hold all or part\n  of the actual Emacs buffer content. If partial, the lexer holds\n  the mapping from Text_Buffer index to Emacs buffer position.\n@field Text_Buffer\n  Text_Buffer is encoded in UTF-8. Text_Buffer may hold all or part\n  of the actual Emacs buffer content. If partial, the lexer holds\n  the mapping from Text_Buffer index to Emacs buffer position.\n@field Text_Buffer_Byte_Last\n  For Incremental parse; after editing, there may be empty space at\n  the end of Text_Buffer.\n@field Text_Buffer_Char_Last\n  For Incremental parse; after editing, there may be empty space at\n  the end of Text_Buffer.\n@field Parser\n@field Prev_Tree\n  Copy of Parser.Tree before edits applied; useful for debugging.\n@field Save_Prev_Text_Tree\n  If true, save text and copy tree before each edit.\n@field Root_Save_Edited_Name\n  If not \"\", save source text after the edit in a parse_incremental command,\n  to <root_save_edited_name_nnn>, where 'nnn' is a three-digit number that\n  increments.\n@field Save_Edited_Count\n@field Frozen",
       documentation_snippet: "type Parse_Context is tagged limited record\n   File_Name   : Ada.Strings.Unbounded.Unbounded_String;\n   Text_Buffer : Ada.Strings.Unbounded.String_Access;\n   Text_Buffer_Byte_Last : Integer := Integer'First;\n   Text_Buffer_Char_Last : Integer := Integer'Last;\n   Parser : WisiToken.Parse.Base_Parser_Access;\n   Prev_Tree : WisiToken.Syntax_Trees.Tree;\n   Save_Prev_Text_Tree : Boolean := False;\n   Root_Save_Edited_Name : Ada.Strings.Unbounded.Unbounded_String;\n   Save_Edited_Count : Integer := 0;\n   Frozen : Boolean := False;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Parse_Context_Access",
       qualified_name: "Wisi.Parse_Context.Parse_Context_Access",
       signature: "wisi.parse_context.parse_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parse_Context_Access is access all Parse_Context;",
       }   ,
   ]
,}
---

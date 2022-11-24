---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Lexer",
qualified_name: "Libadalang.Lexer",
signature: "libadalang.lexer",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
record_types:    [
       {
       name: "Lexer_Input",
       qualified_name: "Libadalang.Lexer.Lexer_Input",
       signature: "libadalang.lexer.lexer_input",
       enclosing: "",
       is_private: false,
       documentation: "Input from which the lexer will read tokens\n\n@field Kind\n@field Charset\n  Name of the charset to use in order to decode the input source\n@field Read_BOM\n  Whether the lexer should look for an optional Byte Order Mark\n@field Filename\n  Name of the file to read\n@field Bytes\n  Source buffer to read\n@field Text",
       documentation_snippet: "type Lexer_Input (Kind : Lexer_Input_Kind) is record\n   case Kind is\n   when File | Bytes_Buffer =>\n      Charset : Unbounded_String;\n      Read_BOM : Boolean;\n      case Kind is\n      when File =>\n         Filename : GNATCOLL.VFS.Virtual_File;\n      when Bytes_Buffer =>\n         Bytes : Unbounded_String;\n      when others => null;\n      end case;\n   when Text_Buffer =>\n      Text : Unbounded_Text_Type;\n   end case;\nend record;",
       }   ,
   ]
,}
---

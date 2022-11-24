---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Text",
qualified_name: "Langkit_Support.Text",
signature: "langkit_support.text",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
packages:    [
       {
       name: "Chars",
       qualified_name: "Langkit_Support.Text.Chars",
       signature: "langkit_support.text.chars",
       enclosing: "langkit_support.text",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
constants:           [
              {
              name: "CR",
              qualified_name: "Langkit_Support.Text.Chars.CR",
              signature: "langkit_support.text.chars.cr",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "CR : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.CR));",
              }          ,
              {
              name: "ESC",
              qualified_name: "Langkit_Support.Text.Chars.ESC",
              signature: "langkit_support.text.chars.esc",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "ESC : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.ESC));",
              }          ,
              {
              name: "FF",
              qualified_name: "Langkit_Support.Text.Chars.FF",
              signature: "langkit_support.text.chars.ff",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "FF : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.FF));",
              }          ,
              {
              name: "HT",
              qualified_name: "Langkit_Support.Text.Chars.HT",
              signature: "langkit_support.text.chars.ht",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "HT : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.HT));",
              }          ,
              {
              name: "LF",
              qualified_name: "Langkit_Support.Text.Chars.LF",
              signature: "langkit_support.text.chars.lf",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "LF : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.LF));",
              }          ,
              {
              name: "NUL",
              qualified_name: "Langkit_Support.Text.Chars.NUL",
              signature: "langkit_support.text.chars.nul",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "NUL : constant Character_Type :=\n   Wide_Wide_Character'Val (Character'Pos (ASCII.NUL));",
              }          ,
          ]
,       }   ,
   ]
,record_types:    [
       {
       name: "Text_Buffer_Ifc",
       qualified_name: "Langkit_Support.Text.Text_Buffer_Ifc",
       signature: "langkit_support.text.text_buffer_ifc",
       enclosing: "",
       is_private: false,
       documentation: "Text buffer base class type. This defines a type that encapsulates a\ntext buffer, and can return a specific line of it.\n\nAnalysis unit types implemented by libraries implement this interface,\nwhich in turns allows users to use features of\n:ada:ref:`Langkit_Support`, like pretty printing of diagnostics\nimplemented in :ada:ref:`Langkit_Support.Diagnostics.Output`.\n\n.. note: T821-010 - This should be an *interface*, but instead is an\n   abstract class, because of a bug in the generated equality operator.",
       documentation_snippet: "type Text_Buffer_Ifc is abstract tagged null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Text_Access",
       qualified_name: "Langkit_Support.Text.Text_Access",
       signature: "langkit_support.text.text_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Access is access all Text_Type;",
       }   ,
       {
       name: "Text_Cst_Access",
       qualified_name: "Langkit_Support.Text.Text_Cst_Access",
       signature: "langkit_support.text.text_cst_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Cst_Access is access constant Text_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Character_Type",
       qualified_name: "Langkit_Support.Text.Character_Type",
       signature: "langkit_support.text.character_type",
       enclosing: "",
       is_private: false,
       documentation: "Alias for :ada:ref:`Wide_Wide_Character`. Main character type in Langkit\nand generated libraries.",
       documentation_snippet: "subtype Character_Type is Wide_Wide_Character;",
       }   ,
       {
       name: "Text_Type",
       qualified_name: "Langkit_Support.Text.Text_Type",
       signature: "langkit_support.text.text_type",
       enclosing: "",
       is_private: false,
       documentation: "Alias for :ada:ref:`Wide_Wide_String`. Main string type in Langkit and\ngenerated libraries.",
       documentation_snippet: "subtype Text_Type is Wide_Wide_String;",
       }   ,
       {
       name: "Unbounded_Text_Type",
       qualified_name: "Langkit_Support.Text.Unbounded_Text_Type",
       signature: "langkit_support.text.unbounded_text_type",
       enclosing: "",
       is_private: false,
       documentation: "Alias for\n:ada:ref:`Ada.Strings.Wide_Wide_Unbounded.Unbounded_Wide_Wide_String`.\nMain unbounded string type in Langkit and generated libraries.",
       documentation_snippet: "subtype Unbounded_Text_Type is\n   Ada.Strings.Wide_Wide_Unbounded.Unbounded_Wide_Wide_String;",
       }   ,
   ]
,}
---

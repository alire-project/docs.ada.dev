---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Csets",
qualified_name: "Csets",
signature: "csets",
enclosing: "",
is_private: false,
documentation: "This package contains character tables for the various character\nsets that are supported for source representation. Character and\nstring literals are not affected, only identifiers. For each set,\nthe table in this package gives the mapping of letters to their\nupper case equivalent. Each table thus provides the information\nfor building the table used to fold lower case to upper case, and\nalso the table of flags showing which characters are allowed in\nidentifiers.",
documentation_snippet: "",
array_types:    [
       {
       name: "Char_Array_Flags",
       qualified_name: "Csets.Char_Array_Flags",
       signature: "csets.char_array_flags",
       enclosing: "",
       is_private: false,
       documentation: "Type used for character attribute arrays. Note that we deliberately\ndo NOT pack this table, since we don't want the extra overhead of\naccessing a packed bit string.",
       documentation_snippet: "type Char_Array_Flags is array (Character) of Boolean;",
       }   ,
       {
       name: "Translate_Table",
       qualified_name: "Csets.Translate_Table",
       signature: "csets.translate_table",
       enclosing: "",
       is_private: false,
       documentation: "Type used to describe translate tables",
       documentation_snippet: "type Translate_Table is array (Character) of Character;",
       }   ,
   ]
,variables:    [
       {
       name: "Fold_Lower",
       qualified_name: "Csets.Fold_Lower",
       signature: "csets.fold_lower",
       enclosing: "",
       is_private: false,
       documentation: "Table to fold upper case identifier letters to lower case",
       documentation_snippet: "Fold_Lower : Translate_Table;",
       }   ,
       {
       name: "Fold_Upper",
       qualified_name: "Csets.Fold_Upper",
       signature: "csets.fold_upper",
       enclosing: "",
       is_private: false,
       documentation: "Table to fold lower case identifier letters to upper case",
       documentation_snippet: "Fold_Upper : Translate_Table;",
       }   ,
       {
       name: "Identifier_Char",
       qualified_name: "Csets.Identifier_Char",
       signature: "csets.identifier_char",
       enclosing: "",
       is_private: false,
       documentation: "This table has True entries for all characters that can legally appear\nin identifiers, including digits, the underline character, all letters\nincluding upper and lower case and extended letters (as controlled by\nthe setting of Opt.Identifier_Character_Set), left bracket for brackets\nnotation wide characters and also ESC if wide characters are permitted\nin identifiers using escape sequences starting with ESC.",
       documentation_snippet: "Identifier_Char : Char_Array_Flags;",
       }   ,
   ]
,}
---

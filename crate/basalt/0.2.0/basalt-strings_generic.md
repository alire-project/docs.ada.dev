---
crate: basalt
layout: gnatdoc
gnatdoc: {
name: "Basalt.Strings_Generic",
qualified_name: "Basalt.Strings_Generic",
signature: "basalt.strings_generic",
enclosing: "basalt",
is_private: false,
documentation: "\n@summary Generic string operations\n@author  Johannes Kliemann\n@date    2019-11-19\n\nCopyright (C) 2019 Componolit GmbH\n\nThis file is part of Basalt, which is distributed under the terms of the\nGNU Affero General Public License version 3.",
documentation_snippet: "",
packages:    [
       {
       name: "Generic_Optional",
       qualified_name: "Basalt.Strings_Generic.Generic_Optional",
       signature: "basalt.strings_generic.generic_optional",
       enclosing: "basalt.strings_generic",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
record_types:           [
              {
              name: "Optional",
              qualified_name: "Basalt.Strings_Generic.Generic_Optional.Optional",
              signature: "basalt.strings_generic.generic_optional.optional",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Optional (Valid : Boolean := False) is record\n   case Valid is\n      when True =>\n         Value : T;\n      when False =>\n         null;\n   end case;\nend record;",
              }          ,
          ]
,       }   ,
       {
       name: "Value_Option_Modular",
       qualified_name: "Basalt.Strings_Generic.Value_Option_Modular",
       signature: "basalt.strings_generic.value_option_modular",
       enclosing: "basalt.strings_generic",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
subtypes:           [
              {
              name: "Optional",
              qualified_name: "Basalt.Strings_Generic.Value_Option_Modular.Optional",
              signature: "basalt.strings_generic.value_option_modular.optional",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Optional is Optional_Pac.Optional;",
              }          ,
          ]
,       }   ,
       {
       name: "Value_Option_Ranged",
       qualified_name: "Basalt.Strings_Generic.Value_Option_Ranged",
       signature: "basalt.strings_generic.value_option_ranged",
       enclosing: "basalt.strings_generic",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
subtypes:           [
              {
              name: "Optional",
              qualified_name: "Basalt.Strings_Generic.Value_Option_Ranged.Optional",
              signature: "basalt.strings_generic.value_option_ranged.optional",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Optional is Optional_Pac.Optional;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Residue_Class_Ring",
       qualified_name: "Basalt.Strings_Generic.Residue_Class_Ring",
       signature: "basalt.strings_generic.residue_class_ring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Residue_Class_Ring is new Integer range 0 .. 16;",
       }   ,
   ]
,array_types:    [
       {
       name: "Base_Size",
       qualified_name: "Basalt.Strings_Generic.Base_Size",
       signature: "basalt.strings_generic.base_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Base_Size is array (Base'Range) of Base_Value;",
       }   ,
       {
       name: "Charset",
       qualified_name: "Basalt.Strings_Generic.Charset",
       signature: "basalt.strings_generic.charset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Charset is array (Residue) of Character;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Base",
       qualified_name: "Basalt.Strings_Generic.Base",
       signature: "basalt.strings_generic.base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Base is Residue_Class_Ring range 2 .. 16;",
       }   ,
       {
       name: "Base_Value",
       qualified_name: "Basalt.Strings_Generic.Base_Value",
       signature: "basalt.strings_generic.base_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Base_Value is Positive range 16 .. 64;",
       }   ,
       {
       name: "Residue",
       qualified_name: "Basalt.Strings_Generic.Residue",
       signature: "basalt.strings_generic.residue",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Residue is Residue_Class_Ring range 0 .. 15;",
       }   ,
   ]
,constants:    [
       {
       name: "Base_Length",
       qualified_name: "Basalt.Strings_Generic.Base_Length",
       signature: "basalt.strings_generic.base_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Base_Length : constant Base_Size := (2  => 64,\n                                     3  => 41,\n                                     4  => 32,\n                                     5  => 28,\n                                     6  => 25,\n                                     7  => 23,\n                                     8  => 22,\n                                     9  => 21,\n                                     10 => 20,\n                                     11 => 19,\n                                     12 => 18,\n                                     13 => 18,\n                                     14 => 17,\n                                     15 => 17,\n                                     16 => 16);",
       }   ,
       {
       name: "Lowercase",
       qualified_name: "Basalt.Strings_Generic.Lowercase",
       signature: "basalt.strings_generic.lowercase",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lowercase : constant Charset := ('0', '1', '2', '3', '4', '5',\n                                 '6', '7', '8', '9',\n                                 'a', 'b', 'c', 'd', 'e', 'f');",
       }   ,
       {
       name: "Uppercase",
       qualified_name: "Basalt.Strings_Generic.Uppercase",
       signature: "basalt.strings_generic.uppercase",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Uppercase : constant Charset := ('0', '1', '2', '3', '4', '5',\n                                 '6', '7', '8', '9',\n                                 'A', 'B', 'C', 'D', 'E', 'F');",
       }   ,
   ]
,}
---

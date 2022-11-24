---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Strings",
qualified_name: "Wiki.Strings",
signature: "wiki.strings",
enclosing: "wiki",
is_private: false,
documentation: "",
documentation_snippet: "",
subtypes:    [
       {
       name: "BString",
       qualified_name: "Wiki.Strings.BString",
       signature: "wiki.strings.bstring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BString is Wide_Wide_Builders.Builder;",
       }   ,
       {
       name: "UString",
       qualified_name: "Wiki.Strings.UString",
       signature: "wiki.strings.ustring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype UString is Ada.Strings.Wide_Wide_Unbounded.Unbounded_Wide_Wide_String;",
       }   ,
       {
       name: "WChar",
       qualified_name: "Wiki.Strings.WChar",
       signature: "wiki.strings.wchar",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype WChar is Wide_Wide_Character;",
       }   ,
       {
       name: "WChar_Mapping",
       qualified_name: "Wiki.Strings.WChar_Mapping",
       signature: "wiki.strings.wchar_mapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype WChar_Mapping is Ada.Strings.Wide_Wide_Maps.Wide_Wide_Character_Mapping;",
       }   ,
       {
       name: "WString",
       qualified_name: "Wiki.Strings.WString",
       signature: "wiki.strings.wstring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype WString is Wide_Wide_String;",
       }   ,
   ]
,variables:    [
       {
       name: "Null_UString",
       qualified_name: "Wiki.Strings.Null_UString",
       signature: "wiki.strings.null_ustring",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_UString : UString\nrenames Ada.Strings.Wide_Wide_Unbounded.Null_Unbounded_Wide_Wide_String;",
       }   ,
   ]
,}
---

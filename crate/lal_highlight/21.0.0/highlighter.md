---
crate: lal_highlight
layout: gnatdoc
gnatdoc: {
name: "Highlighter",
qualified_name: "Highlighter",
signature: "highlighter",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Highlight_Type",
       qualified_name: "Highlighter.Highlight_Type",
       signature: "highlighter.highlight_type",
       enclosing: "",
       is_private: false,
       documentation: "Highlighting \"category\": keyword, comment, identifier, ...\n\n@enum Text\n@enum Comment\n@enum Keyword\n@enum Keyword_Type\n@enum Keyword_Special\n@enum Punctuation\n@enum Punctuation_Special\n@enum Operator\n@enum Preprocessor_Directive\n@enum Integer_Literal\n@enum String_Literal\n@enum Character_Literal\n@enum Identifier\n@enum Label_Name\n@enum Block_Name\n@enum Type_Name\n@enum Attribute_Name",
       documentation_snippet: "type Highlight_Type is\n  (Text,\n   Comment,\n   Keyword,\n   Keyword_Type,\n   Keyword_Special,\n   Punctuation,\n   Punctuation_Special,\n   Operator,\n   Preprocessor_Directive,\n   Integer_Literal,\n   String_Literal,\n   Character_Literal,\n   Identifier,\n   Label_Name,\n   Block_Name,\n   Type_Name,\n   Attribute_Name);",
       }   ,
       {
       name: "Highlights_Holder",
       qualified_name: "Highlighter.Highlights_Holder",
       signature: "highlighter.highlights_holder",
       enclosing: "",
       is_private: false,
       documentation: "Annotations on a set of tokens. Provides highlighting types for all\ntokens/trivias.",
       documentation_snippet: "type Highlights_Holder (Token_Count, Trivia_Count : Token_Index) is\nlimited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Token_Index",
       qualified_name: "Highlighter.Token_Index",
       signature: "highlighter.token_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Token_Index is Langkit_Support.Token_Data_Handlers.Token_Index;",
       }   ,
   ]
,}
---

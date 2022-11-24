---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Packrat",
qualified_name: "Langkit_Support.Packrat",
signature: "langkit_support.packrat",
enclosing: "langkit_support",
is_private: false,
documentation: "Those memo tables have a limited size, and use basic modulo to fit any\noffset in the limited size, so that an entry at index N will be put at\nindex N mod Memo_Size.\n\nIf there was already an entry at this spot, it will simply be removed.\nWhen querying for the entry at a given offset, we check whether there\nis an entry corresponding to Offset mod Memo_Size, and then if the entry\nexists, whether is corresponds to the same offset.\n\n@formal T\n@formal Token_Index\n@formal Memo_Size",
documentation_snippet: "",
simple_types:    [
       {
       name: "Memo_State",
       qualified_name: "Langkit_Support.Packrat.Memo_State",
       signature: "langkit_support.packrat.memo_state",
       enclosing: "",
       is_private: false,
       documentation: "State of a memo entry. Whether we have a result or not.\n\n@enum No_Result\n@enum Failure\n@enum Success",
       documentation_snippet: "type Memo_State is (No_Result, Failure, Success);",
       }   ,
       {
       name: "Memo_Type",
       qualified_name: "Langkit_Support.Packrat.Memo_Type",
       signature: "langkit_support.packrat.memo_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Memo_Type is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Memo_Entry",
       qualified_name: "Langkit_Support.Packrat.Memo_Entry",
       signature: "langkit_support.packrat.memo_entry",
       enclosing: "",
       is_private: false,
       documentation: "\n@field State\n  State of the memo entry\n@field Instance\n  Parsed object\n@field Offset\n  Real offset of this memo entry. Used to verify that it corresponds to\n  the queried offset.\n@field Final_Pos",
       documentation_snippet: "type Memo_Entry is record\n   State             : Memo_State := No_Result;\n   Instance          : T;\n   Offset            : Token_Index := Token_Index'First;\n   Final_Pos         : Token_Index := Token_Index'First;\nend record;",
       }   ,
   ]
,}
---

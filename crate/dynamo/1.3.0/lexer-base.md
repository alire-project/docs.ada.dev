---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Lexer.Base",
qualified_name: "Lexer.Base",
signature: "lexer.base",
enclosing: "lexer",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Private_Values",
       qualified_name: "Lexer.Base.Private_Values",
       signature: "lexer.base.private_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Private_Values is limited private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "Lexer.Base.Instance",
       signature: "lexer.base.instance",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Cur_Line\n@field Line_Start\n@field Prev_Lines_Chars\n@field Pos\n@field Buffer\n  input buffer. filled from the source.\n@field Internal",
       documentation_snippet: "type Instance is limited new Ada.Finalization.Limited_Controlled with record\n   Cur_Line    : Positive := 1;\n   Line_Start  : Positive := 1;\n   Prev_Lines_Chars : Natural := 0;\n   Pos         : Positive := 1;\n   Buffer      : Buffer_Type;\n   Internal : Private_Values;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Buffer_Type",
       qualified_name: "Lexer.Base.Buffer_Type",
       signature: "lexer.base.buffer_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer_Type is access all String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Rune",
       qualified_name: "Lexer.Base.Rune",
       signature: "lexer.base.rune",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Rune is Wide_Wide_Character;",
       }   ,
   ]
,constants:    [
       {
       name: "Carriage_Return",
       qualified_name: "Lexer.Base.Carriage_Return",
       signature: "lexer.base.carriage_return",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Carriage_Return : constant Character := Character'Val (13);",
       }   ,
       {
       name: "Default_Initial_Buffer_Size",
       qualified_name: "Lexer.Base.Default_Initial_Buffer_Size",
       signature: "lexer.base.default_initial_buffer_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Initial_Buffer_Size : constant := 8192;",
       }   ,
       {
       name: "End_Of_Input",
       qualified_name: "Lexer.Base.End_Of_Input",
       signature: "lexer.base.end_of_input",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "End_Of_Input    : constant Character := Character'Val (4);",
       }   ,
       {
       name: "Line_Feed",
       qualified_name: "Lexer.Base.Line_Feed",
       signature: "lexer.base.line_feed",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Line_Feed       : constant Character := Character'Val (10);",
       }   ,
   ]
,}
---

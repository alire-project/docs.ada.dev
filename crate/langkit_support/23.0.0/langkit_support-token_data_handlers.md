---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Token_Data_Handlers",
qualified_name: "Langkit_Support.Token_Data_Handlers",
signature: "langkit_support.token_data_handlers",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Raw_Token_Kind",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Raw_Token_Kind",
       signature: "langkit_support.token_data_handlers.raw_token_kind",
       enclosing: "",
       is_private: false,
       documentation: "Kind for a token, stored as a mere number",
       documentation_snippet: "type Raw_Token_Kind is new Natural;",
       }   ,
       {
       name: "Token_Index",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Token_Index",
       signature: "langkit_support.token_data_handlers.token_index",
       enclosing: "",
       is_private: false,
       documentation: "Although we cannot use anything else than Natural as Token_Vectors\nindexes, this type will be used outside this package so that typing\nhelps us finding index misuses.",
       documentation_snippet: "type Token_Index is new Integer range\n   Token_Vectors.Index_Type'First - 1\n   .. Token_Vectors.Index_Type'Last;",
       }   ,
   ]
,record_types:    [
       {
       name: "Stored_Token_Data",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Stored_Token_Data",
       signature: "langkit_support.token_data_handlers.stored_token_data",
       enclosing: "",
       is_private: false,
       documentation: "Holder for per-token data to be stored in the token data handler\n\n@field Kind\n@field Source_First\n  Bounds in the source buffer corresponding to this token\n@field Source_Last\n  Bounds in the source buffer corresponding to this token\n@field Symbol",
       documentation_snippet: "type Stored_Token_Data is record\n   Kind : Raw_Token_Kind;\n   Source_First : Positive;\n   Source_Last  : Natural;\n   Symbol : Thin_Symbol;\nend record with Pack;",
       }   ,
       {
       name: "Token_Data_Handler",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Token_Data_Handler",
       signature: "langkit_support.token_data_handlers.token_data_handler",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Version\n  Version number for this token data handler. Incremented each time the\n  handler is reset. This allows checking that token references are not\n  stale.\n  End of ABI area\n@field Source_Buffer\n  The whole source buffer. It belongs to this token data handler,\n  and will be deallocated along with it. WARNING: this buffer might\n  actually be *larger* than the real source, which is why we have the\n  ``Source_First``/``Source_Last`` fields below. We allocate a bigger\n  buffer pessimistically so we don't have to have a growable buffer.\n@field Source_First\n  Actual bounds in Source_Buffer for the source text\n@field Source_Last\n  Actual bounds in Source_Buffer for the source text\n@field Filename\n  If the source buffer comes from a file, Filename contains the name of\n  that file. No_File otherwise.\n@field Charset\n  If the source buffer was decoded, charset that was used to do so.\n  Empty string otherwise.\n@field Tokens\n  Sequence of tokens in the same order as found in the source file\n@field Trivias\n  Sequence of trivia in the same order as found in the source file.\n  Trivia are stored in a way that is related to the neighbor tokens:\n  \n  * If a token T0 at index I0 is followed by trivias T1, T2, ..., TN,\n    then the (I0+1)'th entry in Tokens_To_Trivia will contain an index\n    I1. T1 is then to be found in Trivia at index I1.\n  \n    If it's the only trivia before the next token, then Has_Next is\n    False for it, otherwise it is true and T2 is present at index I1+1.\n    The same goes on for T2, ..., until TN, the last trivia before the\n    next token, for which Has_Next is False.\n  \n  * If T0 is not followed by any trivia before the next token, then\n    the (I0+1)'th entry in Tokens_To_Trivia is No_Token_Index.\n@field Tokens_To_Trivias\n  This is the correspondence map between regular tokens and trivias:\n  see documentation for the Trivias field. Note that the first entry\n  stands for the leading trivia, i.e. trivia that come before the first\n  token, then the second entry stands for the trivia that come after\n  the first token, and so on.\n@field Symbols\n  Symbol table for this handler. Note that this can be shared accross\n  multiple Token_Data_Handlers.\n@field Lines_Starts\n  Table keeping count of line starts and line endings. The index of the\n  starting character for line N is at the Nth position in the vector.\n@field Tab_Stop\n@field Owner",
       documentation_snippet: "type Token_Data_Handler is record\n   Version : Version_Number;\n   Source_Buffer : Text_Access;\n   Source_First : Positive;\n   Source_Last  : Natural;\n   Filename : GNATCOLL.VFS.Virtual_File;\n   Charset : Ada.Strings.Unbounded.Unbounded_String;\n   Tokens : Token_Vectors.Vector;\n   Trivias : Trivia_Vectors.Vector;\n   Tokens_To_Trivias : Integer_Vectors.Vector;\n   Symbols : Symbol_Table;\n   Lines_Starts : Index_Vectors.Vector;\n   Tab_Stop : Positive;\n   Owner : System.Address;\nend record;",
       }   ,
       {
       name: "Token_Or_Trivia_Index",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Token_Or_Trivia_Index",
       signature: "langkit_support.token_data_handlers.token_or_trivia_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token_Or_Trivia_Index is record\n   Token, Trivia : Token_Index;\nend record;",
       }   ,
       {
       name: "Trivia_Node",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Trivia_Node",
       signature: "langkit_support.token_data_handlers.trivia_node",
       enclosing: "",
       is_private: false,
       documentation: "This defines a node in a trivia linked list\n\n@field T\n@field Has_Next",
       documentation_snippet: "type Trivia_Node is record\n   T        : aliased Stored_Token_Data;\n   Has_Next : Boolean;\nend record with Pack;",
       }   ,
   ]
,access_types:    [
       {
       name: "Token_Data_Handler_Access",
       qualified_name: "Langkit_Support.Token_Data_Handlers.Token_Data_Handler_Access",
       signature: "langkit_support.token_data_handlers.token_data_handler_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token_Data_Handler_Access is access all Token_Data_Handler;",
       }   ,
   ]
,constants:    [
       {
       name: "First_Token_Index",
       qualified_name: "Langkit_Support.Token_Data_Handlers.First_Token_Index",
       signature: "langkit_support.token_data_handlers.first_token_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "First_Token_Index : constant Token_Index := Token_Index'First + 1;",
       }   ,
       {
       name: "No_Token_Index",
       qualified_name: "Langkit_Support.Token_Data_Handlers.No_Token_Index",
       signature: "langkit_support.token_data_handlers.no_token_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Token_Index    : constant Token_Index := Token_Index'First;",
       }   ,
       {
       name: "No_Token_Or_Trivia_Index",
       qualified_name: "Langkit_Support.Token_Data_Handlers.No_Token_Or_Trivia_Index",
       signature: "langkit_support.token_data_handlers.no_token_or_trivia_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Token_Or_Trivia_Index : constant Token_Or_Trivia_Index :=\n  (No_Token_Index, No_Token_Index);",
       }   ,
   ]
,}
---

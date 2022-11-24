---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Source_File",
qualified_name: "Source_File",
signature: "source_file",
enclosing: "",
is_private: false,
documentation: ".  This package provides input from the source file to the lexical\n.  analyzer.\n.  UNGET will work to unget up to one character. You can unget more\n.  characters until you try to unget an EOLN where the exception\n.  PUSHBACK_ERROR is raised.\n.  The next character in the input stream\n.  can be looked at using PEEK_NEXT_CHAR without affecting the input\n.  stream.",
documentation_snippet: "",
constants:    [
       {
       name: "Eof",
       qualified_name: "Source_File.Eof",
       signature: "source_file.eof",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Eof  : constant Character := Ascii.Nul;",
       }   ,
       {
       name: "Eoln",
       qualified_name: "Source_File.Eoln",
       signature: "source_file.eoln",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Eoln : constant Character := Ascii.Lf;",
       }   ,
   ]
,}
---

---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Sinput",
qualified_name: "GPR.Sinput",
signature: "gpr.sinput",
enclosing: "gpr",
is_private: false,
documentation: "In GNAT, a physical line is ended by any of the sequences LF, CR/LF, or\nCR. LF is used in typical Unix systems, CR/LF in DOS systems, and CR\nalone in System 7. In addition, we recognize any of these sequences in\nany of the operating systems, for better behavior in treating foreign\nfiles (e.g. a Unix file with LF terminators transferred to a DOS system).\nFinally, wide character codes in categories Separator, Line and Separator,\nParagraph are considered to be physical line terminators.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Saved_Project_Scan_State",
       qualified_name: "GPR.Sinput.Saved_Project_Scan_State",
       signature: "gpr.sinput.saved_project_scan_state",
       enclosing: "",
       is_private: false,
       documentation: "Used to save project scan state in following two routines",
       documentation_snippet: "type Saved_Project_Scan_State is limited private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Lines_Table_Type",
       qualified_name: "GPR.Sinput.Lines_Table_Type",
       signature: "gpr.sinput.lines_table_type",
       enclosing: "",
       is_private: false,
       documentation: "Type used for lines table",
       documentation_snippet: "type Lines_Table_Type is\n  array (Line_Number range <>) of Source_Ptr;",
       }   ,
   ]
,record_types:    [
       {
       name: "Source_File_Record",
       qualified_name: "GPR.Sinput.Source_File_Record",
       signature: "gpr.sinput.source_file_record",
       enclosing: "",
       is_private: false,
       documentation: "\n@field File_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Reference_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Debug_Source_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Full_Debug_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Full_File_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Full_Ref_Name\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Source_Text\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Source_First\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Source_Last\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Last_Source_Line\n  The following fields are for internal use only (i.e. only in the\n  body of Sinput or its children, with no direct access by clients).\n@field Lines_Table",
       documentation_snippet: "type Source_File_Record is record\n   File_Name         : File_Name_Type;\n   Reference_Name    : File_Name_Type;\n   Debug_Source_Name : File_Name_Type;\n   Full_Debug_Name   : File_Name_Type;\n   Full_File_Name    : File_Name_Type;\n   Full_Ref_Name     : File_Name_Type;\n   Source_Text       : Source_Buffer_Ptr;\n   Source_First      : Source_Ptr;\n   Source_Last       : Source_Ptr;\n   Last_Source_Line  : Line_Number;\n   Lines_Table : Lines_Table_Ptr;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Lines_Table_Ptr",
       qualified_name: "GPR.Sinput.Lines_Table_Ptr",
       signature: "gpr.sinput.lines_table_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Type used for pointers to line tables",
       documentation_snippet: "type Lines_Table_Ptr is access all Lines_Table_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Internal_Source_Ptr",
       qualified_name: "GPR.Sinput.Internal_Source_Ptr",
       signature: "gpr.sinput.internal_source_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Pointer to internal source buffer",
       documentation_snippet: "Internal_Source_Ptr : constant Source_Buffer_Ptr :=\n                        Internal_Source'Unrestricted_Access;",
       }   ,
   ]
,variables:    [
       {
       name: "Current_Source_File",
       qualified_name: "GPR.Sinput.Current_Source_File",
       signature: "gpr.sinput.current_source_file",
       enclosing: "",
       is_private: false,
       documentation: "Source_File table index of source file currently being scanned.\nInitialized so that some tools (such as gprbuild) can be built with\n-gnatVa and pragma Initialized_Scalars without problems.",
       documentation_snippet: "Current_Source_File : Source_File_Index := No_Source_File;",
       }   ,
       {
       name: "Internal_Source",
       qualified_name: "GPR.Sinput.Internal_Source",
       signature: "gpr.sinput.internal_source",
       enclosing: "",
       is_private: false,
       documentation: "This buffer is used internally in the compiler when the lexical analyzer\nis used to scan a string from within the compiler. The procedure is to\nestablish Internal_Source_Ptr as the value of Source, set the string to\nbe scanned, appropriately terminated, in this buffer, and set Scan_Ptr\nto point to the start of the buffer. It is a fatal error if the scanner\nsignals an error while scanning a token in this internal buffer.",
       documentation_snippet: "Internal_Source : aliased Source_Buffer (1 .. 81);",
       }   ,
       {
       name: "Main_Source_File",
       qualified_name: "GPR.Sinput.Main_Source_File",
       signature: "gpr.sinput.main_source_file",
       enclosing: "",
       is_private: false,
       documentation: "This is set to the source file index of the main unit",
       documentation_snippet: "Main_Source_File : Source_File_Index := No_Source_File;",
       }   ,
       {
       name: "Source",
       qualified_name: "GPR.Sinput.Source",
       signature: "gpr.sinput.source",
       enclosing: "",
       is_private: false,
       documentation: "Current source (copy of Source_File.Table (Current_Source_Unit).Source)",
       documentation_snippet: "Source : Source_Buffer_Ptr;",
       }   ,
       {
       name: "Source_File_Index_Table",
       qualified_name: "GPR.Sinput.Source_File_Index_Table",
       signature: "gpr.sinput.source_file_index_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Source_File_Index_Table :\n  array (Int range 0 .. 1 + (Int'Last / Source_Align)) of Source_File_Index;",
       }   ,
       {
       name: "Upper_Half_Encoding",
       qualified_name: "GPR.Sinput.Upper_Half_Encoding",
       signature: "gpr.sinput.upper_half_encoding",
       enclosing: "",
       is_private: false,
       documentation: "Normally set False, indicating that upper half ISO 8859-1 characters are\nused in the normal way to represent themselves. If the wide character\nencoding method uses the upper bit for this encoding, then this flag is\nset True, and upper half characters in the source indicate the start of\na wide character sequence.",
       documentation_snippet: "Upper_Half_Encoding : Boolean := False;",
       }   ,
   ]
,}
---

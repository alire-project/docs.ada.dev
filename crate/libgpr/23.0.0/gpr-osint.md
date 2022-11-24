---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Osint",
qualified_name: "GPR.Osint",
signature: "gpr.osint",
enclosing: "gpr",
is_private: false,
documentation: "---------------------------------------\n Types Used for Text Buffer Handling --\n---------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Column_Number",
       qualified_name: "GPR.Osint.Column_Number",
       signature: "gpr.osint.column_number",
       enclosing: "",
       is_private: false,
       documentation: "Column number (assume that 2**15 - 1 is large enough). The range for\nthis type is used to compute Hostparm.Max_Line_Length. See also the\nprocessing for -gnatyM in Stylesw).",
       documentation_snippet: "type Column_Number is range 0 .. 32767;",
       }   ,
       {
       name: "Exit_Code_Type",
       qualified_name: "GPR.Osint.Exit_Code_Type",
       signature: "gpr.osint.exit_code_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum E_Success\n  No errors (but there may be warnings)\n@enum E_General\n  General tool error (invalid option, missing file, etc)\n@enum E_Subtool\n  Underlying tool error\n@enum E_Project\n  Project parsing error\n@enum E_Fatal\n  Critical tool error (defensive code failures and the like)",
       documentation_snippet: "type Exit_Code_Type is\n  (E_Success,\n   E_General,\n   E_Subtool,\n   E_Project,\n   E_Fatal);",
       }   ,
       {
       name: "Line_Number",
       qualified_name: "GPR.Osint.Line_Number",
       signature: "gpr.osint.line_number",
       enclosing: "",
       is_private: false,
       documentation: "Special value used to indicate no line number",
       documentation_snippet: "type Line_Number is range 0 .. Int'Last;",
       }   ,
   ]
,array_types:    [
       {
       name: "Text_Buffer",
       qualified_name: "GPR.Osint.Text_Buffer",
       signature: "gpr.osint.text_buffer",
       enclosing: "",
       is_private: false,
       documentation: "Text buffer used to hold source file or library information file",
       documentation_snippet: "type Text_Buffer is array (Text_Ptr range <>) of Character;",
       }   ,
   ]
,access_types:    [
       {
       name: "Source_Buffer_Ptr",
       qualified_name: "GPR.Osint.Source_Buffer_Ptr",
       signature: "gpr.osint.source_buffer_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Pointer to source buffer. We use virtual origin addressing for source\nbuffers, with thin pointers. The pointer points to a virtual instance\nof type Big_Source_Buffer, where the actual type is in fact of type\nSource_Buffer. The address is adjusted so that the virtual origin\naddressing works correctly. See Osint.Read_Source_Buffer for further\ndetails. Again, as for Big_String_Ptr, we should never allocate using\nthis type, but we don't give a storage size clause of zero, since we\nmay end up doing deallocations of instances allocated manually.",
       documentation_snippet: "type Source_Buffer_Ptr is access all Big_Source_Buffer;",
       }   ,
       {
       name: "Text_Buffer_Ptr",
       qualified_name: "GPR.Osint.Text_Buffer_Ptr",
       signature: "gpr.osint.text_buffer_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Text buffers for input files are allocated dynamically and this type\nis used to reference these text buffers.",
       documentation_snippet: "type Text_Buffer_Ptr is access all Text_Buffer;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Big_Source_Buffer",
       qualified_name: "GPR.Osint.Big_Source_Buffer",
       signature: "gpr.osint.big_source_buffer",
       enclosing: "",
       is_private: false,
       documentation: "This is a virtual type used as the designated type of the access type\nSource_Buffer_Ptr, see Osint.Read_Source_File for details.",
       documentation_snippet: "subtype Big_Source_Buffer is Text_Buffer (0 .. Text_Ptr'Last);",
       }   ,
       {
       name: "Source_Buffer",
       qualified_name: "GPR.Osint.Source_Buffer",
       signature: "gpr.osint.source_buffer",
       enclosing: "",
       is_private: false,
       documentation: "Type used to store text of a source file. The buffer for the main source\n(the source specified on the command line) has a lower bound starting\nat zero. Subsequent subsidiary sources have lower bounds which are\none greater than the previous upper bound, rounded up to a multiple\nof Source_Align.",
       documentation_snippet: "subtype Source_Buffer is Text_Buffer;",
       }   ,
       {
       name: "Text_Ptr",
       qualified_name: "GPR.Osint.Text_Ptr",
       signature: "gpr.osint.text_ptr",
       enclosing: "",
       is_private: false,
       documentation: "Type used for subscripts in text buffer",
       documentation_snippet: "subtype Text_Ptr is Source_Ptr;",
       }   ,
   ]
,constants:    [
       {
       name: "Env_Vars_Case_Sensitive",
       qualified_name: "GPR.Osint.Env_Vars_Case_Sensitive",
       signature: "gpr.osint.env_vars_case_sensitive",
       enclosing: "",
       is_private: false,
       documentation: "Set to indicate whether the operating system convention is for\nenvironment variable names to be case sensitive (e.g., in Unix, set\nTrue), or non case sensitive (e.g., in Windows, set False).",
       documentation_snippet: "Env_Vars_Case_Sensitive : constant Boolean :=\n                            Get_Env_Vars_Case_Sensitive /= 0;",
       }   ,
       {
       name: "File_Names_Case_Sensitive",
       qualified_name: "GPR.Osint.File_Names_Case_Sensitive",
       signature: "gpr.osint.file_names_case_sensitive",
       enclosing: "",
       is_private: false,
       documentation: "Set to indicate whether the operating system convention is for file\nnames to be case sensitive (e.g., in Unix, set True), or non case\nsensitive (e.g., in Windows, set False).",
       documentation_snippet: "File_Names_Case_Sensitive : constant Boolean :=\n                              Get_File_Names_Case_Sensitive /= 0;",
       }   ,
       {
       name: "Invalid_Time",
       qualified_name: "GPR.Osint.Invalid_Time",
       signature: "gpr.osint.invalid_time",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Time : constant Ada.Calendar.Time;",
       }   ,
       {
       name: "No_Column_Number",
       qualified_name: "GPR.Osint.No_Column_Number",
       signature: "gpr.osint.no_column_number",
       enclosing: "",
       is_private: false,
       documentation: "Special value used to indicate no column number",
       documentation_snippet: "No_Column_Number : constant Column_Number := 0;",
       }   ,
       {
       name: "No_Line_Number",
       qualified_name: "GPR.Osint.No_Line_Number",
       signature: "gpr.osint.no_line_number",
       enclosing: "",
       is_private: false,
       documentation: "Special value used to indicate no line number",
       documentation_snippet: "No_Line_Number : constant Line_Number := 0;",
       }   ,
       {
       name: "Source_Align",
       qualified_name: "GPR.Osint.Source_Align",
       signature: "gpr.osint.source_align",
       enclosing: "",
       is_private: false,
       documentation: "Alignment requirement for source buffers (by keeping source buffers\naligned, we can optimize the implementation of Get_Source_File_Index.\nSee this routine in Sinput for details.",
       documentation_snippet: "Source_Align : constant := 2 ** 12;",
       }   ,
   ]
,}
---

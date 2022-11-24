---
crate: b2ssum
layout: gnatdoc
gnatdoc: {
name: "SPARK_IO",
qualified_name: "SPARK_IO",
signature: "spark_io",
enclosing: "",
is_private: false,
documentation: "# type State_Type is abstract;\n# type Inputs_Type is abstract;\n# type Outputs_Type is abstract;",
documentation_snippet: "",
simple_types:    [
       {
       name: "File_Mode_T",
       qualified_name: "SPARK_IO.File_Mode_T",
       signature: "spark_io.file_mode_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Mode_T is (In_File, Out_File);",
       }   ,
       {
       name: "File_Status_T",
       qualified_name: "SPARK_IO.File_Status_T",
       signature: "spark_io.file_status_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_Status_T is\n  (Success, Status_Error, Mode_Error, Name_Error, Use_Error, Device_Error,\n   End_Error, Data_Error, Layout_Error, Standard_Storage_Error,\n   Standard_Program_Error);",
       }   ,
       {
       name: "File_T",
       qualified_name: "SPARK_IO.File_T",
       signature: "spark_io.file_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File_T is limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Number_Base_T",
       qualified_name: "SPARK_IO.Number_Base_T",
       signature: "spark_io.number_base_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Number_Base_T is Positive range 2 .. 16;",
       }   ,
   ]
,}
---

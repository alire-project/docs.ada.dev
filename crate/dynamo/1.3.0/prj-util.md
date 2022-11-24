---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Util",
qualified_name: "Prj.Util",
signature: "prj.util",
enclosing: "prj",
is_private: false,
documentation: "Utilities for use in processing project files",
documentation_snippet: "",
simple_types:    [
       {
       name: "Source_Info_Iterator",
       qualified_name: "Prj.Util.Source_Info_Iterator",
       signature: "prj.util.source_info_iterator",
       enclosing: "",
       is_private: false,
       documentation: "Iterator to get the sources for a single project",
       documentation_snippet: "type Source_Info_Iterator is private;",
       }   ,
       {
       name: "Text_File",
       qualified_name: "Prj.Util.Text_File",
       signature: "prj.util.text_file",
       enclosing: "",
       is_private: false,
       documentation: "Represents a text file (default is invalid text file)",
       documentation_snippet: "type Text_File is limited private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Source_Info_Data",
       qualified_name: "Prj.Util.Source_Info_Data",
       signature: "prj.util.source_info_data",
       enclosing: "",
       is_private: false,
       documentation: "Data read from a source info file for a single source\n\n@field Project\n@field Language\n@field Kind\n@field Display_Path_Name\n@field Path_Name\n@field Unit_Name\n@field Index\n@field Naming_Exception",
       documentation_snippet: "type Source_Info_Data is record\n   Project           : Name_Id;\n   Language          : Name_Id;\n   Kind              : Source_Kind;\n   Display_Path_Name : Name_Id;\n   Path_Name         : Name_Id;\n   Unit_Name         : Name_Id               := No_Name;\n   Index             : Int                   := 0;\n   Naming_Exception  : Naming_Exception_Type := No;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Source_Info",
       qualified_name: "Prj.Util.Source_Info",
       signature: "prj.util.source_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Info is access all Source_Info_Data;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Source_Info",
       qualified_name: "Prj.Util.No_Source_Info",
       signature: "prj.util.no_source_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Source_Info : constant Source_Info := null;",
       }   ,
   ]
,}
---

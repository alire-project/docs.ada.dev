---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Attr",
qualified_name: "Prj.Attr",
signature: "prj.attr",
enclosing: "prj",
is_private: false,
documentation: "It is also possible to define new packages with their attributes",
documentation_snippet: "",
simple_types:    [
       {
       name: "Attribute_Kind",
       qualified_name: "Prj.Attr.Attribute_Kind",
       signature: "prj.attr.attribute_kind",
       enclosing: "",
       is_private: false,
       documentation: "Characteristics of an attribute. Optional_Index indicates that there\nmay be an optional index in the index of the associative array, as in\n   for Switches (\"files.ada\" at 2) use ...\n\n@enum Unknown\n  The attribute does not exist\n@enum Single\n  Single variable attribute (not an associative array)\n@enum Associative_Array\n  Associative array attribute with a case sensitive index\n@enum Optional_Index_Associative_Array\n  Associative array attribute with a case sensitive index and an\n  optional source index.\n@enum Case_Insensitive_Associative_Array\n  Associative array attribute with a case insensitive index\n@enum Optional_Index_Case_Insensitive_Associative_Array",
       documentation_snippet: "type Attribute_Kind is (\n   Unknown,\n   Single,\n   Associative_Array,\n   Optional_Index_Associative_Array,\n   Case_Insensitive_Associative_Array,\n   Optional_Index_Case_Insensitive_Associative_Array\n);",
       }   ,
       {
       name: "Attribute_Node_Id",
       qualified_name: "Prj.Attr.Attribute_Node_Id",
       signature: "prj.attr.attribute_node_id",
       enclosing: "",
       is_private: false,
       documentation: "The type to refers to an attribute, self-initialized",
       documentation_snippet: "type Attribute_Node_Id is private;",
       }   ,
       {
       name: "Package_Node_Id",
       qualified_name: "Prj.Attr.Package_Node_Id",
       signature: "prj.attr.package_node_id",
       enclosing: "",
       is_private: false,
       documentation: "Type to refer to a package, self initialized",
       documentation_snippet: "type Package_Node_Id is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Attribute_Data_Array",
       qualified_name: "Prj.Attr.Attribute_Data_Array",
       signature: "prj.attr.attribute_data_array",
       enclosing: "",
       is_private: false,
       documentation: "A list of attribute name/characteristics to be used as parameter of\nprocedure Register_New_Package below.",
       documentation_snippet: "type Attribute_Data_Array is array (Positive range <>) of Attribute_Data;",
       }   ,
   ]
,record_types:    [
       {
       name: "Attribute_Data",
       qualified_name: "Prj.Attr.Attribute_Data",
       signature: "prj.attr.attribute_data",
       enclosing: "",
       is_private: false,
       documentation: "Name and characteristics of an attribute in a package registered\nexplicitly with Register_New_Package (see below).\n\n@field Name_Length\n@field Name\n  The name of the attribute\n@field Attr_Kind\n  The type of the attribute\n@field Index_Is_File_Name\n  For associative arrays, indicate if the index is a file name, so\n  that the attribute kind may be modified depending on the case\n  sensitivity of file names. This is only taken into account when\n  Attr_Kind is Associative_Array or Optional_Index_Associative_Array.\n@field Opt_Index\n  True if there may be an optional index in the value of the index,\n  as in:\n    \"file.ada\" at 2\n    (\"main.adb\", \"file.ada\" at 1)\n@field Var_Kind\n  The attribute value kind: single or list\n@field Default",
       documentation_snippet: "type Attribute_Data (Name_Length : Attribute_Name_Length := 1) is record\n   Name : String (1 .. Name_Length);\n   Attr_Kind  : Defined_Attribute_Kind;\n   Index_Is_File_Name : Boolean;\n   Opt_Index : Boolean;\n   Var_Kind : Defined_Variable_Kind;\n   Default : Attribute_Default_Value := Empty_Value;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "All_Case_Insensitive_Associative_Array",
       qualified_name: "Prj.Attr.All_Case_Insensitive_Associative_Array",
       signature: "prj.attr.all_case_insensitive_associative_array",
       enclosing: "",
       is_private: false,
       documentation: "Subtype including both cases of Case_Insensitive_Associative_Array",
       documentation_snippet: "subtype All_Case_Insensitive_Associative_Array is Attribute_Kind range\n  Case_Insensitive_Associative_Array ..\n  Optional_Index_Case_Insensitive_Associative_Array;",
       }   ,
       {
       name: "Attribute_Name_Length",
       qualified_name: "Prj.Attr.Attribute_Name_Length",
       signature: "prj.attr.attribute_name_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Attribute_Name_Length is\n  Positive range 1 .. Max_Attribute_Name_Length;",
       }   ,
       {
       name: "Defined_Attribute_Kind",
       qualified_name: "Prj.Attr.Defined_Attribute_Kind",
       signature: "prj.attr.defined_attribute_kind",
       enclosing: "",
       is_private: false,
       documentation: "Subset of Attribute_Kinds that may be used for the attributes that is\nused when defining a new package.",
       documentation_snippet: "subtype Defined_Attribute_Kind is Attribute_Kind\n  range Single .. Optional_Index_Case_Insensitive_Associative_Array;",
       }   ,
   ]
,constants:    [
       {
       name: "Attribute_First",
       qualified_name: "Prj.Attr.Attribute_First",
       signature: "prj.attr.attribute_first",
       enclosing: "",
       is_private: false,
       documentation: "First attribute node id of project level attributes",
       documentation_snippet: "Attribute_First : constant Attribute_Node_Id;",
       }   ,
       {
       name: "Empty_Attribute",
       qualified_name: "Prj.Attr.Empty_Attribute",
       signature: "prj.attr.empty_attribute",
       enclosing: "",
       is_private: false,
       documentation: "Indicates no attribute. Default value of Attribute_Node_Id objects",
       documentation_snippet: "Empty_Attribute : constant Attribute_Node_Id;",
       }   ,
       {
       name: "Empty_Package",
       qualified_name: "Prj.Attr.Empty_Package",
       signature: "prj.attr.empty_package",
       enclosing: "",
       is_private: false,
       documentation: "Default value of Package_Node_Id objects",
       documentation_snippet: "Empty_Package : constant Package_Node_Id;",
       }   ,
       {
       name: "Max_Attribute_Name_Length",
       qualified_name: "Prj.Attr.Max_Attribute_Name_Length",
       signature: "prj.attr.max_attribute_name_length",
       enclosing: "",
       is_private: false,
       documentation: "The maximum length of attribute names",
       documentation_snippet: "Max_Attribute_Name_Length : constant := 64;",
       }   ,
       {
       name: "Unknown_Package",
       qualified_name: "Prj.Attr.Unknown_Package",
       signature: "prj.attr.unknown_package",
       enclosing: "",
       is_private: false,
       documentation: "Value of an unknown package that has been found but is unknown",
       documentation_snippet: "Unknown_Package : constant Package_Node_Id;",
       }   ,
   ]
,}
---

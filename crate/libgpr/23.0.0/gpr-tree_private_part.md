---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "Tree_Private_Part",
qualified_name: "GPR.Tree_Private_Part",
signature: "gpr.tree_private_part",
enclosing: "gpr",
is_private: false,
documentation: "This is conceptually in the private part. However, for efficiency,\nsome packages are accessing it directly.",
documentation_snippet: "",
record_types:    [
       {
       name: "Project_Name_And_Node",
       qualified_name: "GPR.Tree_Private_Part.Project_Name_And_Node",
       signature: "gpr.tree_private_part.project_name_and_node",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Name\n  Name of the project\n@field Node\n  Node of the project in table Project_Nodes\n@field Resolved_Path\n  Resolved and canonical path of a real project file.\n  No_Name in case of virtual projects.\n@field Extended\n  True when the project is being extended by another project\n@field From_Extended\n  True when the project is only imported by projects that are\n  extended.\n@field Proj_Qualifier",
       documentation_snippet: "type Project_Name_And_Node is record\n   Name : Name_Id;\n   Node : Project_Node_Id;\n   Resolved_Path : Path_Name_Type;\n   Extended : Boolean;\n   From_Extended : Boolean;\n   Proj_Qualifier : Project_Qualifier;\nend record;",
       }   ,
       {
       name: "Project_Node_Record",
       qualified_name: "GPR.Tree_Private_Part.Project_Node_Record",
       signature: "gpr.tree_private_part.project_node_record",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Kind\n@field Qualifier\n@field Location\n@field Directory\n  Only for N_Project\n@field Display_Name\n  Only for N_Project\n@field Expr_Kind\n  See below for what Project_Node_Kind it is used\n@field Variables\n  First variable in a project or a package\n@field Packages\n  First package declaration in a project\n@field Pkg_Id\n  Only used for N_Package_Declaration\n  \n  The component Pkg_Id is an entry into the table Package_Attributes\n  (in Prj.Attr). It is used to indicate all the attributes of the\n  package with their characteristics.\n  \n  The tables Prj.Attr.Attributes and Prj.Attr.Package_Attributes\n  are built once and for all through a call (from Prj.Initialize)\n  to procedure Prj.Attr.Initialize. It is never modified after that.\n@field Name\n  See below for what Project_Node_Kind it is used\n@field Src_Index\n  Index of a unit in a multi-unit source.\n  Only for some N_Attribute_Declaration and N_Literal_String.\n@field Path_Name\n  See below for what Project_Node_Kind it is used\n@field Value\n  See below for what Project_Node_Kind it is used\n@field Default\n  Only used in N_Attribute_Reference\n@field Field1\n  See below the meaning for each Project_Node_Kind\n@field Field2\n  See below the meaning for each Project_Node_Kind\n@field Field3\n  See below the meaning for each Project_Node_Kind\n@field Field4\n  See below the meaning for each Project_Node_Kind\n@field Flag1\n  This flag is significant only for:\n  \n    N_Attribute_Declaration and N_Attribute_Reference\n      Indicates for an associative array attribute, that the\n      index is case insensitive.\n  \n    N_Comment\n      Indicates that the comment is preceded by an empty line.\n  \n    N_Project\n      Indicates that there are comments in the project source that\n      cannot be kept in the tree.\n  \n    N_Project_Declaration\n      Indicates that there are unkept comments in the project.\n  \n    N_With_Clause\n      Indicates that this is not the last with in a with clause.\n      Set for \"A\", but not for \"B\" in with \"B\"; and with \"A\", \"B\";\n@field Flag2\n  This flag is significant only for:\n  \n    N_Attribute_Declaration and N_Attribute_Reference\n      Indicates if attribute values are concatenated with the value\n      in the configuration project for the same attribute.\n  \n    N_Project\n      Indicates that the project \"extends all\" another project.\n  \n    N_Comment\n      Indicates that the comment is followed by an empty line.\n  \n    N_With_Clause\n      Indicates that the originally imported project is an extending\n      all project.\n@field Comments\n  For nodes other that N_Comment_Zones or N_Comment, designates the\n  comment zones associated with the node.\n  \n  For N_Comment_Zones, designates the comment after the \"end\" of\n  the construct.\n  \n  For N_Comment, designates the next comment, if any.\n@field Checksum",
       documentation_snippet: "type Project_Node_Record is record\n   Kind : Project_Node_Kind;\n   Qualifier : Project_Qualifier := Unspecified;\n   Location : Source_Ptr := No_Location;\n   Directory : Path_Name_Type := No_Path;\n   Display_Name : Name_Id := No_Name;\n   Expr_Kind : Variable_Kind := Undefined;\n   Variables : Variable_Node_Id := Empty_Project_Node;\n   Packages : Package_Declaration_Id := Empty_Project_Node;\n   Pkg_Id : Package_Node_Id := Empty_Package;\n   Name : Name_Id := No_Name;\n   Src_Index : Int := 0;\n   Path_Name : Path_Name_Type := No_Path;\n   Value : Name_Id := No_Name;\n   Default : Attribute_Default_Value := Empty_Value;\n   Field1 : Project_Node_Id := Empty_Project_Node;\n   Field2 : Project_Node_Id := Empty_Project_Node;\n   Field3 : Project_Node_Id := Empty_Project_Node;\n   Field4 : Project_Node_Id := Empty_Project_Node;\n   Flag1 : Boolean := False;\n   Flag2 : Boolean := False;\n   Comments : Project_Node_Id := Empty_Project_Node;\n   Checksum : Word := 0;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Project_Name_And_Node",
       qualified_name: "GPR.Tree_Private_Part.No_Project_Name_And_Node",
       signature: "gpr.tree_private_part.no_project_name_and_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Project_Name_And_Node : constant Project_Name_And_Node :=\n  (Name           => No_Name,\n   Node           => Empty_Project_Node,\n   Resolved_Path  => No_Path,\n   Extended       => True,\n   From_Extended  => False,\n   Proj_Qualifier => Unspecified);",
       }   ,
   ]
,}
---

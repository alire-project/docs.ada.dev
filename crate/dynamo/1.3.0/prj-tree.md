---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Tree",
qualified_name: "Prj.Tree",
signature: "prj.tree",
enclosing: "prj",
is_private: false,
documentation: "---------------\n Environment --\n---------------",
documentation_snippet: "",
packages:    [
       {
       name: "Tree_Private_Part",
       qualified_name: "Prj.Tree.Tree_Private_Part",
       signature: "prj.tree.tree_private_part",
       enclosing: "prj.tree",
       is_private: false,
       documentation: "This is conceptually in the private part. However, for efficiency,\nsome packages are accessing it directly.",
       documentation_snippet: "",
record_types:           [
              {
              name: "Project_Name_And_Node",
              qualified_name: "Prj.Tree.Tree_Private_Part.Project_Name_And_Node",
              signature: "prj.tree.tree_private_part.project_name_and_node",
              enclosing: "",
              is_private: false,
              documentation: "\n@field Name\n  Name of the project\n@field Node\n  Node of the project in table Project_Nodes\n@field Resolved_Path\n  Resolved and canonical path of a real project file.\n  No_Name in case of virtual projects.\n@field Extended\n  True when the project is being extended by another project\n@field From_Extended\n  True when the project is only imported by projects that are\n  extended.\n@field Proj_Qualifier",
              documentation_snippet: "type Project_Name_And_Node is record\n   Name : Name_Id;\n   Node : Project_Node_Id;\n   Resolved_Path : Path_Name_Type;\n   Extended : Boolean;\n   From_Extended : Boolean;\n   Proj_Qualifier : Project_Qualifier;\nend record;",
              }          ,
              {
              name: "Project_Node_Record",
              qualified_name: "Prj.Tree.Tree_Private_Part.Project_Node_Record",
              signature: "prj.tree.tree_private_part.project_node_record",
              enclosing: "",
              is_private: false,
              documentation: "\n@field Kind\n@field Qualifier\n@field Location\n@field Directory\n  Only for N_Project\n@field Display_Name\n  Only for N_Project\n@field Expr_Kind\n  See below for what Project_Node_Kind it is used\n@field Variables\n  First variable in a project or a package\n@field Packages\n  First package declaration in a project\n@field Pkg_Id\n  Only used for N_Package_Declaration\n  \n  The component Pkg_Id is an entry into the table Package_Attributes\n  (in Prj.Attr). It is used to indicate all the attributes of the\n  package with their characteristics.\n  \n  The tables Prj.Attr.Attributes and Prj.Attr.Package_Attributes\n  are built once and for all through a call (from Prj.Initialize)\n  to procedure Prj.Attr.Initialize. It is never modified after that.\n@field Name\n  See below for what Project_Node_Kind it is used\n@field Src_Index\n  Index of a unit in a multi-unit source.\n  Only for some N_Attribute_Declaration and N_Literal_String.\n@field Path_Name\n  See below for what Project_Node_Kind it is used\n@field Value\n  See below for what Project_Node_Kind it is used\n@field Default\n  Only used in N_Attribute_Reference\n@field Field1\n  See below the meaning for each Project_Node_Kind\n@field Field2\n  See below the meaning for each Project_Node_Kind\n@field Field3\n  See below the meaning for each Project_Node_Kind\n@field Field4\n  See below the meaning for each Project_Node_Kind\n@field Flag1\n  This flag is significant only for:\n  \n    N_Attribute_Declaration and N_Attribute_Reference\n      Indicates for an associative array attribute, that the\n      index is case insensitive.\n  \n    N_Comment\n      Indicates that the comment is preceded by an empty line.\n  \n    N_Project\n      Indicates that there are comments in the project source that\n      cannot be kept in the tree.\n  \n    N_Project_Declaration\n      Indicates that there are unkept comments in the project.\n  \n    N_With_Clause\n      Indicates that this is not the last with in a with clause.\n      Set for \"A\", but not for \"B\" in with \"B\"; and with \"A\", \"B\";\n@field Flag2\n  This flag is significant only for:\n  \n    N_Project\n      Indicates that the project \"extends all\" another project.\n  \n    N_Comment\n      Indicates that the comment is followed by an empty line.\n  \n    N_With_Clause\n      Indicates that the originally imported project is an extending\n      all project.\n@field Comments",
              documentation_snippet: "type Project_Node_Record is record\n   Kind : Project_Node_Kind;\n   Qualifier : Project_Qualifier := Unspecified;\n   Location : Source_Ptr := No_Location;\n   Directory : Path_Name_Type := No_Path;\n   Display_Name : Name_Id := No_Name;\n   Expr_Kind : Variable_Kind := Undefined;\n   Variables : Variable_Node_Id := Empty_Node;\n   Packages : Package_Declaration_Id := Empty_Node;\n   Pkg_Id : Package_Node_Id := Empty_Package;\n   Name : Name_Id := No_Name;\n   Src_Index : Int := 0;\n   Path_Name : Path_Name_Type := No_Path;\n   Value : Name_Id := No_Name;\n   Default : Attribute_Default_Value := Empty_Value;\n   Field1 : Project_Node_Id := Empty_Node;\n   Field2 : Project_Node_Id := Empty_Node;\n   Field3 : Project_Node_Id := Empty_Node;\n   Field4 : Project_Node_Id := Empty_Node;\n   Flag1 : Boolean := False;\n   Flag2 : Boolean := False;\n   Comments : Project_Node_Id := Empty_Node;\nend record;",
              }          ,
          ]
,constants:           [
              {
              name: "No_Project_Name_And_Node",
              qualified_name: "Prj.Tree.Tree_Private_Part.No_Project_Name_And_Node",
              signature: "prj.tree.tree_private_part.no_project_name_and_node",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "No_Project_Name_And_Node : constant Project_Name_And_Node :=\n  (Name           => No_Name,\n   Node           => Empty_Node,\n   Resolved_Path  => No_Path,\n   Extended       => True,\n   From_Extended  => False,\n   Proj_Qualifier => Unspecified);",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Comment_Location",
       qualified_name: "Prj.Tree.Comment_Location",
       signature: "prj.tree.comment_location",
       enclosing: "",
       is_private: false,
       documentation: "Used in call to Add_Comments below\n\n@enum Before\n@enum After\n@enum Before_End\n@enum After_End\n@enum End_Of_Line",
       documentation_snippet: "type Comment_Location is\n  (Before, After, Before_End, After_End, End_Of_Line);",
       }   ,
       {
       name: "Comment_State",
       qualified_name: "Prj.Tree.Comment_State",
       signature: "prj.tree.comment_state",
       enclosing: "",
       is_private: false,
       documentation: "A type to store the values of several global variables related to\ncomments.",
       documentation_snippet: "type Comment_State is private;",
       }   ,
       {
       name: "Project_Node_Id",
       qualified_name: "Prj.Tree.Project_Node_Id",
       signature: "prj.tree.project_node_id",
       enclosing: "",
       is_private: false,
       documentation: "The index of table Tree_Private_Part.Project_Nodes",
       documentation_snippet: "type Project_Node_Id is range\n  Project_Node_Low_Bound .. Project_Node_High_Bound;",
       }   ,
       {
       name: "Project_Node_Kind",
       qualified_name: "Prj.Tree.Project_Node_Kind",
       signature: "prj.tree.project_node_kind",
       enclosing: "",
       is_private: false,
       documentation: "Each node in the tree is of a Project_Node_Kind. For the signification\nof the fields in each node of Project_Node_Kind, look at package\nTree_Private_Part.\n\n@enum N_Project\n@enum N_With_Clause\n@enum N_Project_Declaration\n@enum N_Declarative_Item\n@enum N_Package_Declaration\n@enum N_String_Type_Declaration\n@enum N_Literal_String\n@enum N_Attribute_Declaration\n@enum N_Typed_Variable_Declaration\n@enum N_Variable_Declaration\n@enum N_Expression\n@enum N_Term\n@enum N_Literal_String_List\n@enum N_Variable_Reference\n@enum N_External_Value\n@enum N_Attribute_Reference\n@enum N_Case_Construction\n@enum N_Case_Item\n@enum N_Comment_Zones\n@enum N_Comment",
       documentation_snippet: "type Project_Node_Kind is\n  (N_Project,\n   N_With_Clause,\n   N_Project_Declaration,\n   N_Declarative_Item,\n   N_Package_Declaration,\n   N_String_Type_Declaration,\n   N_Literal_String,\n   N_Attribute_Declaration,\n   N_Typed_Variable_Declaration,\n   N_Variable_Declaration,\n   N_Expression,\n   N_Term,\n   N_Literal_String_List,\n   N_Variable_Reference,\n   N_External_Value,\n   N_Attribute_Reference,\n   N_Case_Construction,\n   N_Case_Item,\n   N_Comment_Zones,\n   N_Comment);",
       }   ,
   ]
,record_types:    [
       {
       name: "Comment_Data",
       qualified_name: "Prj.Tree.Comment_Data",
       signature: "prj.tree.comment_data",
       enclosing: "",
       is_private: false,
       documentation: "Component type for Comments Table below\n\n@field Value\n@field Follows_Empty_Line\n@field Is_Followed_By_Empty_Line",
       documentation_snippet: "type Comment_Data is record\n   Value                     : Name_Id := No_Name;\n   Follows_Empty_Line        : Boolean := False;\n   Is_Followed_By_Empty_Line : Boolean := False;\nend record;",
       }   ,
       {
       name: "Environment",
       qualified_name: "Prj.Tree.Environment",
       signature: "prj.tree.environment",
       enclosing: "",
       is_private: false,
       documentation: "\n@field External\n  External references are stored in this hash table (and manipulated\n  through subprograms in prj-ext.ads). External references are\n  project-tree specific so that one can load the same tree twice but\n  have two views of it, for instance.\n@field Project_Path\n  The project path is tree specific, since we might want to load\n  simultaneously multiple projects, each with its own search path, in\n  particular when using different compilers with different default\n  search directories.\n@field Flags",
       documentation_snippet: "type Environment is record\n   External : Prj.Ext.External_References;\n   Project_Path : aliased Prj.Env.Project_Search_Path;\n   Flags : Prj.Processing_Flags;\nend record;",
       }   ,
       {
       name: "Project_Node_Tree_Data",
       qualified_name: "Prj.Tree.Project_Node_Tree_Data",
       signature: "prj.tree.project_node_tree_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Project_Node_Tree_Data is record\n   Project_Nodes : Tree_Private_Part.Project_Node_Table.Instance;\n   Projects_HT   : Tree_Private_Part.Projects_Htable.Instance;\n   Incomplete_With : Boolean := False;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Project_Node_Tree_Ref",
       qualified_name: "Prj.Tree.Project_Node_Tree_Ref",
       signature: "prj.tree.project_node_tree_ref",
       enclosing: "",
       is_private: false,
       documentation: "Type to designate a project node tree, so that several project node\ntrees can coexist in memory.",
       documentation_snippet: "type Project_Node_Tree_Ref is access all Project_Node_Tree_Data;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Package_Declaration_Id",
       qualified_name: "Prj.Tree.Package_Declaration_Id",
       signature: "prj.tree.package_declaration_id",
       enclosing: "",
       is_private: false,
       documentation: "Used to designate a node whose expected kind is N_Project_Declaration",
       documentation_snippet: "subtype Package_Declaration_Id is Project_Node_Id;",
       }   ,
       {
       name: "Variable_Node_Id",
       qualified_name: "Prj.Tree.Variable_Node_Id",
       signature: "prj.tree.variable_node_id",
       enclosing: "",
       is_private: false,
       documentation: "Used to designate a node whose expected kind is one of\nN_Typed_Variable_Declaration, N_Variable_Declaration or\nN_Variable_Reference.",
       documentation_snippet: "subtype Variable_Node_Id is Project_Node_Id;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Node",
       qualified_name: "Prj.Tree.Empty_Node",
       signature: "prj.tree.empty_node",
       enclosing: "",
       is_private: false,
       documentation: "Designates no node in table Project_Nodes",
       documentation_snippet: "Empty_Node : constant Project_Node_Id := Project_Node_Low_Bound;",
       }   ,
       {
       name: "First_Node_Id",
       qualified_name: "Prj.Tree.First_Node_Id",
       signature: "prj.tree.first_node_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "First_Node_Id : constant Project_Node_Id := Project_Node_Low_Bound + 1;",
       }   ,
       {
       name: "Project_Node_High_Bound",
       qualified_name: "Prj.Tree.Project_Node_High_Bound",
       signature: "prj.tree.project_node_high_bound",
       enclosing: "",
       is_private: false,
       documentation: "Range of values for project node id's (in practice infinite)",
       documentation_snippet: "Project_Node_High_Bound : constant := 099_999_999;",
       }   ,
       {
       name: "Project_Node_Low_Bound",
       qualified_name: "Prj.Tree.Project_Node_Low_Bound",
       signature: "prj.tree.project_node_low_bound",
       enclosing: "",
       is_private: false,
       documentation: "Range of values for project node id's (in practice infinite)",
       documentation_snippet: "Project_Node_Low_Bound  : constant := 0;",
       }   ,
       {
       name: "Project_Nodes_Increment",
       qualified_name: "Prj.Tree.Project_Nodes_Increment",
       signature: "prj.tree.project_nodes_increment",
       enclosing: "",
       is_private: false,
       documentation: "Allocation parameters for initializing and extending number\nof nodes in table Tree_Private_Part.Project_Nodes",
       documentation_snippet: "Project_Nodes_Increment : constant := 100;",
       }   ,
       {
       name: "Project_Nodes_Initial",
       qualified_name: "Prj.Tree.Project_Nodes_Initial",
       signature: "prj.tree.project_nodes_initial",
       enclosing: "",
       is_private: false,
       documentation: "Allocation parameters for initializing and extending number\nof nodes in table Tree_Private_Part.Project_Nodes",
       documentation_snippet: "Project_Nodes_Initial   : constant := 1_000;",
       }   ,
   ]
,}
---

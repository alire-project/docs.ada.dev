---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Internal.Descriptor",
qualified_name: "Langkit_Support.Internal.Descriptor",
signature: "langkit_support.internal.descriptor",
enclosing: "langkit_support.internal",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
record_types:    [
       {
       name: "Language_Descriptor",
       qualified_name: "Langkit_Support.Internal.Descriptor.Language_Descriptor",
       signature: "langkit_support.internal.descriptor.language_descriptor",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Language_Name\n  Name of the language that is analyzed (in camel-with-underscores\n  casing).\n  Descriptors for grammar rules. The table also defines the range of\n  supported rules for this language.\n@field Default_Grammar_Rule\n  Descriptors for token kinds. The table for names also defines the\n  range of supported kinds for this language.\n@field Grammar_Rules\n  Descriptors for token kinds. The table for names also defines the\n  range of supported kinds for this language.\n@field Token_Kind_Names\n  Descriptors for introspection capabilities\n@field Types\n@field Enum_Types\n@field Array_Types\n@field Iterator_Types\n@field Struct_Types\n@field Builtin_Types\n@field First_Node\n  Index of the first node descriptor in ``Struct_Types``. In\n  ``Struct_Types``, descriptors from 1 to ``First_Node - 1`` are struct\n  types (not nodes), and descriptors from ``First_Node`` to\n  ``Struct_Types'Last`` are nodes.\n@field Struct_Members\n  Descriptors for struct members: fields and properties. In\n  ``Struct_Members``, descriptors from 1 to ``First_Property - 1`` are\n  fields, and descriptors from ``First_Property`` to\n  ``Struct_Members'Last`` are properties.\n@field First_Property\n  Index of the first property descriptor in ``Struct_Members``\n  Implementation for generic operations\n@field Create_Context\n@field Context_Inc_Ref\n@field Context_Dec_Ref\n@field Context_Version\n@field Context_Get_From_File\n@field Context_Has_Unit\n@field Unit_Context\n@field Unit_Version\n@field Unit_Filename\n@field Unit_Root\n@field Unit_First_Token\n@field Unit_Last_Token\n@field Unit_Get_Line\n@field Node_Metadata_Inc_Ref\n@field Node_Metadata_Dec_Ref\n@field Node_Unit\n@field Node_Kind\n@field Node_Parent\n@field Node_Parents\n@field Node_Children_Count\n@field Node_Get_Child\n@field Node_Fetch_Sibling\n@field Node_Is_Ghost\n@field Node_Token_Start\n@field Node_Token_End\n@field Node_Text\n@field Node_Sloc_Range\n@field Node_Last_Attempted_Child\n@field Entity_Image\n@field Token_Is_Equivalent\n  Operations to build/inspect generic data types\n@field Create_Enum\n@field Create_Array\n@field Create_Struct\n@field Eval_Node_Member",
       documentation_snippet: "type Language_Descriptor is limited record\n   Language_Name : Text_Access;\n   Default_Grammar_Rule : Grammar_Rule_Index;\n   Grammar_Rules        : Grammar_Rule_Descriptor_Array_Access;\n   Token_Kind_Names : Token_Kind_Name_Array_Access;\n   Types          : Type_Descriptor_Array_Access;\n   Enum_Types     : Enum_Type_Descriptor_Array_Access;\n   Array_Types    : Array_Type_Descriptor_Array_Access;\n   Iterator_Types : Iterator_Type_Descriptor_Array_Access;\n   Struct_Types   : Struct_Type_Descriptor_Array_Access;\n   Builtin_Types  : Builtin_Types_Access;\n   First_Node : Type_Index;\n   Struct_Members : Struct_Member_Descriptor_Array_Access;\n   First_Property : Struct_Member_Index;\n   Create_Context        : Create_Context_Type;\n   Context_Inc_Ref       : Context_Inc_Ref_Type;\n   Context_Dec_Ref       : Context_Dec_Ref_Type;\n   Context_Version       : Context_Version_Type;\n   Context_Get_From_File : Context_Get_From_File_Type;\n   Context_Has_Unit      : Context_Has_Unit_Type;\n   Unit_Context     : Unit_Context_Type;\n   Unit_Version     : Unit_Version_Type;\n   Unit_Filename    : Unit_Filename_Type;\n   Unit_Root        : Unit_Root_Type;\n   Unit_First_Token : Unit_Token_Getter_Type;\n   Unit_Last_Token  : Unit_Token_Getter_Type;\n   Unit_Get_Line    : Unit_Get_Line_Type;\n   Node_Metadata_Inc_Ref : Node_Metadata_Inc_Ref_Type;\n   Node_Metadata_Dec_Ref : Node_Metadata_Dec_Ref_Type;\n   Node_Unit                 : Node_Unit_Type;\n   Node_Kind                 : Node_Kind_Type;\n   Node_Parent               : Node_Parent_Type;\n   Node_Parents              : Node_Parents_Type;\n   Node_Children_Count       : Node_Children_Count_Type;\n   Node_Get_Child            : Node_Get_Child_Type;\n   Node_Fetch_Sibling        : Node_Fetch_Sibling_Type;\n   Node_Is_Ghost             : Node_Is_Ghost_Type;\n   Node_Token_Start          : Node_Token_Getter_Type;\n   Node_Token_End            : Node_Token_Getter_Type;\n   Node_Text                 : Node_Text_Type;\n   Node_Sloc_Range           : Node_Sloc_Range_Type;\n   Node_Last_Attempted_Child : Node_Last_Attempted_Child_Type;\n   Entity_Image : Entity_Image_Type;\n   Token_Is_Equivalent : Token_Is_Equivalent_Type;\n   Create_Enum      : Create_Enum_Type;\n   Create_Array     : Create_Array_Type;\n   Create_Struct    : Create_Struct_Type;\n   Eval_Node_Member : Eval_Node_Member_Type;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Context_Dec_Ref_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Context_Dec_Ref_Type",
       signature: "langkit_support.internal.descriptor.context_dec_ref_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Dec_Ref_Type is access procedure\n  (Context : in out Internal_Context);",
       }   ,
       {
       name: "Context_Get_From_File_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Context_Get_From_File_Type",
       signature: "langkit_support.internal.descriptor.context_get_from_file_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Get_From_File_Type is access function\n  (Context           : Internal_Context;\n   Filename, Charset : String;\n   Reparse           : Boolean;\n   Rule              : Grammar_Rule_Index) return Internal_Unit;",
       }   ,
       {
       name: "Context_Has_Unit_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Context_Has_Unit_Type",
       signature: "langkit_support.internal.descriptor.context_has_unit_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Has_Unit_Type is access function\n  (Context : Internal_Context; Unit_Filename : String) return Boolean;",
       }   ,
       {
       name: "Context_Inc_Ref_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Context_Inc_Ref_Type",
       signature: "langkit_support.internal.descriptor.context_inc_ref_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Inc_Ref_Type is access procedure (Context : Internal_Context);",
       }   ,
       {
       name: "Context_Version_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Context_Version_Type",
       signature: "langkit_support.internal.descriptor.context_version_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Version_Type is access function\n  (Context : Internal_Context) return Version_Number;",
       }   ,
       {
       name: "Create_Array_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Create_Array_Type",
       signature: "langkit_support.internal.descriptor.create_array_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Array_Type is access function\n  (Array_Type : Type_Index;\n   Values     : Internal_Value_Array) return Internal_Value_Access;",
       }   ,
       {
       name: "Create_Context_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Create_Context_Type",
       signature: "langkit_support.internal.descriptor.create_context_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Context_Type is access function\n  (Charset     : String := \"\";\n   File_Reader : File_Reader_Reference := No_File_Reader_Reference;\n   With_Trivia : Boolean := True;\n   Tab_Stop    : Natural := 0)\n   return Internal_Context;",
       }   ,
       {
       name: "Create_Enum_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Create_Enum_Type",
       signature: "langkit_support.internal.descriptor.create_enum_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Enum_Type is access function\n  (Enum_Type   : Type_Index;\n   Value_Index : Enum_Value_Index) return Internal_Value_Access;",
       }   ,
       {
       name: "Create_Struct_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Create_Struct_Type",
       signature: "langkit_support.internal.descriptor.create_struct_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Struct_Type is access function\n  (Struct_Type : Type_Index;\n   Values      : Internal_Value_Array) return Internal_Value_Access;",
       }   ,
       {
       name: "Entity_Image_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Entity_Image_Type",
       signature: "langkit_support.internal.descriptor.entity_image_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Entity_Image_Type is access function\n  (Entity : Internal_Entity) return String;",
       }   ,
       {
       name: "Eval_Node_Member_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Eval_Node_Member_Type",
       signature: "langkit_support.internal.descriptor.eval_node_member_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Eval_Node_Member_Type is access function\n  (Node      : Internal_Acc_Node;\n   Member    : Struct_Member_Index;\n   Arguments : Internal_Value_Array) return Internal_Value_Access;",
       }   ,
       {
       name: "Language_Descriptor_Access",
       qualified_name: "Langkit_Support.Internal.Descriptor.Language_Descriptor_Access",
       signature: "langkit_support.internal.descriptor.language_descriptor_access",
       enclosing: "",
       is_private: false,
       documentation: "Unique identifier for Langkit-generated libraries and dispatch table for\nall generic operations.",
       documentation_snippet: "type Language_Descriptor_Access is access constant Language_Descriptor;",
       }   ,
       {
       name: "Node_Children_Count_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Children_Count_Type",
       signature: "langkit_support.internal.descriptor.node_children_count_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Children_Count_Type is access function\n  (Node : Analysis.Internal_Node) return Natural;",
       }   ,
       {
       name: "Node_Fetch_Sibling_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Fetch_Sibling_Type",
       signature: "langkit_support.internal.descriptor.node_fetch_sibling_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Fetch_Sibling_Type is access function\n  (Node   : Analysis.Internal_Node;\n   Offset : Integer) return Analysis.Internal_Node;",
       }   ,
       {
       name: "Node_Get_Child_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Get_Child_Type",
       signature: "langkit_support.internal.descriptor.node_get_child_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Get_Child_Type is access procedure\n  (Node            : Analysis.Internal_Node;\n   Index           : Positive;\n   Index_In_Bounds : out Boolean;\n   Result          : out Analysis.Internal_Node);",
       }   ,
       {
       name: "Node_Is_Ghost_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Is_Ghost_Type",
       signature: "langkit_support.internal.descriptor.node_is_ghost_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Is_Ghost_Type is access function\n  (Node : Analysis.Internal_Node) return Boolean;",
       }   ,
       {
       name: "Node_Kind_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Kind_Type",
       signature: "langkit_support.internal.descriptor.node_kind_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Kind_Type is access function\n  (Node : Analysis.Internal_Node) return Type_Index;",
       }   ,
       {
       name: "Node_Last_Attempted_Child_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Last_Attempted_Child_Type",
       signature: "langkit_support.internal.descriptor.node_last_attempted_child_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Last_Attempted_Child_Type is access function\n  (Node : Analysis.Internal_Node) return Integer;",
       }   ,
       {
       name: "Node_Metadata_Dec_Ref_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Metadata_Dec_Ref_Type",
       signature: "langkit_support.internal.descriptor.node_metadata_dec_ref_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Metadata_Dec_Ref_Type is access procedure\n  (Metadata : in out Internal_Node_Metadata);",
       }   ,
       {
       name: "Node_Metadata_Inc_Ref_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Metadata_Inc_Ref_Type",
       signature: "langkit_support.internal.descriptor.node_metadata_inc_ref_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Metadata_Inc_Ref_Type is access procedure\n  (Metadata : Internal_Node_Metadata);",
       }   ,
       {
       name: "Node_Parent_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Parent_Type",
       signature: "langkit_support.internal.descriptor.node_parent_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Parent_Type is access function\n  (Node : Analysis.Internal_Entity) return Analysis.Internal_Entity;",
       }   ,
       {
       name: "Node_Parents_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Parents_Type",
       signature: "langkit_support.internal.descriptor.node_parents_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Parents_Type is access function\n  (Node      : Analysis.Internal_Entity;\n   With_Self : Boolean) return Analysis.Internal_Entity_Array;",
       }   ,
       {
       name: "Node_Sloc_Range_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Sloc_Range_Type",
       signature: "langkit_support.internal.descriptor.node_sloc_range_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Sloc_Range_Type is access function\n  (Node : Analysis.Internal_Node) return Source_Location_Range;",
       }   ,
       {
       name: "Node_Text_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Text_Type",
       signature: "langkit_support.internal.descriptor.node_text_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Text_Type is access function\n  (Node : Analysis.Internal_Node) return Text_Type;",
       }   ,
       {
       name: "Node_Token_Getter_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Token_Getter_Type",
       signature: "langkit_support.internal.descriptor.node_token_getter_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Token_Getter_Type is access function\n  (Node : Analysis.Internal_Node) return Analysis.Internal_Token;",
       }   ,
       {
       name: "Node_Unit_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Node_Unit_Type",
       signature: "langkit_support.internal.descriptor.node_unit_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Unit_Type is access function\n  (Node : Analysis.Internal_Node) return Internal_Unit;",
       }   ,
       {
       name: "Token_Is_Equivalent_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Token_Is_Equivalent_Type",
       signature: "langkit_support.internal.descriptor.token_is_equivalent_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Token_Is_Equivalent_Type is access function\n  (Left, Right       : Internal_Token;\n   Left_SN, Right_SN : Token_Safety_Net) return Boolean;",
       }   ,
       {
       name: "Unit_Context_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Context_Type",
       signature: "langkit_support.internal.descriptor.unit_context_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Context_Type is access function\n  (Unit : Internal_Unit) return Internal_Context;",
       }   ,
       {
       name: "Unit_Filename_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Filename_Type",
       signature: "langkit_support.internal.descriptor.unit_filename_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Filename_Type is access function\n  (Unit : Internal_Unit) return String;",
       }   ,
       {
       name: "Unit_Get_Line_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Get_Line_Type",
       signature: "langkit_support.internal.descriptor.unit_get_line_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Get_Line_Type is access function\n  (Unit : Internal_Unit; Line_Number : Positive) return Text_Type;",
       }   ,
       {
       name: "Unit_Root_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Root_Type",
       signature: "langkit_support.internal.descriptor.unit_root_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Root_Type is access function\n  (Unit : Internal_Unit) return Analysis.Internal_Node;",
       }   ,
       {
       name: "Unit_Token_Getter_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Token_Getter_Type",
       signature: "langkit_support.internal.descriptor.unit_token_getter_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Token_Getter_Type is access function\n  (Unit : Internal_Unit) return Analysis.Internal_Token;",
       }   ,
       {
       name: "Unit_Version_Type",
       qualified_name: "Langkit_Support.Internal.Descriptor.Unit_Version_Type",
       signature: "langkit_support.internal.descriptor.unit_version_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Version_Type is access function\n  (Unit : Internal_Unit) return Version_Number;",
       }   ,
   ]
,}
---

---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Table",
qualified_name: "Table",
signature: "table",
enclosing: "",
is_private: false,
documentation: "Note that this interface should remain synchronized with those in\nGNAT.Table and GNAT.Dynamic_Tables to keep coherency between these\nthree related units.",
documentation_snippet: "",
packages:    [
       {
       name: "Table",
       qualified_name: "Table.Table",
       signature: "table.table",
       enclosing: "table",
       is_private: false,
       documentation: "Table_Component_Type and Table_Index_Type specify the type of the\narray, Table_Low_Bound is the lower bound. Index_type must be an\ninteger type. The effect is roughly to declare:\n\n@formal Table_Component_Type\n@formal Table_Index_Type\n@formal Table_Low_Bound\n@formal Table_Initial\n@formal Table_Increment\n@formal Table_Name",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Saved_Table",
              qualified_name: "Table.Table.Saved_Table",
              signature: "table.table.saved_table",
              enclosing: "",
              is_private: false,
              documentation: "Type used for Save/Restore subprograms",
              documentation_snippet: "type Saved_Table is private;",
              }          ,
          ]
,array_types:           [
              {
              name: "Table_Type",
              qualified_name: "Table.Table.Table_Type",
              signature: "table.table.table_type",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Table_Type is\n  array (Table_Index_Type range <>) of Table_Component_Type;",
              }          ,
          ]
,access_types:           [
              {
              name: "Table_Ptr",
              qualified_name: "Table.Table.Table_Ptr",
              signature: "table.table.table_ptr",
              enclosing: "",
              is_private: false,
              documentation: "The table is actually represented as a pointer to allow reallocation",
              documentation_snippet: "type Table_Ptr is access all Big_Table_Type;",
              }          ,
          ]
,subtypes:           [
              {
              name: "Big_Table_Type",
              qualified_name: "Table.Table.Big_Table_Type",
              signature: "table.table.big_table_type",
              enclosing: "",
              is_private: false,
              documentation: "We work with pointers to a bogus array type that is constrained\nwith the maximum possible range bound. This means that the pointer\nis a thin pointer, which is more efficient. Since subscript checks\nin any case must be on the logical, rather than physical bounds,\nsafety is not compromised by this approach.",
              documentation_snippet: "subtype Big_Table_Type is\n  Table_Type (Table_Low_Bound .. Table_Index_Type'Last);",
              }          ,
          ]
,constants:           [
              {
              name: "First",
              qualified_name: "Table.Table.First",
              signature: "table.table.first",
              enclosing: "",
              is_private: false,
              documentation: "Export First as synonym for Low_Bound (parallel with use of Last)",
              documentation_snippet: "First : constant Table_Index_Type := Table_Low_Bound;",
              }          ,
          ]
,variables:           [
              {
              name: "Locked",
              qualified_name: "Table.Table.Locked",
              signature: "table.table.locked",
              enclosing: "",
              is_private: false,
              documentation: "Table expansion is permitted only if this switch is set to False. A\nclient may set Locked to True, in which case any attempt to expand\nthe table will cause an assertion failure. Note that while a table\nis locked, its address in memory remains fixed and unchanging. This\nfeature is used to control table expansion during Gigi processing.\nGigi assumes that tables other than the Uint and Ureal tables do\nnot move during processing, which means that they cannot be expanded.\nThe Locked flag is used to enforce this restriction.",
              documentation_snippet: "Locked : Boolean := False;",
              }          ,
              {
              name: "Table",
              qualified_name: "Table.Table.Table",
              signature: "table.table.table",
              enclosing: "",
              is_private: false,
              documentation: "The table itself. The lower bound is the value of Low_Bound.\nLogically the upper bound is the current value of Last (although\nthe actual size of the allocated table may be larger than this).\nThe program may only access and modify Table entries in the range\nFirst .. Last.",
              documentation_snippet: "Table : aliased Table_Ptr := null;",
              }          ,
          ]
,       }   ,
   ]
,}
---

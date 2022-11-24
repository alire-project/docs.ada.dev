---
crate: adabots
layout: gnatdoc
gnatdoc: {
name: "Adabots",
qualified_name: "Adabots",
signature: "adabots",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Material",
       qualified_name: "Adabots.Material",
       signature: "adabots.material",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Material is\n  (Grass, Planks, Air, Glass, Ice, Gold_Block, Sand, Bedrock, Stone);",
       }   ,
       {
       name: "Stack_Count",
       qualified_name: "Adabots.Stack_Count",
       signature: "adabots.stack_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stack_Count is range 0 .. 64;",
       }   ,
       {
       name: "Turtle_Inventory_Slot",
       qualified_name: "Adabots.Turtle_Inventory_Slot",
       signature: "adabots.turtle_inventory_slot",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Turtle_Inventory_Slot is range 1 .. 16;",
       }   ,
   ]
,record_types:    [
       {
       name: "Absolute_Location",
       qualified_name: "Adabots.Absolute_Location",
       signature: "adabots.absolute_location",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Absolute_Location is record\n   X : Integer := 0;\n   Y : Integer := 0;\n   Z : Integer := 0;\nend record;",
       }   ,
       {
       name: "Item_Detail",
       qualified_name: "Adabots.Item_Detail",
       signature: "adabots.item_detail",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item_Detail is record\n   Count : Stack_Count;\n   Name  : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
       {
       name: "Relative_Location",
       qualified_name: "Adabots.Relative_Location",
       signature: "adabots.relative_location",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Relative_Location is record\n   X_Offset : Integer := 0;\n   Y_Offset : Integer := 0;\n   Z_Offset : Integer := 0;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Command_Computer",
       qualified_name: "Adabots.Command_Computer",
       signature: "adabots.command_computer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Computer is\n  new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Turtle",
       qualified_name: "Adabots.Turtle",
       signature: "adabots.turtle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Turtle is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Port",
       qualified_name: "Adabots.Default_Port",
       signature: "adabots.default_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Port : constant := 7_112;",
       }   ,
   ]
,}
---

---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.View.Grid",
qualified_name: "Gnoga.Gui.View.Grid",
signature: "gnoga.gui.view.grid",
enclosing: "gnoga.gui.view",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Grid_View_Types\n-----------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Grid_Element_Type",
       qualified_name: "Gnoga.Gui.View.Grid.Grid_Element_Type",
       signature: "gnoga.gui.view.grid.grid_element_type",
       enclosing: "",
       is_private: false,
       documentation: "COL = A single column\nSPN = Span previous column through this column\n\n@enum COL\n@enum SPN",
       documentation_snippet: "type Grid_Element_Type is (COL, SPN);",
       }   ,
   ]
,array_types:    [
       {
       name: "Grid_Rows_Type",
       qualified_name: "Gnoga.Gui.View.Grid.Grid_Rows_Type",
       signature: "gnoga.gui.view.grid.grid_rows_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grid_Rows_Type is array (Positive range <>, Positive range <>) of Grid_Element_Type;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Grid_View_Type",
       qualified_name: "Gnoga.Gui.View.Grid.Grid_View_Type",
       signature: "gnoga.gui.view.grid.grid_view_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grid_View_Type is new View_Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Grid_View_Access",
       qualified_name: "Gnoga.Gui.View.Grid.Grid_View_Access",
       signature: "gnoga.gui.view.grid.grid_view_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grid_View_Access is access all Grid_View_Type;",
       }   ,
       {
       name: "Pointer_To_Grid_View_Class",
       qualified_name: "Gnoga.Gui.View.Grid.Pointer_To_Grid_View_Class",
       signature: "gnoga.gui.view.grid.pointer_to_grid_view_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Grid_View_Class is access all Grid_View_Type'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "Horizontal_Split",
       qualified_name: "Gnoga.Gui.View.Grid.Horizontal_Split",
       signature: "gnoga.gui.view.grid.horizontal_split",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Horizontal_Split : constant Grid_Rows_Type := (1 => (COL, COL));",
       }   ,
       {
       name: "Vertical_Split",
       qualified_name: "Gnoga.Gui.View.Grid.Vertical_Split",
       signature: "gnoga.gui.view.grid.vertical_split",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Vertical_Split   : constant Grid_Rows_Type := ((1 => COL), (1 => COL));",
       }   ,
   ]
,}
---

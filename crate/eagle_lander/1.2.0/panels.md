---
crate: eagle_lander
layout: gnatdoc
gnatdoc: {
name: "Panels",
qualified_name: "Panels",
signature: "panels",
enclosing: "",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n                                                                           --\n                               Eagle Lander                                --\n                                                                           --\n         Copyright (C) 2015 Fabien Chouteau (chouteau@adacore.com)         --\n                                                                           --\n    Eagle Lander is free software: you can redistribute it and/or modify   --\n    it under the terms of the GNU General Public License as published by   --\n    the Free Software Foundation, either version 3 of the License, or      --\n    (at your option) any later version.                                    --\n                                                                           --\n    Foobar is distributed in the hope that it will be useful,              --\n    but WITHOUT ANY WARRANTY; without even the implied warranty of         --\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          --\n    GNU General Public License for more details.                           --\n                                                                           --\n    You should have received a copy of the GNU General Public License      --\n    along with Eagle Lander.  If not, see <http://www.gnu.org/licenses/>.  --\n                                                                           --\n-----------------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Angle_Array",
       qualified_name: "Panels.Angle_Array",
       signature: "panels.angle_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Angle_Array is array (1 .. 4) of Gdouble;",
       }   ,
   ]
,record_types:    [
       {
       name: "Panel",
       qualified_name: "Panels.Panel",
       signature: "panels.panel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Panel is abstract tagged record\n   Pos               : Vector2D;\n   Size              : Vector2D;\n   Scale             : Gdouble := 1.0;\n   Clicked           : Boolean;\n   Resized           : Boolean;\n   Click_Pos         : Vector2D;\n   Frame_Initialized : Boolean;\n   Screws_Angle      : Angle_Array;\n   Inner_Frame_Pos   : Vector2D;\n   Inner_Frame_Size  : Vector2D;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Gauge",
       qualified_name: "Panels.Gauge",
       signature: "panels.gauge",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Gauge is new Panel with record\n   Text : String_Access := new String'(\"N/A\");\nend record;",
       }   ,
       {
       name: "Xpointer",
       qualified_name: "Panels.Xpointer",
       signature: "panels.xpointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Xpointer is new Panel with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Panel_Access",
       qualified_name: "Panels.Panel_Access",
       signature: "panels.panel_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Panel_Access is not null access all Panel'Class;",
       }   ,
   ]
,}
---

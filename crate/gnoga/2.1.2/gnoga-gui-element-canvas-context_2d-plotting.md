---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting",
qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting",
signature: "gnoga.gui.element.canvas.context_2d.plotting",
enclosing: "gnoga.gui.element.canvas.context_2d",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                   GNOGA - The GNU Omnificent GUI for Ada                 --\n                                                                          --\n   G N O G A . G U I . E L E M E N T . C A N V A S . C O N T E X T _ 2 D  --\n                               P L O T T I N G                            --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                     Copyright (C) 2016 Jeffrey Carter                    --\n                                                                          --\n  This library is free software;  you can redistribute it and/or modify   --\n  it under terms of the  GNU General Public License  as published by the  --\n  Free Software  Foundation;  either version 3,  or (at your  option) any --\n  later version. This library is distributed in the hope that it will be  --\n  useful, but WITHOUT ANY WARRANTY;  without even the implied warranty of --\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    --\n                                                                          --\n  As a special exception under Section 7 of GPL version 3, you are        --\n  granted additional permissions described in the GCC Runtime Library     --\n  Exception, version 3.1, as published by the Free Software Foundation.   --\n                                                                          --\n  You should have received a copy of the GNU General Public License and   --\n  a copy of the GCC Runtime Library Exception along with this program;    --\n  see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see   --\n  <http://www.gnu.org/licenses/>.                                         --\n                                                                          --\n  As a special exception, if other files instantiate generics from this   --\n  unit, or you link this unit with other files to produce an executable,  --\n  this  unit  does not  by itself cause  the resulting executable to be   --\n  covered by the GNU General Public License. This exception does not      --\n  however invalidate any other reasons why the executable file might be   --\n  covered by the  GNU Public License.                                     --\n                                                                          --\n  For more information please go to http://www.gnoga.com                  --\n----------------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Point_List",
       qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting.Point_List",
       signature: "gnoga.gui.element.canvas.context_2d.plotting.point_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point_List is array (Positive range <>) of Plot_Point;",
       }   ,
   ]
,record_types:    [
       {
       name: "Plot_Point",
       qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting.Plot_Point",
       signature: "gnoga.gui.element.canvas.context_2d.plotting.plot_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plot_Point is record\n   X : Float;\n   Y : Float;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Plot_Info",
       qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting.Plot_Info",
       signature: "gnoga.gui.element.canvas.context_2d.plotting.plot_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plot_Info is new Canvas_Type with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Positive_Float",
       qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting.Positive_Float",
       signature: "gnoga.gui.element.canvas.context_2d.plotting.positive_float",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Positive_Float is Float range Float'Succ (0.0) .. Float'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Black",
       qualified_name: "Gnoga.Gui.Element.Canvas.Context_2D.Plotting.Black",
       signature: "gnoga.gui.element.canvas.context_2d.plotting.black",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Black : constant Gnoga.Types.RGBA_Type := (others => <>);",
       }   ,
   ]
,}
---

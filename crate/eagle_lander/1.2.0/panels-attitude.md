---
crate: eagle_lander
layout: gnatdoc
gnatdoc: {
name: "Panels.Attitude",
qualified_name: "Panels.Attitude",
signature: "panels.attitude",
enclosing: "panels",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n                                                                           --\n                               Eagle Lander                                --\n                                                                           --\n         Copyright (C) 2015 Fabien Chouteau (chouteau@adacore.com)         --\n                                                                           --\n    Eagle Lander is free software: you can redistribute it and/or modify   --\n    it under the terms of the GNU General Public License as published by   --\n    the Free Software Foundation, either version 3 of the License, or      --\n    (at your option) any later version.                                    --\n                                                                           --\n    Eagle Lander is distributed in the hope that it will be useful,        --\n    but WITHOUT ANY WARRANTY; without even the implied warranty of         --\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          --\n    GNU General Public License for more details.                           --\n                                                                           --\n    You should have received a copy of the GNU General Public License      --\n    along with Eagle Lander.  If not, see <http://www.gnu.org/licenses/>.  --\n                                                                           --\n-----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Attitude_Indicator",
       qualified_name: "Panels.Attitude.Attitude_Indicator",
       signature: "panels.attitude.attitude_indicator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attitude_Indicator is new Panel with record\n   Background  : Cairo_Surface;\n   Ball        : Cairo_Surface;\n   Initialized : Boolean := False;\nend record;",
       }   ,
   ]
,}
---

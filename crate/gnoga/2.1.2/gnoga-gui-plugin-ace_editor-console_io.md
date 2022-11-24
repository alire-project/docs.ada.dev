---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO",
qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO",
signature: "gnoga.gui.plugin.ace_editor.console_io",
enclosing: "gnoga.gui.plugin.ace_editor",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                   GNOGA - The GNU Omnificent GUI for Ada                 --\n                                                                          --\n           G N O G A . G U I . P L U G I N . A C E _ E D I T O R .        --\n                            C O N S O L E _ I O                           --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                     Copyright (C) 2017 Pascal Pignard                    --\n                                                                          --\n  This library is free software;  you can redistribute it and/or modify   --\n  it under terms of the  GNU General Public License  as published by the  --\n  Free Software  Foundation;  either version 3,  or (at your  option) any --\n  later version. This library is distributed in the hope that it will be  --\n  useful, but WITHOUT ANY WARRANTY;  without even the implied warranty of --\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    --\n                                                                          --\n  As a special exception under Section 7 of GPL version 3, you are        --\n  granted additional permissions described in the GCC Runtime Library     --\n  Exception, version 3.1, as published by the Free Software Foundation.   --\n                                                                          --\n  You should have received a copy of the GNU General Public License and   --\n  a copy of the GCC Runtime Library Exception along with this program;    --\n  see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see   --\n  <http://www.gnu.org/licenses/>.                                         --\n                                                                          --\n  As a special exception, if other files instantiate generics from this   --\n  unit, or you link this unit with other files to produce an executable,  --\n  this  unit  does not  by itself cause  the resulting executable to be   --\n  covered by the GNU General Public License. This exception does not      --\n  however invalidate any other reasons why the executable file might be   --\n  covered by the  GNU Public License.                                     --\n                                                                          --\n  For more information please go to http://www.gnoga.com                  --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Console_IO_Type",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Console_IO_Type",
       signature: "gnoga.gui.plugin.ace_editor.console_io.console_io_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Console_IO_Type is new Ace_Editor_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Console_IO_Access",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Console_IO_Access",
       signature: "gnoga.gui.plugin.ace_editor.console_io.console_io_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Console_IO_Access is access all Console_IO_Type;",
       }   ,
       {
       name: "Pointer_To_Console_IO_Class",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Pointer_To_Console_IO_Class",
       signature: "gnoga.gui.plugin.ace_editor.console_io.pointer_to_console_io_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Console_IO_Class is access all Console_IO_Type'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Count",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Count",
       signature: "gnoga.gui.plugin.ace_editor.console_io.count",
       enclosing: "",
       is_private: false,
       documentation: "Line and page length",
       documentation_snippet: "subtype Count is Natural range 0 .. Natural'Last;",
       }   ,
       {
       name: "Positive_Count",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Positive_Count",
       signature: "gnoga.gui.plugin.ace_editor.console_io.positive_count",
       enclosing: "",
       is_private: false,
       documentation: "Line and page length",
       documentation_snippet: "subtype Positive_Count is Count range 1 .. Count'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Unbounded",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Console_IO.Unbounded",
       signature: "gnoga.gui.plugin.ace_editor.console_io.unbounded",
       enclosing: "",
       is_private: false,
       documentation: "Line and page length",
       documentation_snippet: "Unbounded : constant Count := 0;",
       }   ,
   ]
,}
---

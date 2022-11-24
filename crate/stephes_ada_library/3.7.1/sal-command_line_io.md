---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Command_Line_IO",
qualified_name: "SAL.Command_Line_IO",
signature: "sal.command_line_io",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nProvide generic routines for reading parameters from the command line.\n\nEach Get_* procedure reads a particular parameter type from\nCommand_Line.Argument(Next_Arg) and then increments Next_Arg by\none. PARAMETER_ERROR is raised for *any* error, after putting an\nappropriate message to Standard_Error.\n\nCopyright (C) 1996 - 1997, 2008, 2009, 2015 Stephen Leake.  All Rights Reserved.\n\nSAL is free software; you can redistribute it and/or modify it\nunder terms of the GNU General Public License as published by the\nFree Software Foundation; either version 3, or (at your option) any\nlater version. SAL is distributed in the hope that it will be\nuseful, but WITHOUT ANY WARRANTY; without even the implied warranty\nof MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details. You should have received a\ncopy of the GNU General Public License distributed with SAL; see\nfile COPYING. If not, write to the Free Software Foundation, 59\nTemple Place - Suite 330, Boston, MA 02111-1307, USA.\n\nAs a special exception, if other files instantiate generics from\nSAL, or you link SAL object files with other files to produce\nan executable, that does not by itself cause the resulting\nexecutable to be covered by the GNU General Public License. This\nexception does not however invalidate any other reasons why the\nexecutable file might be covered by the GNU Public License.",
documentation_snippet: "",
}
---

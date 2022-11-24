---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Inputs.Mice.Cursors",
qualified_name: "SDL.Inputs.Mice.Cursors",
signature: "sdl.inputs.mice.cursors",
enclosing: "sdl.inputs.mice",
is_private: false,
documentation: "Don't confuse this package with any type of Ada iterator, this is for visual mouse cursors.",
documentation_snippet: "",
simple_types:    [
       {
       name: "System_Cursors",
       qualified_name: "SDL.Inputs.Mice.Cursors.System_Cursors",
       signature: "sdl.inputs.mice.cursors.system_cursors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type System_Cursors is\n  (Arrow,\n   I_Beam,\n   Wait,\n   Cross_Hair,\n   Wait_Arrow,\n   Size_NWSE,\n   Size_NESW,\n   Size_WE,\n   size_NS,\n   Size_All,\n   No,\n   Hand) with\n  Convention => C;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cursor",
       qualified_name: "SDL.Inputs.Mice.Cursors.Cursor",
       signature: "sdl.inputs.mice.cursors.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,}
---

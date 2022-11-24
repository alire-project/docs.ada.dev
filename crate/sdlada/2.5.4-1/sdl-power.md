---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Power",
qualified_name: "SDL.Power",
signature: "sdl.power",
enclosing: "sdl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Percentage",
       qualified_name: "SDL.Power.Percentage",
       signature: "sdl.power.percentage",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Percentage is range 0 .. 100;",
       }   ,
       {
       name: "Seconds",
       qualified_name: "SDL.Power.Seconds",
       signature: "sdl.power.seconds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Seconds is range 0 .. Integer'Last;",
       }   ,
       {
       name: "State",
       qualified_name: "SDL.Power.State",
       signature: "sdl.power.state",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Unknown\n  Cannot determine power status.\n@enum Battery\n  Not plugged in, running on the battery.\n@enum No_Battery\n  Plugged in, no battery available.\n@enum Charging\n  Plugged in, charging battery.\n@enum Charged\n  Plugged in, battery charged.",
       documentation_snippet: "type State is\n  (Unknown,\n   Battery,\n   No_Battery,\n   Charging,\n   Charged\n  ) with\n    Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Battery_Info",
       qualified_name: "SDL.Power.Battery_Info",
       signature: "sdl.power.battery_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Battery_Info is\n   record\n      Power_State      : State;\n      Time_Valid       : Boolean;\n      Time             : Seconds;\n      Percentage_Valid : Boolean;\n      Percent          : Percentage;\n   end record;",
       }   ,
   ]
,}
---

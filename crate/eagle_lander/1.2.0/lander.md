---
crate: eagle_lander
layout: gnatdoc
gnatdoc: {
name: "Lander",
qualified_name: "Lander",
signature: "lander",
enclosing: "",
is_private: false,
documentation: "For landing envolope, see:\nAn Analysis and a Historical Review\nof the Apollo Program\nLunar Module Touchdown Dynamics",
documentation_snippet: "",
simple_types:    [
       {
       name: "Result_Type",
       qualified_name: "Lander.Result_Type",
       signature: "lander.result_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Result_Type is (Crash, Out_Of_Bounds, Sucess, Not_Done_Yet);",
       }   ,
   ]
,record_types:    [
       {
       name: "Ending_Situation",
       qualified_name: "Lander.Ending_Situation",
       signature: "lander.ending_situation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ending_Situation is record\n   Situ    : Lander_Situation;\n   Result  : Result_Type := Not_Done_Yet;\n   Message : Unbounded_String := Null_Unbounded_String;\n   Points  : Natural;\nend record;",
       }   ,
       {
       name: "Lander_Situation",
       qualified_name: "Lander.Lander_Situation",
       signature: "lander.lander_situation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lander_Situation is record\n   Pos     : Position;\n   Vel     : Speed_Vect;\n   Pitch   : Angle := 0.0;\n   Pitch_R : Angular_Velocity := Angular_Velocity (0.0);\n   DPS_Throttle       : Dimentionless := 0.0;\n   Left_RCS_Throttle  : Dimentionless := 0.0;\n   Right_RCS_Throttle : Dimentionless := 0.0;\n   RCS_Propellent_Mass  : Mass  := 633.0 * kg;\n   DPS_Propellent_Mass  : Mass  := 8_874.2 * kg;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Safe_Landing_Pitch",
       qualified_name: "Lander.Safe_Landing_Pitch",
       signature: "lander.safe_landing_pitch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Safe_Landing_Pitch : constant Angle := Ada.Numerics.Pi / 6.0;",
       }   ,
       {
       name: "Safe_Landing_Vel",
       qualified_name: "Lander.Safe_Landing_Vel",
       signature: "lander.safe_landing_vel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Safe_Landing_Vel : constant Speed_Vect := (Speed (1.2), Speed (2.1));",
       }   ,
   ]
,}
---

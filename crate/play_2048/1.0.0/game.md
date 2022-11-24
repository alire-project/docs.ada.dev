---
crate: play_2048
layout: gnatdoc
gnatdoc: {
name: "Game",
qualified_name: "Game",
signature: "game",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "t_Direction",
       qualified_name: "Game.t_Direction",
       signature: "game.t_direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_Direction is (Up, Down, Right, Left);",
       }   ,
       {
       name: "t_Game_Status",
       qualified_name: "Game.t_Game_Status",
       signature: "game.t_game_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_Game_Status is (Playing, Won, Lost);",
       }   ,
   ]
,array_types:    [
       {
       name: "t_Board",
       qualified_name: "Game.t_Board",
       signature: "game.t_board",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    t_Board is array  (t_Board_Size) of t_Row;",
       }   ,
       {
       name: "t_List",
       qualified_name: "Game.t_List",
       signature: "game.t_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    t_List  is array (Positive range <>) of Natural;",
       }   ,
   ]
,record_types:    [
       {
       name: "t_Board_State",
       qualified_name: "Game.t_Board_State",
       signature: "game.t_board_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_Board_State is record\n   Board       : t_Board;\n   Score       : Natural;\n   Blanks      : t_Cell_Count;\n   Start_Time  : Ada.Calendar.Time;\n   Game_Status : t_Game_Status;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "t_Board_Size",
       qualified_name: "Game.t_Board_Size",
       signature: "game.t_board_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype t_Board_Size is Natural range 1 .. Board_Length;",
       }   ,
       {
       name: "t_Cell_Count",
       qualified_name: "Game.t_Cell_Count",
       signature: "game.t_cell_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype t_Cell_Count is Natural range 0 .. Board_Length ** 2;",
       }   ,
       {
       name: "t_Row",
       qualified_name: "Game.t_Row",
       signature: "game.t_row",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype t_Row   is t_List (t_Board_Size);",
       }   ,
   ]
,constants:    [
       {
       name: "Board_Length",
       qualified_name: "Game.Board_Length",
       signature: "game.board_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Board_Length : constant Natural :=\n  (if Ada.Environment_Variables.Exists (Environment_Size) then\n      Natural'Value (Ada.Environment_Variables.Value (Environment_Size))\n   else Default_Length);",
       }   ,
       {
       name: "Default_Length",
       qualified_name: "Game.Default_Length",
       signature: "game.default_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Length : constant := 4;",
       }   ,
       {
       name: "Environment_Size",
       qualified_name: "Game.Environment_Size",
       signature: "game.environment_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Environment_Size : constant String := \"PLAY_2048_SIZE\";",
       }   ,
   ]
,}
---

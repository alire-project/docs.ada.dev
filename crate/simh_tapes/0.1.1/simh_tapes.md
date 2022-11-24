---
crate: simh_tapes
layout: gnatdoc
gnatdoc: {
name: "Simh_Tapes",
qualified_name: "Simh_Tapes",
signature: "simh_tapes",
enclosing: "",
is_private: false,
documentation: "tape image markers",
documentation_snippet: "",
simple_types:    [
       {
       name: "Mt_Stat",
       qualified_name: "Simh_Tapes.Mt_Stat",
       signature: "simh_tapes.mt_stat",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mt_Stat is\n   (OK, Tmk, Unatt, IOerr, InvRec, InvFmt, BOT, EOM, RecErr, WrOnly);",
       }   ,
   ]
,array_types:    [
       {
       name: "Mt_Rec",
       qualified_name: "Simh_Tapes.Mt_Rec",
       signature: "simh_tapes.mt_rec",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mt_Rec is array (Natural range <>) of Unsigned_8;",
       }   ,
   ]
,constants:    [
       {
       name: "Mtr_EOM",
       qualified_name: "Simh_Tapes.Mtr_EOM",
       signature: "simh_tapes.mtr_eom",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Mtr_EOM     : constant Unsigned_32 := 16#ffff_ffff#;",
       }   ,
       {
       name: "Mtr_Erf",
       qualified_name: "Simh_Tapes.Mtr_Erf",
       signature: "simh_tapes.mtr_erf",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Mtr_Erf     : constant Unsigned_32 := 16#8000_0000#;",
       }   ,
       {
       name: "Mtr_Gap",
       qualified_name: "Simh_Tapes.Mtr_Gap",
       signature: "simh_tapes.mtr_gap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Mtr_Gap     : constant Unsigned_32 := 16#ffff_fffe#;",
       }   ,
       {
       name: "Mtr_Max_Len",
       qualified_name: "Simh_Tapes.Mtr_Max_Len",
       signature: "simh_tapes.mtr_max_len",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Mtr_Max_Len : constant Unsigned_32 := 16#00ff_ffff#;",
       }   ,
       {
       name: "Mtr_Tmk",
       qualified_name: "Simh_Tapes.Mtr_Tmk",
       signature: "simh_tapes.mtr_tmk",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Mtr_Tmk     : constant Unsigned_32 := 0;",
       }   ,
   ]
,}
---

---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "U_Rand",
qualified_name: "U_Rand",
signature: "u_rand",
enclosing: "",
is_private: false,
documentation: "------------------------------------------------------------------------
documentation_snippet: "",
simple_types:    [
       {
       name: "Generator",
       qualified_name: "U_Rand.Generator",
       signature: "u_rand.generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator is limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "SEED_RANGE_1",
       qualified_name: "U_Rand.SEED_RANGE_1",
       signature: "u_rand.seed_range_1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SEED_RANGE_1 is Integer range 1..M1-1 ;",
       }   ,
       {
       name: "SEED_RANGE_2",
       qualified_name: "U_Rand.SEED_RANGE_2",
       signature: "u_rand.seed_range_2",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SEED_RANGE_2 is Integer range 1..M2-1 ;",
       }   ,
       {
       name: "Seed_range_for_Reset",
       qualified_name: "U_Rand.Seed_range_for_Reset",
       signature: "u_rand.seed_range_for_reset",
       enclosing: "",
       is_private: false,
       documentation: "NB: concretely, the range is: 0 .. 947'478'337
       documentation_snippet: "subtype Seed_range_for_Reset is Integer range 0 .. ((M1-1) ** 3) * (M2-1) - 1;",
       }   ,
       {
       name: "Uniformly_Distributed",
       qualified_name: "U_Rand.Uniformly_Distributed",
       signature: "u_rand.uniformly_distributed",
       enclosing: "",
       is_private: false,
       documentation: "
       documentation_snippet: "subtype Uniformly_Distributed is Real range 0.0 .. 1.0;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_I",
       qualified_name: "U_Rand.Default_I",
       signature: "u_rand.default_i",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_I : constant SEED_RANGE_1 := 12 ;",
       }   ,
       {
       name: "Default_J",
       qualified_name: "U_Rand.Default_J",
       signature: "u_rand.default_j",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_J : constant SEED_RANGE_1 := 34 ;",
       }   ,
       {
       name: "Default_K",
       qualified_name: "U_Rand.Default_K",
       signature: "u_rand.default_k",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_K : constant SEED_RANGE_1 := 56 ;",
       }   ,
       {
       name: "Default_L",
       qualified_name: "U_Rand.Default_L",
       signature: "u_rand.default_l",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_L : constant SEED_RANGE_1 := 78 ;",
       }   ,
       {
       name: "M1",
       qualified_name: "U_Rand.M1",
       signature: "u_rand.m1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "M1 : constant := 179 ;",
       }   ,
       {
       name: "M2",
       qualified_name: "U_Rand.M2",
       signature: "u_rand.m2",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "M2 : constant := M1 - 10 ;",
       }   ,
   ]
,}
---
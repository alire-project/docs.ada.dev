---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Stochastics.Mdp",
qualified_name: "Agpl.Stochastics.Mdp",
signature: "agpl.stochastics.mdp",
enclosing: "agpl.stochastics",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Discounts",
       qualified_name: "Agpl.Stochastics.Mdp.Discounts",
       signature: "agpl.stochastics.mdp.discounts",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Discounts is new Float range 0.0 .. 1.0;",
       }   ,
       {
       name: "Distances",
       qualified_name: "Agpl.Stochastics.Mdp.Distances",
       signature: "agpl.stochastics.mdp.distances",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Distances is new Float;",
       }   ,
       {
       name: "Rewards",
       qualified_name: "Agpl.Stochastics.Mdp.Rewards",
       signature: "agpl.stochastics.mdp.rewards",
       enclosing: "",
       is_private: false,
       documentation: "Costs and Rewards are equivalent, just the sign changes.",
       documentation_snippet: "type Rewards is new Float;",
       }   ,
   ]
,array_types:    [
       {
       name: "Markov_Matrix",
       qualified_name: "Agpl.Stochastics.Mdp.Markov_Matrix",
       signature: "agpl.stochastics.mdp.markov_matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Markov_Matrix is\n  array (Positive range <>, Positive range <>) of Probabilities;",
       }   ,
       {
       name: "Reward_Array",
       qualified_name: "Agpl.Stochastics.Mdp.Reward_Array",
       signature: "agpl.stochastics.mdp.reward_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reward_Array is array (Positive range <>) of Rewards;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Costs",
       qualified_name: "Agpl.Stochastics.Mdp.Costs",
       signature: "agpl.stochastics.mdp.costs",
       enclosing: "",
       is_private: false,
       documentation: "Costs and Rewards are equivalent, just the sign changes.",
       documentation_snippet: "subtype Costs is Rewards;",
       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Stochastics.Mdp.Log_Section",
       signature: "agpl.stochastics.mdp.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.stochastics.mdp\";",
       }   ,
   ]
,variables:    [
       {
       name: "Verbose",
       qualified_name: "Agpl.Stochastics.Mdp.Verbose",
       signature: "agpl.stochastics.mdp.verbose",
       enclosing: "",
       is_private: false,
       documentation: "If true, detailed progress messages will be printed by the solvers.",
       documentation_snippet: "Verbose : Boolean := False;",
       }   ,
   ]
,}
---

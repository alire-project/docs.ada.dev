---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Discrete_Random_Simulation",
qualified_name: "Discrete_Random_Simulation",
signature: "discrete_random_simulation",
enclosing: "",
is_private: false,
documentation: "--------------------------------------------------------------------------\n  The function Index gives the appropriate index of an array Fx containing\n  a Cumulative Distribution Function (CDF), given a value in [0,1].\n  Index is given in three variants with different usefulness/performance\n  features (discussed in their specifications):\n\n     Index_Linear_Search\n     Index_Dichotomic_Search\n     Index_Alias_Method\n\n  The Fx array type represents an empiric random variable\n  with integer values, like 0,1,2,...n, and cumulative probabilities\n  p0, p0+p1, ... , p0+p1+...+pn = 1\n\n  Indeed, Index is an inverse CDF function.\n\n  For general discrete random variables with values that are not all integers\n  you can use an array x(i). Example: x(Index_Linear_Search(Random(gen), Fx)).\n\n  Caution:\n----------\n\n    1) The first probability value in the array must be 0.0. The array\n           represents the function F(x) = P(X<x) (variant of P with strict \"<\").\n\n    2) It is advised to avoid an 1.0 as final value for\n           the \"x=infinite case\" even if it looks fine, since\n           it will be drawn sometimes due to random U01 values\n           very close to 1 that satisfy, *numerically*, 1.0 <= U01.\n\n  Examples with correct data (more in Test_Discrete_Random_Simulation):\n\n     Flip-or-coin: (0.0, 0.5)\n\n     Dice: (0.0, 1.0/6.0, 2.0/6.0, 3.0/6.0, 4.0/6.0, 5.0/6.0)\n\n--------------------------------------------------------------------------\n\n@formal Probability_value\n@formal Probability_array",
documentation_snippet: "",
simple_types:    [
       {
       name: "Alias_pair",
       qualified_name: "Discrete_Random_Simulation.Alias_pair",
       signature: "discrete_random_simulation.alias_pair",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Alias_pair is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Alias_table",
       qualified_name: "Discrete_Random_Simulation.Alias_table",
       signature: "discrete_random_simulation.alias_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Alias_table is array (Integer range <>) of Alias_pair;",
       }   ,
   ]
,}
---

---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Permutations",
qualified_name: "Permutations",
signature: "permutations",
enclosing: "",
is_private: false,
documentation: "Creation : 13-JAN-1989 by Mats Weber.\n\n@formal Discrete\n  Must have at least two values\n@formal Count",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parity",
       qualified_name: "Permutations.Parity",
       signature: "permutations.parity",
       enclosing: "",
       is_private: false,
       documentation: "---------\n\n@enum Even\n@enum Odd",
       documentation_snippet: "type Parity is (Even, Odd);",
       }   ,
   ]
,array_types:    [
       {
       name: "Cycle_List",
       qualified_name: "Permutations.Cycle_List",
       signature: "permutations.cycle_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cycle_List is array (Positive_Count range <>) of Cycle;",
       }   ,
       {
       name: "Discrete_List",
       qualified_name: "Permutations.Discrete_List",
       signature: "permutations.discrete_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Discrete_List is array (Positive_Count range <>) of Discrete;",
       }   ,
       {
       name: "Permutation",
       qualified_name: "Permutations.Permutation",
       signature: "permutations.permutation",
       enclosing: "",
       is_private: false,
       documentation: "--------------",
       documentation_snippet: "type Permutation is array (Discrete) of Discrete;",
       }   ,
       {
       name: "Transposition_List",
       qualified_name: "Permutations.Transposition_List",
       signature: "permutations.transposition_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Transposition_List is array (Positive_Count range <>) of Transposition;",
       }   ,
   ]
,record_types:    [
       {
       name: "Cycle",
       qualified_name: "Permutations.Cycle",
       signature: "permutations.cycle",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Length\n  --------\n@field Contents",
       documentation_snippet: "type Cycle (Length : Cycle_Length := 2) is\n   record\n      Contents : Discrete_List(1..Length);\n   end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Cycle_Length",
       qualified_name: "Permutations.Cycle_Length",
       signature: "permutations.cycle_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Cycle_Length is Count range 2..Permutation'Length;",
       }   ,
       {
       name: "Positive_Count",
       qualified_name: "Permutations.Positive_Count",
       signature: "permutations.positive_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Positive_Count is Count range 1..Count'Last;",
       }   ,
       {
       name: "Transposition",
       qualified_name: "Permutations.Transposition",
       signature: "permutations.transposition",
       enclosing: "",
       is_private: false,
       documentation: "-------------------",
       documentation_snippet: "subtype Transposition is Cycle(Length => 2);",
       }   ,
   ]
,}
---

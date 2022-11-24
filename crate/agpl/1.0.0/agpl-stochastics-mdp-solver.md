---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Stochastics.Mdp.Solver",
qualified_name: "Agpl.Stochastics.Mdp.Solver",
signature: "agpl.stochastics.mdp.solver",
enclosing: "agpl.stochastics.mdp",
is_private: false,
documentation: "Root package for MDP solvers.",
documentation_snippet: "",
access_types:    [
       {
       name: "Action_Evolution_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Action_Evolution_Function",
       signature: "agpl.stochastics.mdp.solver.action_evolution_function",
       enclosing: "",
       is_private: false,
       documentation: "All states reachable from a single state, given an action.\n\n@param Initial\n@param Action\n\n@return",
       documentation_snippet: "type Action_Evolution_Function is access function\n  (Initial : in State.Object'Class;\n   Action  : in Mdp.Action.Object'Class)\n   return       State.Object_Lists.List;",
       }   ,
       {
       name: "Action_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Action_Function",
       signature: "agpl.stochastics.mdp.solver.action_function",
       enclosing: "",
       is_private: false,
       documentation: "This function must return all appliable actions to some state.\n\n@param Initial\n\n@return",
       documentation_snippet: "type Action_Function is access function\n  (Initial : in State.Object'Class)\n   return       Action.Object_Lists.List;",
       }   ,
       {
       name: "Evolution_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Evolution_Function",
       signature: "agpl.stochastics.mdp.solver.evolution_function",
       enclosing: "",
       is_private: false,
       documentation: "This function must return all reachable states from another given one.\n\n@param Initial\n\n@return",
       documentation_snippet: "type Evolution_Function is access function\n  (Initial : in State.Object'Class)\n   return       State.Object_Lists.List;",
       }   ,
       {
       name: "Involution_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Involution_Function",
       signature: "agpl.stochastics.mdp.solver.involution_function",
       enclosing: "",
       is_private: false,
       documentation: "Gives states from where the Final state is reachable.\n\n@param Final\n\n@return",
       documentation_snippet: "type Involution_Function is access function\n  (Final : in State.Object'Class)\n   return     State.Object_Lists.List;",
       }   ,
       {
       name: "Reward_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Reward_Function",
       signature: "agpl.stochastics.mdp.solver.reward_function",
       enclosing: "",
       is_private: false,
       documentation: "This function is the typical reward function for MDPs\n\n@param Initial\n@param Doing\n@param Final\n\n@return",
       documentation_snippet: "type Reward_Function is access function\n  (Initial : in State.Object'Class;\n   Doing   : in Action.Object'Class;\n   Final   : in State.Object'Class)\n   return       Rewards;",
       }   ,
       {
       name: "Transition_Function",
       qualified_name: "Agpl.Stochastics.Mdp.Solver.Transition_Function",
       signature: "agpl.stochastics.mdp.solver.transition_function",
       enclosing: "",
       is_private: false,
       documentation: "This function is the typical transition function for MDPs\n\n@param Initial\n@param Doing\n@param Final\n\n@return",
       documentation_snippet: "type Transition_Function is access function\n  (Initial : in State.Object'Class;\n   Doing   : in Action.Object'Class;\n   Final   : in State.Object'Class)\n   return       Probabilities;",
       }   ,
   ]
,}
---

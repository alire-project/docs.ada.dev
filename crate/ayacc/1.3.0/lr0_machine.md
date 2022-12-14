---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "LR0_Machine",
qualified_name: "LR0_Machine",
signature: "lr0_machine",
enclosing: "",
is_private: false,
documentation: "$Header: /dc/uc/self/tmp/gnat_ayacc_new/lr0bad/RCS/lr0_machine.ads,v 1.1 1995/02/16 17:28:09 self Exp self $ \n$Log: lr0_machine.ads,v $\nRevision 0.1  86/04/01  15:06:19  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:37:14  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
documentation_snippet: "",
simple_types:    [
       {
       name: "Kernel_Iterator",
       qualified_name: "LR0_Machine.Kernel_Iterator",
       signature: "lr0_machine.kernel_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Kernel_Iterator is limited private;",
       }   ,
       {
       name: "Nt_Transition_Iterator",
       qualified_name: "LR0_Machine.Nt_Transition_Iterator",
       signature: "lr0_machine.nt_transition_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Nt_Transition_Iterator is limited private;",
       }   ,
       {
       name: "Parse_State",
       qualified_name: "LR0_Machine.Parse_State",
       signature: "lr0_machine.parse_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parse_State   is   range -1..5_000;",
       }   ,
       {
       name: "T_Transition_Iterator",
       qualified_name: "LR0_Machine.T_Transition_Iterator",
       signature: "lr0_machine.t_transition_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type T_Transition_Iterator is limited private;",
       }   ,
       {
       name: "Transition_Type",
       qualified_name: "LR0_Machine.Transition_Type",
       signature: "lr0_machine.transition_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Transition_Type is (Terminals, Nonterminals, Grammar_Symbols);",
       }   ,
   ]
,record_types:    [
       {
       name: "Item",
       qualified_name: "LR0_Machine.Item",
       signature: "lr0_machine.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "    type Item is\n	record\n	    Rule_ID      : Rule;\n	    Dot_Position : Natural;\n	end record;",
       }   ,
       {
       name: "Transition",
       qualified_name: "LR0_Machine.Transition",
       signature: "lr0_machine.transition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "    type Transition is\n	record\n	    Symbol   : Grammar_Symbol;\n	    State_ID : Parse_State;\n	end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Grammar_Symbol_Iterator",
       qualified_name: "LR0_Machine.Grammar_Symbol_Iterator",
       signature: "lr0_machine.grammar_symbol_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Grammar_Symbol_Iterator  is Grammar_Symbol_Set_Pack.Set_Iterator;",
       }   ,
       {
       name: "Grammar_Symbol_Set",
       qualified_name: "LR0_Machine.Grammar_Symbol_Set",
       signature: "lr0_machine.grammar_symbol_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Grammar_Symbol_Set       is Grammar_Symbol_Set_Pack.Set;",
       }   ,
       {
       name: "Item_Iterator",
       qualified_name: "LR0_Machine.Item_Iterator",
       signature: "lr0_machine.item_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Item_Iterator            is Item_Set_Pack.Set_Iterator;",
       }   ,
       {
       name: "Item_Set",
       qualified_name: "LR0_Machine.Item_Set",
       signature: "lr0_machine.item_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Item_Set                 is Item_Set_Pack.Set;",
       }   ,
       {
       name: "Parse_State_Iterator",
       qualified_name: "LR0_Machine.Parse_State_Iterator",
       signature: "lr0_machine.parse_state_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parse_State_Iterator     is Parse_State_Set_Pack.Set_Iterator;",
       }   ,
       {
       name: "Parse_State_Set",
       qualified_name: "LR0_Machine.Parse_State_Set",
       signature: "lr0_machine.parse_state_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parse_State_Set          is Parse_State_Set_Pack.Set;",
       }   ,
       {
       name: "Transition_Iterator",
       qualified_name: "LR0_Machine.Transition_Iterator",
       signature: "lr0_machine.transition_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Transition_Iterator      is Transition_Set_Pack.Set_Iterator;",
       }   ,
       {
       name: "Transition_Set",
       qualified_name: "LR0_Machine.Transition_Set",
       signature: "lr0_machine.transition_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Transition_Set           is Transition_Set_Pack.Set;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Parse_State",
       qualified_name: "LR0_Machine.Null_Parse_State",
       signature: "lr0_machine.null_parse_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Parse_State   :    constant Parse_State := -1;",
       }   ,
   ]
,}
---

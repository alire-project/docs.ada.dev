---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Machine_Code",
qualified_name: "System.Machine_Code",
signature: "system.machine_code",
enclosing: "system",
is_private: false,
documentation: "This package provides machine code support, both for intrinsic machine\noperations, and also for machine code statements. See GNAT documentation\nfor full details.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Asm_Input_Operand",
       qualified_name: "System.Machine_Code.Asm_Input_Operand",
       signature: "system.machine_code.asm_input_operand",
       enclosing: "",
       is_private: false,
       documentation: "These types are never used directly, they are declared only so that\nthe calls to Asm are type correct according to Ada semantic rules.",
       documentation_snippet: "type Asm_Input_Operand  is private;",
       }   ,
       {
       name: "Asm_Insn",
       qualified_name: "System.Machine_Code.Asm_Insn",
       signature: "system.machine_code.asm_insn",
       enclosing: "",
       is_private: false,
       documentation: "This type is not used directly. It is declared only so that the\naggregates used in code statements are type correct by Ada rules.",
       documentation_snippet: "type Asm_Insn is private;",
       }   ,
       {
       name: "Asm_Output_Operand",
       qualified_name: "System.Machine_Code.Asm_Output_Operand",
       signature: "system.machine_code.asm_output_operand",
       enclosing: "",
       is_private: false,
       documentation: "These types are never used directly, they are declared only so that\nthe calls to Asm are type correct according to Ada semantic rules.",
       documentation_snippet: "type Asm_Output_Operand is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Asm_Input_Operand_List",
       qualified_name: "System.Machine_Code.Asm_Input_Operand_List",
       signature: "system.machine_code.asm_input_operand_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Asm_Input_Operand_List  is\n  array (Integer range <>) of Asm_Input_Operand;",
       }   ,
       {
       name: "Asm_Output_Operand_List",
       qualified_name: "System.Machine_Code.Asm_Output_Operand_List",
       signature: "system.machine_code.asm_output_operand_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Asm_Output_Operand_List is\n  array (Integer range <>) of Asm_Output_Operand;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Input_Operands",
       qualified_name: "System.Machine_Code.No_Input_Operands",
       signature: "system.machine_code.no_input_operands",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Input_Operands  : constant Asm_Input_Operand;",
       }   ,
       {
       name: "No_Output_Operands",
       qualified_name: "System.Machine_Code.No_Output_Operands",
       signature: "system.machine_code.no_output_operands",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Output_Operands : constant Asm_Output_Operand;",
       }   ,
   ]
,}
---

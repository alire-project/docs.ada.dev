---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PIO.Encoding",
qualified_name: "RP.PIO.Encoding",
signature: "rp.pio.encoding",
enclosing: "rp.pio",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "JMP_Condition",
       qualified_name: "RP.PIO.Encoding.JMP_Condition",
       signature: "rp.pio.encoding.jmp_condition",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Always\n@enum Scratch_X_Zero\n  !X\n@enum Scratch_X_Nonzero_Decrement\n  X--\n@enum Scratch_Y_Zero\n  !Y\n@enum Scratch_Y_Nonzero_Decrement\n  Y--\n@enum X_Notequal_Y\n  X!=Y\n@enum Input_Pin\n  PIN\n@enum OSRE_Not_Empty\n  !OSRE",
       documentation_snippet: "type JMP_Condition is\n   (Always,\n    Scratch_X_Zero,\n    Scratch_X_Nonzero_Decrement,\n    Scratch_Y_Zero,\n    Scratch_Y_Nonzero_Decrement,\n    X_Notequal_Y,\n    Input_Pin,\n    OSRE_Not_Empty)\nwith Size => 3;",
       }   ,
       {
       name: "MOV_Operation",
       qualified_name: "RP.PIO.Encoding.MOV_Operation",
       signature: "rp.pio.encoding.mov_operation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MOV_Operation is\n   (None, Invert, Bit_Reverse)\nwith Size => 2;",
       }   ,
       {
       name: "MOV_Target",
       qualified_name: "RP.PIO.Encoding.MOV_Target",
       signature: "rp.pio.encoding.mov_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MOV_Target is\n   (PINS, X, Y, EXEC, PC, ISR, OSR)\nwith Size => 3;",
       }   ,
       {
       name: "SET_Destination",
       qualified_name: "RP.PIO.Encoding.SET_Destination",
       signature: "rp.pio.encoding.set_destination",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SET_Destination is\n   (PINS, X, Y, PINDIRS)\nwith Size => 3;",
       }   ,
       {
       name: "SHIFT_IN_Source",
       qualified_name: "RP.PIO.Encoding.SHIFT_IN_Source",
       signature: "rp.pio.encoding.shift_in_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SHIFT_IN_Source is\n   (PINS, X, Y, ZERO, ISR, OSR)\nwith Size => 3;",
       }   ,
       {
       name: "SHIFT_OUT_Destination",
       qualified_name: "RP.PIO.Encoding.SHIFT_OUT_Destination",
       signature: "rp.pio.encoding.shift_out_destination",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SHIFT_OUT_Destination is\n   (PINS, X, Y, DISCARD, PINDIRS, PC, ISR, EXEC)\nwith Size => 3;",
       }   ,
       {
       name: "WAIT_Source",
       qualified_name: "RP.PIO.Encoding.WAIT_Source",
       signature: "rp.pio.encoding.wait_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WAIT_Source is\n   (GPIO, PIN, WAIT_IRQ)\nwith Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "IRQ",
       qualified_name: "RP.PIO.Encoding.IRQ",
       signature: "rp.pio.encoding.irq",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IRQ is record\n   Opcode         : HAL.UInt3 := 2#110#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Opcode_2       : Boolean := False;\n   Clear          : Boolean := False;\n   Wait           : Boolean := False;\n   Index          : HAL.UInt5;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "JMP",
       qualified_name: "RP.PIO.Encoding.JMP",
       signature: "rp.pio.encoding.jmp",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JMP is record\n   Opcode         : HAL.UInt3 := 2#000#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Condition      : JMP_Condition := Always;\n   Address        : HAL.UInt5 := 0;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "MOV",
       qualified_name: "RP.PIO.Encoding.MOV",
       signature: "rp.pio.encoding.mov",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MOV is record\n   Opcode         : HAL.UInt3 := 2#101#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Destination    : MOV_Target := PINS;\n   Operation      : MOV_Operation := None;\n   Source         : MOV_Target := PINS;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "PULL",
       qualified_name: "RP.PIO.Encoding.PULL",
       signature: "rp.pio.encoding.pull",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PULL is record\n   Opcode         : HAL.UInt3 := 2#100#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Opcode_2       : Boolean := True;\n   If_Empty       : Boolean := False;\n   Block          : Boolean := False;\n   Opcode_3       : HAL.UInt5 := 0;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "PUSH",
       qualified_name: "RP.PIO.Encoding.PUSH",
       signature: "rp.pio.encoding.push",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PUSH is record\n   Opcode         : HAL.UInt3 := 2#100#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Opcode_2       : Boolean := False;\n   If_Full        : Boolean := False;\n   Block          : Boolean := False;\n   Opcode_3       : HAL.UInt5 := 0;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "SET",
       qualified_name: "RP.PIO.Encoding.SET",
       signature: "rp.pio.encoding.set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SET is record\n   Opcode         : HAL.UInt3 := 2#111#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Destination    : SET_Destination := PINS;\n   Data           : HAL.UInt5 := 0;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "SHIFT_IN",
       qualified_name: "RP.PIO.Encoding.SHIFT_IN",
       signature: "rp.pio.encoding.shift_in",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Opcode\n@field Delay_Sideset\n@field Source\n@field Bit_Count\n  0 = 32",
       documentation_snippet: "type SHIFT_IN is record\n   Opcode         : HAL.UInt3 := 2#010#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Source         : SHIFT_IN_Source := PINS;\n   Bit_Count      : HAL.UInt5;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "SHIFT_OUT",
       qualified_name: "RP.PIO.Encoding.SHIFT_OUT",
       signature: "rp.pio.encoding.shift_out",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Opcode\n@field Delay_Sideset\n@field Destination\n@field Bit_Count\n  0 = 32",
       documentation_snippet: "type SHIFT_OUT is record\n   Opcode         : HAL.UInt3 := 2#011#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Destination    : SHIFT_OUT_Destination := PINS;\n   Bit_Count      : HAL.UInt5;\nend record\n   with Size => 16;",
       }   ,
       {
       name: "WAIT",
       qualified_name: "RP.PIO.Encoding.WAIT",
       signature: "rp.pio.encoding.wait",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WAIT is record\n   Opcode         : HAL.UInt3 := 2#001#;\n   Delay_Sideset  : HAL.UInt5 := 0;\n   Polarity       : Boolean := False;\n   Source         : WAIT_Source := GPIO;\n   Index          : HAL.UInt5 := 0;\nend record\n   with Size => 16;",
       }   ,
   ]
,}
---
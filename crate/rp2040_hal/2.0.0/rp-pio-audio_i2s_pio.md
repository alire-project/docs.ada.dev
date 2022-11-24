---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PIO.Audio_I2S_PIO",
qualified_name: "RP.PIO.Audio_I2S_PIO",
signature: "rp.pio.audio_i2s_pio",
enclosing: "rp.pio",
is_private: false,
documentation: "-------------\n Audio_I2s --\n-------------",
documentation_snippet: "",
constants:    [
       {
       name: "Audio_I2s_Wrap",
       qualified_name: "RP.PIO.Audio_I2S_PIO.Audio_I2s_Wrap",
       signature: "rp.pio.audio_i2s_pio.audio_i2s_wrap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Audio_I2s_Wrap        : constant := 7;",
       }   ,
       {
       name: "Audio_I2s_Wrap_Target",
       qualified_name: "RP.PIO.Audio_I2S_PIO.Audio_I2s_Wrap_Target",
       signature: "rp.pio.audio_i2s_pio.audio_i2s_wrap_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Audio_I2s_Wrap_Target : constant := 0;",
       }   ,
       {
       name: "Offset_entry_point",
       qualified_name: "RP.PIO.Audio_I2S_PIO.Offset_entry_point",
       signature: "rp.pio.audio_i2s_pio.offset_entry_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Offset_entry_point : constant := 7;",
       }   ,
   ]
,variables:    [
       {
       name: "Audio_I2s_Program_Instructions",
       qualified_name: "RP.PIO.Audio_I2S_PIO.Audio_I2s_Program_Instructions",
       signature: "rp.pio.audio_i2s_pio.audio_i2s_program_instructions",
       enclosing: "",
       is_private: false,
       documentation: " 7: set    x, 14           side 3\n.wrap",
       documentation_snippet: "Audio_I2s_Program_Instructions : RP.PIO.Program := (\n      16#7001#,\n      16#1840#,\n      16#6001#,\n      16#e82e#,\n      16#6001#,\n      16#0844#,\n      16#7001#,\n      16#f82e#);",
       }   ,
   ]
,}
---

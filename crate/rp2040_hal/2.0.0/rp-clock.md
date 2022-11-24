---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.Clock",
qualified_name: "RP.Clock",
signature: "rp.clock",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Clock_Id",
       qualified_name: "RP.Clock.Clock_Id",
       signature: "rp.clock.clock_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Clock_Id is\n   (GPOUT0, GPOUT1, GPOUT2, GPOUT3, REF, SYS, PERI, USB, ADC, RTC,\n    PLL_SYS, GPIN0, GPIN1, PLL_USB, ROSC, XOSC);",
       }   ,
   ]
,record_types:    [
       {
       name: "PLL_Config",
       qualified_name: "RP.Clock.PLL_Config",
       signature: "rp.clock.pll_config",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py\n\n@field FREF\n@field REFDIV\n@field FBDIV\n@field POSTDIV1\n@field POSTDIV2",
       documentation_snippet: "type PLL_Config is record\n   FREF     : PLL_FREF_Field;\n   REFDIV   : PLL_REFDIV_Field;\n   FBDIV    : PLL_FBDIV_Field;\n   POSTDIV1 : PLL_POSTDIV_Field;\n   POSTDIV2 : PLL_POSTDIV_Field;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Countable_Clock_Id",
       qualified_name: "RP.Clock.Countable_Clock_Id",
       signature: "rp.clock.countable_clock_id",
       enclosing: "",
       is_private: false,
       documentation: "By default, the fractional part of the frequency counter result register\nis ignored. Setting Rounded = False includes the fractional frequency,\nwhich may include as much as 2048 KHz of error, depending on the\nvalue of Accuracy. Higher Accuracy values take longer to measure the\nclock, but produce more accurate results.",
       documentation_snippet: "subtype Countable_Clock_Id is Clock_Id range REF .. RTC;",
       }   ,
       {
       name: "GP_Output",
       qualified_name: "RP.Clock.GP_Output",
       signature: "rp.clock.gp_output",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype GP_Output is Clock_Id range GPOUT0 .. GPOUT3;",
       }   ,
       {
       name: "GP_Source",
       qualified_name: "RP.Clock.GP_Source",
       signature: "rp.clock.gp_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype GP_Source is Clock_Id range REF .. XOSC;",
       }   ,
       {
       name: "PLL_Clock_Id",
       qualified_name: "RP.Clock.PLL_Clock_Id",
       signature: "rp.clock.pll_clock_id",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py",
       documentation_snippet: "subtype PLL_Clock_Id is Clock_Id\n   with Static_Predicate => PLL_Clock_Id in PLL_SYS | PLL_USB;",
       }   ,
       {
       name: "PLL_FBDIV_Field",
       qualified_name: "RP.Clock.PLL_FBDIV_Field",
       signature: "rp.clock.pll_fbdiv_field",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py",
       documentation_snippet: "subtype PLL_FBDIV_Field is UInt12 range 16 .. 320;",
       }   ,
       {
       name: "PLL_FREF_Field",
       qualified_name: "RP.Clock.PLL_FREF_Field",
       signature: "rp.clock.pll_fref_field",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py",
       documentation_snippet: "subtype PLL_FREF_Field is Hertz range 5_000_000 .. 800_000_000;",
       }   ,
       {
       name: "PLL_POSTDIV_Field",
       qualified_name: "RP.Clock.PLL_POSTDIV_Field",
       signature: "rp.clock.pll_postdiv_field",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py",
       documentation_snippet: "subtype PLL_POSTDIV_Field is UInt3 range 1 .. 7;",
       }   ,
       {
       name: "PLL_REFDIV_Field",
       qualified_name: "RP.Clock.PLL_REFDIV_Field",
       signature: "rp.clock.pll_refdiv_field",
       enclosing: "",
       is_private: false,
       documentation: "2.18.2. Calculating PLL parameters\nPLL = (FREF / REFDIV) * FBDIV / (POSTDIV1 / POSTDIV2)\nCommon configurations are included below.\nUse pico-sdk/src/rp2_common/hardware_clocks/scripts/vcocalc.py",
       documentation_snippet: "subtype PLL_REFDIV_Field is UInt6 range 1 .. 63;",
       }   ,
       {
       name: "SYS_Clock_Id",
       qualified_name: "RP.Clock.SYS_Clock_Id",
       signature: "rp.clock.sys_clock_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SYS_Clock_Id is Clock_Id range PLL_SYS .. XOSC;",
       }   ,
       {
       name: "XOSC_Cycles",
       qualified_name: "RP.Clock.XOSC_Cycles",
       signature: "rp.clock.xosc_cycles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype XOSC_Cycles is Natural;",
       }   ,
       {
       name: "XOSC_Hertz",
       qualified_name: "RP.Clock.XOSC_Hertz",
       signature: "rp.clock.xosc_hertz",
       enclosing: "",
       is_private: false,
       documentation: "The special value 0 indicates that the XOSC is not available.",
       documentation_snippet: "subtype XOSC_Hertz is Hertz range 0 .. 15_000_000\n   with Static_Predicate => XOSC_Hertz in 0 | 1_000_000 .. 15_000_000;",
       }   ,
   ]
,constants:    [
       {
       name: "GP_Divider_Fraction",
       qualified_name: "RP.Clock.GP_Divider_Fraction",
       signature: "rp.clock.gp_divider_fraction",
       enclosing: "",
       is_private: false,
       documentation: "If GP_Divider is 0.0, then it represents (2.0 ** 16)",
       documentation_snippet: "GP_Divider_Fraction : constant := 1.0 / (2 ** 8);",
       }   ,
       {
       name: "PLL_125_MHz",
       qualified_name: "RP.Clock.PLL_125_MHz",
       signature: "rp.clock.pll_125_mhz",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_125_MHz : constant PLL_Config :=\n   (FREF     => 12_000_000,\n    REFDIV   => 1,\n    FBDIV    => 125,\n    POSTDIV1 => 6,\n    POSTDIV2 => 2);",
       }   ,
       {
       name: "PLL_133_MHz",
       qualified_name: "RP.Clock.PLL_133_MHz",
       signature: "rp.clock.pll_133_mhz",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_133_MHz : constant PLL_Config :=\n   (FREF     => 12_000_000,\n    REFDIV   => 1,\n    FBDIV    => 133,\n    POSTDIV1 => 6,\n    POSTDIV2 => 2);",
       }   ,
       {
       name: "PLL_250_MHz",
       qualified_name: "RP.Clock.PLL_250_MHz",
       signature: "rp.clock.pll_250_mhz",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_250_MHz : constant PLL_Config :=\n   (FREF     => 12_000_000,\n    REFDIV   => 1,\n    FBDIV    => 125,\n    POSTDIV1 => 6,\n    POSTDIV2 => 1);",
       }   ,
       {
       name: "PLL_48_MHz",
       qualified_name: "RP.Clock.PLL_48_MHz",
       signature: "rp.clock.pll_48_mhz",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_48_MHz : constant PLL_Config :=\n   (FREF     => 12_000_000,\n    REFDIV   => 1,\n    FBDIV    => 64,\n    POSTDIV1 => 4,\n    POSTDIV2 => 4);",
       }   ,
   ]
,}
---
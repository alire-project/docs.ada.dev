---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE.Maths_Tables",
qualified_name: "GESTE.Maths_Tables",
signature: "geste.maths_tables",
enclosing: "geste",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
constants:    [
       {
       name: "Cos_Alpha",
       qualified_name: "GESTE.Maths_Tables.Cos_Alpha",
       signature: "geste.maths_tables.cos_alpha",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Cos_Alpha      : constant := Value (Cos_Table_Size) / (2 * 3.14159);",
       }   ,
       {
       name: "Cos_Table",
       qualified_name: "GESTE.Maths_Tables.Cos_Table",
       signature: "geste.maths_tables.cos_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Cos_Table : constant array (Unsigned_32 range 0 .. Cos_Table_Size - 1) of Value :=\n ( 1.000, 1.000, 0.999, 0.997, 0.995, 0.992,\n   0.989, 0.985, 0.981, 0.976, 0.970, 0.964,\n   0.957, 0.950, 0.942, 0.933, 0.924, 0.914,\n   0.904, 0.893, 0.882, 0.870, 0.858, 0.845,\n   0.831, 0.818, 0.803, 0.788, 0.773, 0.757,\n   0.741, 0.724, 0.707, 0.690, 0.672, 0.653,\n   0.634, 0.615, 0.596, 0.576, 0.556, 0.535,\n   0.514, 0.493, 0.471, 0.450, 0.428, 0.405,\n   0.383, 0.360, 0.337, 0.314, 0.290, 0.267,\n   0.243, 0.219, 0.195, 0.171, 0.147, 0.122,\n   0.098, 0.074, 0.049, 0.025, 0.000,-0.025,\n  -0.049,-0.074,-0.098,-0.122,-0.147,-0.171,\n  -0.195,-0.219,-0.243,-0.267,-0.290,-0.314,\n  -0.337,-0.360,-0.383,-0.405,-0.428,-0.450,\n  -0.471,-0.493,-0.514,-0.535,-0.556,-0.576,\n  -0.596,-0.615,-0.634,-0.653,-0.672,-0.690,\n  -0.707,-0.724,-0.741,-0.757,-0.773,-0.788,\n  -0.803,-0.818,-0.831,-0.845,-0.858,-0.870,\n  -0.882,-0.893,-0.904,-0.914,-0.924,-0.933,\n  -0.942,-0.950,-0.957,-0.964,-0.970,-0.976,\n  -0.981,-0.985,-0.989,-0.992,-0.995,-0.997,\n  -0.999,-1.000,-1.000,-1.000,-0.999,-0.997,\n  -0.995,-0.992,-0.989,-0.985,-0.981,-0.976,\n  -0.970,-0.964,-0.957,-0.950,-0.942,-0.933,\n  -0.924,-0.914,-0.904,-0.893,-0.882,-0.870,\n  -0.858,-0.845,-0.831,-0.818,-0.803,-0.788,\n  -0.773,-0.757,-0.741,-0.724,-0.707,-0.690,\n  -0.672,-0.653,-0.634,-0.615,-0.596,-0.576,\n  -0.556,-0.535,-0.514,-0.493,-0.471,-0.450,\n  -0.428,-0.405,-0.383,-0.360,-0.337,-0.314,\n  -0.290,-0.267,-0.243,-0.219,-0.195,-0.171,\n  -0.147,-0.122,-0.098,-0.074,-0.049,-0.025,\n  -0.000, 0.025, 0.049, 0.074, 0.098, 0.122,\n   0.147, 0.171, 0.195, 0.219, 0.243, 0.267,\n   0.290, 0.314, 0.337, 0.360, 0.383, 0.405,\n   0.428, 0.450, 0.471, 0.493, 0.514, 0.535,\n   0.556, 0.576, 0.596, 0.615, 0.634, 0.653,\n   0.672, 0.690, 0.707, 0.724, 0.741, 0.757,\n   0.773, 0.788, 0.803, 0.818, 0.831, 0.845,\n   0.858, 0.870, 0.882, 0.893, 0.904, 0.914,\n   0.924, 0.933, 0.942, 0.950, 0.957, 0.964,\n   0.970, 0.976, 0.981, 0.985, 0.989, 0.992,\n   0.995, 0.997, 0.999, 1.000);",
       }   ,
       {
       name: "Cos_Table_Size",
       qualified_name: "GESTE.Maths_Tables.Cos_Table_Size",
       signature: "geste.maths_tables.cos_table_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Cos_Table_Size : constant := 256;",
       }   ,
       {
       name: "Sine_Alpha",
       qualified_name: "GESTE.Maths_Tables.Sine_Alpha",
       signature: "geste.maths_tables.sine_alpha",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Sine_Alpha      : constant := Value (Sine_Table_Size) / (2 * 3.14159);",
       }   ,
       {
       name: "Sine_Table",
       qualified_name: "GESTE.Maths_Tables.Sine_Table",
       signature: "geste.maths_tables.sine_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Sine_Table : constant array (Unsigned_32 range 0 .. Sine_Table_Size - 1) of Value :=\n ( 0.000, 0.025, 0.049, 0.074, 0.098, 0.122,\n   0.147, 0.171, 0.195, 0.219, 0.243, 0.267,\n   0.290, 0.314, 0.337, 0.360, 0.383, 0.405,\n   0.428, 0.450, 0.471, 0.493, 0.514, 0.535,\n   0.556, 0.576, 0.596, 0.615, 0.634, 0.653,\n   0.672, 0.690, 0.707, 0.724, 0.741, 0.757,\n   0.773, 0.788, 0.803, 0.818, 0.831, 0.845,\n   0.858, 0.870, 0.882, 0.893, 0.904, 0.914,\n   0.924, 0.933, 0.942, 0.950, 0.957, 0.964,\n   0.970, 0.976, 0.981, 0.985, 0.989, 0.992,\n   0.995, 0.997, 0.999, 1.000, 1.000, 1.000,\n   0.999, 0.997, 0.995, 0.992, 0.989, 0.985,\n   0.981, 0.976, 0.970, 0.964, 0.957, 0.950,\n   0.942, 0.933, 0.924, 0.914, 0.904, 0.893,\n   0.882, 0.870, 0.858, 0.845, 0.831, 0.818,\n   0.803, 0.788, 0.773, 0.757, 0.741, 0.724,\n   0.707, 0.690, 0.672, 0.653, 0.634, 0.615,\n   0.596, 0.576, 0.556, 0.535, 0.514, 0.493,\n   0.471, 0.450, 0.428, 0.405, 0.383, 0.360,\n   0.337, 0.314, 0.290, 0.267, 0.243, 0.219,\n   0.195, 0.171, 0.147, 0.122, 0.098, 0.074,\n   0.049, 0.025, 0.000,-0.025,-0.049,-0.074,\n  -0.098,-0.122,-0.147,-0.171,-0.195,-0.219,\n  -0.243,-0.267,-0.290,-0.314,-0.337,-0.360,\n  -0.383,-0.405,-0.428,-0.450,-0.471,-0.493,\n  -0.514,-0.535,-0.556,-0.576,-0.596,-0.615,\n  -0.634,-0.653,-0.672,-0.690,-0.707,-0.724,\n  -0.741,-0.757,-0.773,-0.788,-0.803,-0.818,\n  -0.831,-0.845,-0.858,-0.870,-0.882,-0.893,\n  -0.904,-0.914,-0.924,-0.933,-0.942,-0.950,\n  -0.957,-0.964,-0.970,-0.976,-0.981,-0.985,\n  -0.989,-0.992,-0.995,-0.997,-0.999,-1.000,\n  -1.000,-1.000,-0.999,-0.997,-0.995,-0.992,\n  -0.989,-0.985,-0.981,-0.976,-0.970,-0.964,\n  -0.957,-0.950,-0.942,-0.933,-0.924,-0.914,\n  -0.904,-0.893,-0.882,-0.870,-0.858,-0.845,\n  -0.831,-0.818,-0.803,-0.788,-0.773,-0.757,\n  -0.741,-0.724,-0.707,-0.690,-0.672,-0.653,\n  -0.634,-0.615,-0.596,-0.576,-0.556,-0.535,\n  -0.514,-0.493,-0.471,-0.450,-0.428,-0.405,\n  -0.383,-0.360,-0.337,-0.314,-0.290,-0.267,\n  -0.243,-0.219,-0.195,-0.171,-0.147,-0.122,\n  -0.098,-0.074,-0.049,-0.025);",
       }   ,
       {
       name: "Sine_Table_Size",
       qualified_name: "GESTE.Maths_Tables.Sine_Table_Size",
       signature: "geste.maths_tables.sine_table_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Sine_Table_Size : constant := 256;",
       }   ,
   ]
,}
---

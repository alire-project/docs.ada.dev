---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Monitor.Block_Drivers",
qualified_name: "Monitor.Block_Drivers",
signature: "monitor.block_drivers",
enclosing: "monitor",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                        Copyright (C) 2017, AdaCore                       --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Block_Driver_Monitor",
       qualified_name: "Monitor.Block_Drivers.Block_Driver_Monitor",
       signature: "monitor.block_drivers.block_driver_monitor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Block_Driver_Monitor\n  (Driver_Under_Monitoring : not null Any_Block_Driver;\n   Put_Line                : not null Put_Line_Procedure)\nis new Block_Driver with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Put_Line_Procedure",
       qualified_name: "Monitor.Block_Drivers.Put_Line_Procedure",
       signature: "monitor.block_drivers.put_line_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Put_Line_Procedure is access procedure (Str : String);",
       }   ,
   ]
,}
---

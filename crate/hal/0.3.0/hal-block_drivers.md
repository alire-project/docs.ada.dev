---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.Block_Drivers",
qualified_name: "HAL.Block_Drivers",
signature: "hal.block_drivers",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "Block_Driver",
       qualified_name: "HAL.Block_Drivers.Block_Driver",
       signature: "hal.block_drivers.block_driver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Block_Driver is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Block_Driver",
       qualified_name: "HAL.Block_Drivers.Any_Block_Driver",
       signature: "hal.block_drivers.any_block_driver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Block_Driver is access all Block_Driver'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Block",
       qualified_name: "HAL.Block_Drivers.Block",
       signature: "hal.block_drivers.block",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Block is UInt8_Array;",
       }   ,
   ]
,constants:    [
       {
       name: "Block_Size",
       qualified_name: "HAL.Block_Drivers.Block_Size",
       signature: "hal.block_drivers.block_size",
       enclosing: "",
       is_private: false,
       documentation: "Size of a block, for block number.",
       documentation_snippet: "Block_Size : constant := 512;",
       }   ,
   ]
,}
---

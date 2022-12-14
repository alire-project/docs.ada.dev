---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Partitions",
qualified_name: "Partitions",
signature: "partitions",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Partition_Kind",
       qualified_name: "Partitions.Partition_Kind",
       signature: "partitions.partition_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Partition_Kind is new UInt8;",
       }   ,
       {
       name: "Status_Code",
       qualified_name: "Partitions.Status_Code",
       signature: "partitions.status_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status_Code is (Status_Ok, Disk_Error, Invalid_Parition);",
       }   ,
   ]
,record_types:    [
       {
       name: "CHS_Address",
       qualified_name: "Partitions.CHS_Address",
       signature: "partitions.chs_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CHS_Address is record\n   C : UInt10;\n   H : UInt8;\n   S : UInt6;\nend record with Pack, Size => 24;",
       }   ,
       {
       name: "Partition_Entry",
       qualified_name: "Partitions.Partition_Entry",
       signature: "partitions.partition_entry",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Partition_Entry is record\n   Status            : UInt8;\n   First_Sector_CHS  : CHS_Address;\n   Kind              : Partition_Kind;\n   Last_Sector_CHS   : CHS_Address;\n   First_Sector_LBA  : Logical_Block_Address;\n   Number_Of_Sectors : UInt32;\nend record with Pack, Size => 16 * 8;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Logical_Block_Address",
       qualified_name: "Partitions.Logical_Block_Address",
       signature: "partitions.logical_block_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Logical_Block_Address is UInt32;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Partition",
       qualified_name: "Partitions.Empty_Partition",
       signature: "partitions.empty_partition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Partition       : constant Partition_Kind := 16#00#;",
       }   ,
       {
       name: "Extended_LBA_Parition",
       qualified_name: "Partitions.Extended_LBA_Parition",
       signature: "partitions.extended_lba_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Extended_LBA_Parition : constant Partition_Kind := 16#0F#;",
       }   ,
       {
       name: "Extended_Parition",
       qualified_name: "Partitions.Extended_Parition",
       signature: "partitions.extended_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Extended_Parition     : constant Partition_Kind := 16#05#;",
       }   ,
       {
       name: "Fat12_Parition",
       qualified_name: "Partitions.Fat12_Parition",
       signature: "partitions.fat12_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat12_Parition        : constant Partition_Kind := 16#01#;",
       }   ,
       {
       name: "Fat16_Parition",
       qualified_name: "Partitions.Fat16_Parition",
       signature: "partitions.fat16_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat16_Parition        : constant Partition_Kind := 16#04#;",
       }   ,
       {
       name: "Fat16B_LBA_Parition",
       qualified_name: "Partitions.Fat16B_LBA_Parition",
       signature: "partitions.fat16b_lba_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat16B_LBA_Parition   : constant Partition_Kind := 16#0E#;",
       }   ,
       {
       name: "Fat16B_Parition",
       qualified_name: "Partitions.Fat16B_Parition",
       signature: "partitions.fat16b_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat16B_Parition       : constant Partition_Kind := 16#06#;",
       }   ,
       {
       name: "Fat32_CHS_Parition",
       qualified_name: "Partitions.Fat32_CHS_Parition",
       signature: "partitions.fat32_chs_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat32_CHS_Parition    : constant Partition_Kind := 16#0B#;",
       }   ,
       {
       name: "Fat32_LBA_Parition",
       qualified_name: "Partitions.Fat32_LBA_Parition",
       signature: "partitions.fat32_lba_parition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fat32_LBA_Parition    : constant Partition_Kind := 16#0C#;",
       }   ,
       {
       name: "Linux_Partition",
       qualified_name: "Partitions.Linux_Partition",
       signature: "partitions.linux_partition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Linux_Partition       : constant Partition_Kind := 16#83#;",
       }   ,
       {
       name: "Linux_Swap_Partition",
       qualified_name: "Partitions.Linux_Swap_Partition",
       signature: "partitions.linux_swap_partition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Linux_Swap_Partition  : constant Partition_Kind := 16#82#;",
       }   ,
       {
       name: "NTFS_Partition",
       qualified_name: "Partitions.NTFS_Partition",
       signature: "partitions.ntfs_partition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NTFS_Partition        : constant Partition_Kind := 16#07#;",
       }   ,
   ]
,}
---

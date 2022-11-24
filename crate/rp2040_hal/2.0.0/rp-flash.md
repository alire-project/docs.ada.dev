---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.Flash",
qualified_name: "RP.Flash",
signature: "rp.flash",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Flash_Offset",
       qualified_name: "RP.Flash.Flash_Offset",
       signature: "rp.flash.flash_offset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flash_Offset is range 0 .. Flash_Size;",
       }   ,
   ]
,constants:    [
       {
       name: "Flash_Size",
       qualified_name: "RP.Flash.Flash_Size",
       signature: "rp.flash.flash_size",
       enclosing: "",
       is_private: false,
       documentation: "XIP maps up to 16 MB of flash. Actual flash chip may be smaller.",
       documentation_snippet: "Flash_Size  : constant := 16 * 1024 * 1024;",
       }   ,
       {
       name: "Page_Size",
       qualified_name: "RP.Flash.Page_Size",
       signature: "rp.flash.page_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Page_Size   : constant := 256;",
       }   ,
       {
       name: "Sector_Size",
       qualified_name: "RP.Flash.Sector_Size",
       signature: "rp.flash.sector_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Sector_Size : constant := 4096;",
       }   ,
   ]
,}
---

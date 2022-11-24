---
crate: avrada_mcu
layout: gnatdoc
gnatdoc: {
name: "AVR.ATmega328P.Bootloader",
qualified_name: "AVR.ATmega328P.Bootloader",
signature: "avr.atmega328p.bootloader",
enclosing: "avr.atmega328p",
is_private: false,
documentation: "-------------------------------------------------------------------------\n The AVR-Ada Library is free software;  you can redistribute it and/or --\n modify it under terms of the  GNU General Public License as published --\n by  the  Free Software  Foundation;  either  version 2, or  (at  your --\n option) any later version.  The AVR-Ada Library is distributed in the --\n hope that it will be useful, but  WITHOUT ANY WARRANTY;  without even --\n the  implied warranty of MERCHANTABILITY or FITNESS FOR A  PARTICULAR --\n PURPOSE. See the GNU General Public License for more details.         --\n                                                                       --\n As a special exception, if other files instantiate generics from this --\n unit,  or  you  link  this  unit  with  other  files  to  produce  an --\n executable   this  unit  does  not  by  itself  cause  the  resulting --\n executable to  be  covered by the  GNU General  Public License.  This --\n exception does  not  however  invalidate  any  other reasons why  the --\n executable file might be covered by the GNU Public License.           --\n-------------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Boot_Info_Array",
       qualified_name: "AVR.ATmega328P.Bootloader.Boot_Info_Array",
       signature: "avr.atmega328p.bootloader.boot_info_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Boot_Info_Array is array (Unsigned_8 range <>) of Boot_Info_Type;",
       }   ,
   ]
,record_types:    [
       {
       name: "Boot_Info_Type",
       qualified_name: "AVR.ATmega328P.Bootloader.Boot_Info_Type",
       signature: "avr.atmega328p.bootloader.boot_info_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Boot_Info_Type is record\n   Pages : Unsigned_8;\n   Start : System.Address;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Boot_Info",
       qualified_name: "AVR.ATmega328P.Bootloader.Boot_Info",
       signature: "avr.atmega328p.bootloader.boot_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Boot_Info : constant Boot_Info_Array :=\n  ( 1 => (Pages => 4, Start => 16#3F00#) ,\n    2 => (Pages => 8, Start => 16#3E00#) ,\n    3 => (Pages => 16, Start => 16#3C00#) ,\n    4 => (Pages => 32, Start => 16#3800#) );",
       }   ,
       {
       name: "CVS_Version",
       qualified_name: "AVR.ATmega328P.Bootloader.CVS_Version",
       signature: "avr.atmega328p.bootloader.cvs_version",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CVS_Version : constant String := \"$Id$\";",
       }   ,
       {
       name: "nrww_End",
       qualified_name: "AVR.ATmega328P.Bootloader.nrww_End",
       signature: "avr.atmega328p.bootloader.nrww_end",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "nrww_End   : constant := 16#3fff#;",
       }   ,
       {
       name: "nrww_Start",
       qualified_name: "AVR.ATmega328P.Bootloader.nrww_Start",
       signature: "avr.atmega328p.bootloader.nrww_start",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "nrww_Start : constant := 16#3800#;",
       }   ,
       {
       name: "Pagesize",
       qualified_name: "AVR.ATmega328P.Bootloader.Pagesize",
       signature: "avr.atmega328p.bootloader.pagesize",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Pagesize   : constant := 128;",
       }   ,
       {
       name: "rww_End",
       qualified_name: "AVR.ATmega328P.Bootloader.rww_End",
       signature: "avr.atmega328p.bootloader.rww_end",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "rww_End    : constant := 16#37ff#;",
       }   ,
       {
       name: "rww_Start",
       qualified_name: "AVR.ATmega328P.Bootloader.rww_Start",
       signature: "avr.atmega328p.bootloader.rww_start",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "rww_Start  : constant := 16#0000#;",
       }   ,
   ]
,}
---

---
crate: trendy_terminal
layout: gnatdoc
gnatdoc: {
name: "Trendy_Terminal.Linux",
qualified_name: "Trendy_Terminal.Linux",
signature: "trendy_terminal.linux",
enclosing: "trendy_terminal",
is_private: false,
documentation: "-------------------------------------------------------------------------\n Interfacing with C\n-------------------------------------------------------------------------\n Crash course in how this works.\n https://en.wikibooks.org/wiki/Ada_Programming/Types/access#Access_vs._System.Address",
documentation_snippet: "",
simple_types:    [
       {
       name: "Application_Time",
       qualified_name: "Trendy_Terminal.Linux.Application_Time",
       signature: "trendy_terminal.linux.application_time",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum TCSANOW\n  immediate effect\n@enum TCSADRAIN\n  after all output written\n@enum TCSAFLUSH\n  like drain, except input received as well",
       documentation_snippet: "type Application_Time is\n    (TCSANOW,\n     TCSADRAIN,\n     TCSAFLUSH\n);",
       }   ,
       {
       name: "BOOL",
       qualified_name: "Trendy_Terminal.Linux.BOOL",
       signature: "trendy_terminal.linux.bool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BOOL is new Interfaces.C.int;",
       }   ,
       {
       name: "c_lflag_bit",
       qualified_name: "Trendy_Terminal.Linux.c_lflag_bit",
       signature: "trendy_terminal.linux.c_lflag_bit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type c_lflag_bit is (ISIG,\n                   ICANON,\n                   XCASE,\n                   ECHO,\n                   ECHOE,\n                   ECHOK,\n                   ECHONL,\n                   NOFLSH,\n                   TOSTOP,\n                   ECHOCTL,\n                   ECHOPRT,\n                   ECHOKE,\n                   FLUSHO,\n                   PENDIN,\n                   IEXTEN,\n                   EXTPROC)\n   with Size => tcflag_t'Size;",
       }   ,
       {
       name: "cc_t",
       qualified_name: "Trendy_Terminal.Linux.cc_t",
       signature: "trendy_terminal.linux.cc_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type cc_t is new Interfaces.C.unsigned_char;",
       }   ,
       {
       name: "FD",
       qualified_name: "Trendy_Terminal.Linux.FD",
       signature: "trendy_terminal.linux.fd",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FD is new Interfaces.C.int;",
       }   ,
       {
       name: "FILE_Ptr",
       qualified_name: "Trendy_Terminal.Linux.FILE_Ptr",
       signature: "trendy_terminal.linux.file_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FILE_Ptr is new System.Address;",
       }   ,
       {
       name: "speed_t",
       qualified_name: "Trendy_Terminal.Linux.speed_t",
       signature: "trendy_terminal.linux.speed_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type speed_t is new Interfaces.C.unsigned;",
       }   ,
       {
       name: "tcflag_t",
       qualified_name: "Trendy_Terminal.Linux.tcflag_t",
       signature: "trendy_terminal.linux.tcflag_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type tcflag_t is new Interfaces.C.unsigned;",
       }   ,
   ]
,array_types:    [
       {
       name: "c_lflag_t",
       qualified_name: "Trendy_Terminal.Linux.c_lflag_t",
       signature: "trendy_terminal.linux.c_lflag_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type c_lflag_t is array (c_lflag_bit) of Boolean with\n    Pack,\n    Size => tcflag_t'Size;",
       }   ,
       {
       name: "cc_array",
       qualified_name: "Trendy_Terminal.Linux.cc_array",
       signature: "trendy_terminal.linux.cc_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type cc_array is array (Natural range 0 .. NCCS - 1) of cc_t with Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Termios",
       qualified_name: "Trendy_Terminal.Linux.Termios",
       signature: "trendy_terminal.linux.termios",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Termios is record\n    c_iflag  : tcflag_t;\n    c_oflag  : tcflag_t;\n    c_cflag  : tcflag_t;\n    c_lflag  : c_lflag_t;\n    c_line   : cc_t;\n    c_cc     : cc_array;\n    c_ispeed : speed_t;\n    c_ospeed : speed_t;\nend record with\n    Convention => C;",
       }   ,
   ]
,constants:    [
       {
       name: "NCCS",
       qualified_name: "Trendy_Terminal.Linux.NCCS",
       signature: "trendy_terminal.linux.nccs",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NCCS : constant := 32;",
       }   ,
   ]
,variables:    [
       {
       name: "stderr",
       qualified_name: "Trendy_Terminal.Linux.stderr",
       signature: "trendy_terminal.linux.stderr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "stderr : aliased FILE_Ptr;",
       }   ,
       {
       name: "stdin",
       qualified_name: "Trendy_Terminal.Linux.stdin",
       signature: "trendy_terminal.linux.stdin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "stdin  : aliased FILE_Ptr;",
       }   ,
       {
       name: "stdout",
       qualified_name: "Trendy_Terminal.Linux.stdout",
       signature: "trendy_terminal.linux.stdout",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "stdout : aliased FILE_Ptr;",
       }   ,
   ]
,}
---

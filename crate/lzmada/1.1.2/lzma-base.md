---
crate: lzmada
layout: gnatdoc
gnatdoc: {
name: "Lzma.Base",
qualified_name: "Lzma.Base",
signature: "lzma.base",
enclosing: "lzma",
is_private: false,
documentation: "  unsupported macro: LZMA_STREAM_INIT { NULL, 0, 0, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, LZMA_RESERVED_ENUM, LZMA_RESERVED_ENUM }\n*\n * \\file        lzma/base.h\n * \\brief       Data types and functions used in many places in liblzma API",
documentation_snippet: "",
simple_types:    [
       {
       name: "lzma_action",
       qualified_name: "Lzma.Base.lzma_action",
       signature: "lzma.base.lzma_action",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum LZMA_RUN\n@enum LZMA_SYNC_FLUSH\n@enum LZMA_FULL_FLUSH\n@enum LZMA_FINISH\n  /usr/include/lzma/base.h:322",
       documentation_snippet: "type lzma_action is\n  (LZMA_RUN,\n   LZMA_SYNC_FLUSH,\n   LZMA_FULL_FLUSH,\n   LZMA_FINISH);",
       }   ,
       {
       name: "lzma_reserved_enum_type",
       qualified_name: "Lzma.Base.lzma_reserved_enum_type",
       signature: "lzma.base.lzma_reserved_enum_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum LZMA_RESERVED_ENUM\n  /usr/include/lzma/base.h:46",
       documentation_snippet: "type lzma_reserved_enum_type is\n  (LZMA_RESERVED_ENUM);",
       }   ,
       {
       name: "lzma_ret",
       qualified_name: "Lzma.Base.lzma_ret",
       signature: "lzma.base.lzma_ret",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum LZMA_OK\n@enum LZMA_STREAM_END\n@enum LZMA_NO_CHECK\n@enum LZMA_UNSUPPORTED_CHECK\n@enum LZMA_GET_CHECK\n@enum LZMA_MEM_ERROR\n@enum LZMA_MEMLIMIT_ERROR\n@enum LZMA_FORMAT_ERROR\n@enum LZMA_OPTIONS_ERROR\n@enum LZMA_DATA_ERROR\n@enum LZMA_BUF_ERROR\n@enum LZMA_PROG_ERROR\n  /usr/include/lzma/base.h:237",
       documentation_snippet: "type lzma_ret is\n  (LZMA_OK,\n   LZMA_STREAM_END,\n   LZMA_NO_CHECK,\n   LZMA_UNSUPPORTED_CHECK,\n   LZMA_GET_CHECK,\n   LZMA_MEM_ERROR,\n   LZMA_MEMLIMIT_ERROR,\n   LZMA_FORMAT_ERROR,\n   LZMA_OPTIONS_ERROR,\n   LZMA_DATA_ERROR,\n   LZMA_BUF_ERROR,\n   LZMA_PROG_ERROR);",
       }   ,
   ]
,record_types:    [
       {
       name: "lzma_allocator",
       qualified_name: "Lzma.Base.lzma_allocator",
       signature: "lzma.base.lzma_allocator",
       enclosing: "",
       is_private: false,
       documentation: "\n@field alloc\n  /usr/include/lzma/base.h:384\n@field free\n  /usr/include/lzma/base.h:398\n@field opaque\n  /usr/include/lzma/base.h:409\n  /usr/include/lzma/base.h:411",
       documentation_snippet: "type lzma_allocator is record\n   alloc : access function\n        (arg1 : System.Address;\n         arg2 : Interfaces.C.size_t;\n         arg3 : Interfaces.C.size_t) return System.Address;\n   free : access procedure (arg1 : System.Address; arg2 : System.Address);\n   opaque : System.Address;\nend record;",
       }   ,
       {
       name: "lzma_stream",
       qualified_name: "Lzma.Base.lzma_stream",
       signature: "lzma.base.lzma_stream",
       enclosing: "",
       is_private: false,
       documentation: "\n@field next_in\n  /usr/include/lzma/base.h:462\n@field avail_in\n  /usr/include/lzma/base.h:463\n@field total_in\n  /usr/include/lzma/base.h:464\n@field next_out\n  /usr/include/lzma/base.h:466\n@field avail_out\n  /usr/include/lzma/base.h:467\n@field total_out\n  /usr/include/lzma/base.h:468\n@field allocator\n  /usr/include/lzma/base.h:476\n@field internal\n  /usr/include/lzma/base.h:479\n@field reserved_ptr1\n  /usr/include/lzma/base.h:487\n@field reserved_ptr2\n  /usr/include/lzma/base.h:488\n@field reserved_ptr3\n  /usr/include/lzma/base.h:489\n@field reserved_ptr4\n  /usr/include/lzma/base.h:490\n@field reserved_int1\n  /usr/include/lzma/base.h:491\n@field reserved_int2\n  /usr/include/lzma/base.h:492\n@field reserved_int3\n  /usr/include/lzma/base.h:493\n@field reserved_int4\n  /usr/include/lzma/base.h:494\n@field reserved_enum1\n  /usr/include/lzma/base.h:495\n@field reserved_enum2\n  /usr/include/lzma/base.h:496",
       documentation_snippet: "type lzma_stream is record\n   next_in : access Ada.Streams.Stream_Element;\n   avail_in : aliased Interfaces.C.size_t;\n   total_in : aliased Long_Long_Integer;\n   next_out : access Ada.Streams.Stream_Element;\n   avail_out : aliased Interfaces.C.size_t;\n   total_out : aliased Long_Long_Integer;\n   allocator : access lzma_allocator;\n   internal : System.Address;\n   reserved_ptr1 : System.Address;\n   reserved_ptr2 : System.Address;\n   reserved_ptr3 : System.Address;\n   reserved_ptr4 : System.Address;\n   reserved_int1 : aliased Long_Long_Integer;\n   reserved_int2 : aliased Long_Long_Integer;\n   reserved_int3 : aliased Interfaces.C.size_t;\n   reserved_int4 : aliased Interfaces.C.size_t;\n   reserved_enum1 : aliased lzma_reserved_enum_type;\n   reserved_enum2 : aliased lzma_reserved_enum_type;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "lzma_bool",
       qualified_name: "Lzma.Base.lzma_bool",
       signature: "lzma.base.lzma_bool",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/base.h:29",
       documentation_snippet: "subtype lzma_bool is unsigned_char;",
       }   ,
   ]
,constants:    [
       {
       name: "LZMA_STREAM_INIT",
       qualified_name: "Lzma.Base.LZMA_STREAM_INIT",
       signature: "lzma.base.lzma_stream_init",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/base.h:498",
       documentation_snippet: "LZMA_STREAM_INIT : constant lzma_stream :=\n  (next_in => null, avail_in => 0, total_in => 0,\n   next_out => null, avail_out => 0, total_out => 0, allocator => null,\n   internal => System.Null_Address, reserved_ptr1 => System.Null_Address,\n   reserved_ptr2 => System.Null_Address, reserved_ptr3 => System.Null_Address,\n   reserved_ptr4 => System.Null_Address, reserved_enum1 => LZMA_RESERVED_ENUM,\n   reserved_enum2 => LZMA_RESERVED_ENUM, reserved_int1 => 0,\n   reserved_int2 => 0, others => 0);",
       }   ,
   ]
,}
---

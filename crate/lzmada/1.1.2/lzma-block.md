---
crate: lzmada
layout: gnatdoc
gnatdoc: {
name: "Lzma.Block",
qualified_name: "Lzma.Block",
signature: "lzma.block",
enclosing: "lzma",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "lzma_block_raw_check_array",
       qualified_name: "Lzma.Block.lzma_block_raw_check_array",
       signature: "lzma.block.lzma_block_raw_check_array",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/block.h:245",
       documentation_snippet: "type lzma_block_raw_check_array is array (0 .. 63) of aliased Ada.Streams.Stream_Element;",
       }   ,
   ]
,record_types:    [
       {
       name: "lzma_block",
       qualified_name: "Lzma.Block.lzma_block",
       signature: "lzma.block.lzma_block",
       enclosing: "",
       is_private: false,
       documentation: "\n@field version\n  /usr/include/lzma/block.h:47\n@field header_size\n  /usr/include/lzma/block.h:67\n@field check\n  /usr/include/lzma/block.h:88\n@field compressed_size\n  /usr/include/lzma/block.h:143\n@field uncompressed_size\n  /usr/include/lzma/block.h:167\n@field filters\n  /usr/include/lzma/block.h:195\n@field raw_check\n  /usr/include/lzma/block.h:212\n@field reserved_ptr1\n  /usr/include/lzma/block.h:221\n@field reserved_ptr2\n  /usr/include/lzma/block.h:222\n@field reserved_ptr3\n  /usr/include/lzma/block.h:223\n@field reserved_int1\n  /usr/include/lzma/block.h:224\n@field reserved_int2\n  /usr/include/lzma/block.h:225\n@field reserved_int3\n  /usr/include/lzma/block.h:226\n@field reserved_int4\n  /usr/include/lzma/block.h:227\n@field reserved_int5\n  /usr/include/lzma/block.h:228\n@field reserved_int6\n  /usr/include/lzma/block.h:229\n@field reserved_int7\n  /usr/include/lzma/block.h:230\n@field reserved_int8\n  /usr/include/lzma/block.h:231\n@field reserved_enum1\n  /usr/include/lzma/block.h:232\n@field reserved_enum2\n  /usr/include/lzma/block.h:233\n@field reserved_enum3\n  /usr/include/lzma/block.h:234\n@field reserved_enum4\n  /usr/include/lzma/block.h:235\n@field reserved_bool1\n  /usr/include/lzma/block.h:236\n@field reserved_bool2\n  /usr/include/lzma/block.h:237\n@field reserved_bool3\n  /usr/include/lzma/block.h:238\n@field reserved_bool4\n  /usr/include/lzma/block.h:239\n@field reserved_bool5\n  /usr/include/lzma/block.h:240\n@field reserved_bool6\n  /usr/include/lzma/block.h:241\n@field reserved_bool7\n  /usr/include/lzma/block.h:242\n@field reserved_bool8\n  /usr/include/lzma/block.h:243\n  /usr/include/lzma/block.h:245",
       documentation_snippet: "type lzma_block is record\n   version : aliased Interfaces.C.unsigned;\n   header_size : aliased Interfaces.C.unsigned;\n   check : aliased Lzma.Check.lzma_check;\n   compressed_size : aliased Lzma.Vli.lzma_vli;\n   uncompressed_size : aliased Lzma.Vli.lzma_vli;\n   filters : access Lzma.Filter.lzma_filter;\n   raw_check : aliased lzma_block_raw_check_array;\n   reserved_ptr1 : System.Address;\n   reserved_ptr2 : System.Address;\n   reserved_ptr3 : System.Address;\n   reserved_int1 : aliased Interfaces.C.unsigned;\n   reserved_int2 : aliased Interfaces.C.unsigned;\n   reserved_int3 : aliased Lzma.Vli.lzma_vli;\n   reserved_int4 : aliased Lzma.Vli.lzma_vli;\n   reserved_int5 : aliased Lzma.Vli.lzma_vli;\n   reserved_int6 : aliased Lzma.Vli.lzma_vli;\n   reserved_int7 : aliased Lzma.Vli.lzma_vli;\n   reserved_int8 : aliased Lzma.Vli.lzma_vli;\n   reserved_enum1 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum2 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum3 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum4 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_bool1 : aliased Lzma.Base.lzma_bool;\n   reserved_bool2 : aliased Lzma.Base.lzma_bool;\n   reserved_bool3 : aliased Lzma.Base.lzma_bool;\n   reserved_bool4 : aliased Lzma.Base.lzma_bool;\n   reserved_bool5 : aliased Lzma.Base.lzma_bool;\n   reserved_bool6 : aliased Lzma.Base.lzma_bool;\n   reserved_bool7 : aliased Lzma.Base.lzma_bool;\n   reserved_bool8 : aliased Lzma.Base.lzma_bool;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "LZMA_BLOCK_HEADER_SIZE_MAX",
       qualified_name: "Lzma.Block.LZMA_BLOCK_HEADER_SIZE_MAX",
       signature: "lzma.block.lzma_block_header_size_max",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/block.h:69\narg-macro: function lzma_block_header_size_decode (((uint32_t)(b) + 1) * 4\n  return ((uint32_t)(b) + 1) * 4;",
       documentation_snippet: "LZMA_BLOCK_HEADER_SIZE_MAX : constant := 1024;",
       }   ,
       {
       name: "LZMA_BLOCK_HEADER_SIZE_MIN",
       qualified_name: "Lzma.Block.LZMA_BLOCK_HEADER_SIZE_MIN",
       signature: "lzma.block.lzma_block_header_size_min",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/block.h:69\narg-macro: function lzma_block_header_size_decode (((uint32_t)(b) + 1) * 4\n  return ((uint32_t)(b) + 1) * 4;",
       documentation_snippet: "LZMA_BLOCK_HEADER_SIZE_MIN : constant := 8;",
       }   ,
   ]
,}
---

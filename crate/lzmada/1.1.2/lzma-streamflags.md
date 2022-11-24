---
crate: lzmada
layout: gnatdoc
gnatdoc: {
name: "Lzma.StreamFlags",
qualified_name: "Lzma.StreamFlags",
signature: "lzma.streamflags",
enclosing: "lzma",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "lzma_stream_flags",
       qualified_name: "Lzma.StreamFlags.lzma_stream_flags",
       signature: "lzma.streamflags.lzma_stream_flags",
       enclosing: "",
       is_private: false,
       documentation: "\n@field version\n  /usr/include/lzma/stream_flags.h:51\n@field backward_size\n  /usr/include/lzma/stream_flags.h:69\n@field check\n  /usr/include/lzma/stream_flags.h:79\n@field reserved_enum1\n  /usr/include/lzma/stream_flags.h:90\n@field reserved_enum2\n  /usr/include/lzma/stream_flags.h:91\n@field reserved_enum3\n  /usr/include/lzma/stream_flags.h:92\n@field reserved_enum4\n  /usr/include/lzma/stream_flags.h:93\n@field reserved_bool1\n  /usr/include/lzma/stream_flags.h:94\n@field reserved_bool2\n  /usr/include/lzma/stream_flags.h:95\n@field reserved_bool3\n  /usr/include/lzma/stream_flags.h:96\n@field reserved_bool4\n  /usr/include/lzma/stream_flags.h:97\n@field reserved_bool5\n  /usr/include/lzma/stream_flags.h:98\n@field reserved_bool6\n  /usr/include/lzma/stream_flags.h:99\n@field reserved_bool7\n  /usr/include/lzma/stream_flags.h:100\n@field reserved_bool8\n  /usr/include/lzma/stream_flags.h:101\n@field reserved_int1\n  /usr/include/lzma/stream_flags.h:102\n@field reserved_int2\n  /usr/include/lzma/stream_flags.h:103\n  /usr/include/lzma/stream_flags.h:105",
       documentation_snippet: "type lzma_stream_flags is record\n   version : aliased Interfaces.C.unsigned;\n   backward_size : aliased Lzma.Vli.lzma_vli;\n   check : aliased Lzma.Check.lzma_check;\n   reserved_enum1 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum2 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum3 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_enum4 : aliased Lzma.Base.lzma_reserved_enum_type;\n   reserved_bool1 : aliased Lzma.Base.lzma_bool;\n   reserved_bool2 : aliased Lzma.Base.lzma_bool;\n   reserved_bool3 : aliased Lzma.Base.lzma_bool;\n   reserved_bool4 : aliased Lzma.Base.lzma_bool;\n   reserved_bool5 : aliased Lzma.Base.lzma_bool;\n   reserved_bool6 : aliased Lzma.Base.lzma_bool;\n   reserved_bool7 : aliased Lzma.Base.lzma_bool;\n   reserved_bool8 : aliased Lzma.Base.lzma_bool;\n   reserved_int1 : aliased Interfaces.C.unsigned;\n   reserved_int2 : aliased Interfaces.C.unsigned;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "LZMA_BACKWARD_SIZE_MIN",
       qualified_name: "Lzma.StreamFlags.LZMA_BACKWARD_SIZE_MIN",
       signature: "lzma.streamflags.lzma_backward_size_min",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/stream_flags.h:70\nunsupported macro: LZMA_BACKWARD_SIZE_MAX (LZMA_VLI_C(1) << 34)",
       documentation_snippet: "LZMA_BACKWARD_SIZE_MIN : constant := 4;",
       }   ,
       {
       name: "LZMA_STREAM_HEADER_SIZE",
       qualified_name: "Lzma.StreamFlags.LZMA_STREAM_HEADER_SIZE",
       signature: "lzma.streamflags.lzma_stream_header_size",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/stream_flags.h:27",
       documentation_snippet: "LZMA_STREAM_HEADER_SIZE : constant := 12;",
       }   ,
   ]
,}
---

---
crate: bbqueue
layout: gnatdoc
gnatdoc: {
name: "BBqueue.Buffers",
qualified_name: "BBqueue.Buffers",
signature: "bbqueue.buffers",
enclosing: "bbqueue",
is_private: false,
documentation: "This unit is based on BBqueue.Offsets_Only and embeds an internal buffer.\nIt provides directly usable slices of memory from its internal buffer:\n\n   Q   : aliased Buffer (64);\n   WG  : Write_Grant := Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8);\n   if State (WG) = Valid then\n      declare\n         B : Storage_Array (1 .. Slice (WG).Length)\n           with Address => Slice (WG).Addr;\n      begin\n         B := (others => 42);\n      end;\n      Commit (Q, WG);\n   end if;",
documentation_snippet: "",
simple_types:    [
       {
       name: "Buffer",
       qualified_name: "BBqueue.Buffers.Buffer",
       signature: "bbqueue.buffers.buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer (Size   : Buffer_Size)\nis limited private;",
       }   ,
       {
       name: "Read_Grant",
       qualified_name: "BBqueue.Buffers.Read_Grant",
       signature: "bbqueue.buffers.read_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Read_Grant is limited private;",
       }   ,
       {
       name: "Write_Grant",
       qualified_name: "BBqueue.Buffers.Write_Grant",
       signature: "bbqueue.buffers.write_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Grant is limited private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Slice_Rec",
       qualified_name: "BBqueue.Buffers.Slice_Rec",
       signature: "bbqueue.buffers.slice_rec",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Slice_Rec is record\n   Length : Count;\n   Addr   : System.Address;\nend record;",
       }   ,
   ]
,}
---

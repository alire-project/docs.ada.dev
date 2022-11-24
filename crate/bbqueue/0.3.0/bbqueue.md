---
crate: bbqueue
layout: gnatdoc
gnatdoc: {
name: "BBqueue",
qualified_name: "BBqueue",
signature: "bbqueue",
enclosing: "",
is_private: false,
documentation: "Based on James Munns' https://github.com/jamesmunns/bbqueue\n\nBBqueue implements lock free, one producer one consumer, BipBuffers.\n\nThis unit only handles index offsets without having an internal buffer.\nIt can be used to allocate slices of an existing array, e.g.:\n\n   Buf : Storage_Array (8 .. 64) := (others => 0);\n   Q   : aliased Offsets_Only (Buf'Length);\n   WG  : Write_Grant := BBqueue.Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8);\n   if State (WG) = Valid then\n      S := Slice (WG);\n      Buf (Buf'First + S.From .. Buf'First + S.To) := (others => 42);\n      Commit (Q, WG);\n   end if;",
documentation_snippet: "",
simple_types:    [
       {
       name: "Offsets_Only",
       qualified_name: "BBqueue.Offsets_Only",
       signature: "bbqueue.offsets_only",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Offsets_Only (Size : Buffer_Size) is limited private;",
       }   ,
       {
       name: "Read_Grant",
       qualified_name: "BBqueue.Read_Grant",
       signature: "bbqueue.read_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Read_Grant is limited private;",
       }   ,
       {
       name: "Result_Kind",
       qualified_name: "BBqueue.Result_Kind",
       signature: "bbqueue.result_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Result_Kind is (Valid, Grant_In_Progress, Insufficient_Size, Empty);",
       }   ,
       {
       name: "Write_Grant",
       qualified_name: "BBqueue.Write_Grant",
       signature: "bbqueue.write_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Grant is limited private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Slice_Rec",
       qualified_name: "BBqueue.Slice_Rec",
       signature: "bbqueue.slice_rec",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Slice_Rec is record\n   Length : Count;\n   From   : Buffer_Offset;\n   To     : Buffer_Offset;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Buffer_Offset",
       qualified_name: "BBqueue.Buffer_Offset",
       signature: "bbqueue.buffer_offset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Buffer_Offset is Storage_Offset range 0 .. Count'Last - 1;",
       }   ,
       {
       name: "Buffer_Size",
       qualified_name: "BBqueue.Buffer_Size",
       signature: "bbqueue.buffer_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Buffer_Size is Count range 1 .. Count'Last;",
       }   ,
       {
       name: "Count",
       qualified_name: "BBqueue.Count",
       signature: "bbqueue.count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Count is Storage_Count;",
       }   ,
   ]
,}
---

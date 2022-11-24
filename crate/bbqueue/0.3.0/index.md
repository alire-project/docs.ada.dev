---
crate: bbqueue
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "BBqueue",
    qualified_name: "BBqueue",
    signature: "bbqueue",
    enclosing: "",
    is_private: false,
    documentation: "Based on James Munns' https://github.com/jamesmunns/bbqueue\n\nBBqueue implements lock free, one producer one consumer, BipBuffers.\n\nThis unit only handles index offsets without having an internal buffer.\nIt can be used to allocate slices of an existing array, e.g.:\n\n   Buf : Storage_Array (8 .. 64) := (others => 0);\n   Q   : aliased Offsets_Only (Buf'Length);\n   WG  : Write_Grant := BBqueue.Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8);\n   if State (WG) = Valid then\n      S := Slice (WG);\n      Buf (Buf'First + S.From .. Buf'First + S.To) := (others => 42);\n      Commit (Q, WG);\n   end if;",
    documentation_snippet: "",
    },
    {
    name: "BBqueue.Buffers",
    qualified_name: "BBqueue.Buffers",
    signature: "bbqueue.buffers",
    enclosing: "bbqueue",
    is_private: false,
    documentation: "This unit is based on BBqueue.Offsets_Only and embeds an internal buffer.\nIt provides directly usable slices of memory from its internal buffer:\n\n   Q   : aliased Buffer (64);\n   WG  : Write_Grant := Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8);\n   if State (WG) = Valid then\n      declare\n         B : Storage_Array (1 .. Slice (WG).Length)\n           with Address => Slice (WG).Addr;\n      begin\n         B := (others => 42);\n      end;\n      Commit (Q, WG);\n   end if;",
    documentation_snippet: "",
    },
    {
    name: "BBqueue.Buffers.framed",
    qualified_name: "BBqueue.Buffers.framed",
    signature: "bbqueue.buffers.framed",
    enclosing: "bbqueue.buffers",
    is_private: false,
    documentation: "This unit is based on BBqueue.Buffers and uses markers in the buffer to\ntrack the size of each commited write grants. The size of consequent read\ngrants will conrespond to the sizes of commited write grants.\n\nIt can be used to handle variable lenght packets:\n\n   Q   : aliased Framed_Buffer (64);\n   WG  : Write_Grant := Empty;\n   RG  : Read_Grant := Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8); -- Get a worst case grant of size 8\n   Commit (Q, WG, 4); -- Only commit 4\n   Grant (Q, WG, 8); -- Get a worst case grant of size 8\n   Commit (Q, WG, 5); -- Only commit 5\n   Read (W, RG); -- Returns a grant of size 4",
    documentation_snippet: "",
    },
]
}
---

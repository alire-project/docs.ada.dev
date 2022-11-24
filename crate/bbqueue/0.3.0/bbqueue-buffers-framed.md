---
crate: bbqueue
layout: gnatdoc
gnatdoc: {
name: "BBqueue.Buffers.framed",
qualified_name: "BBqueue.Buffers.framed",
signature: "bbqueue.buffers.framed",
enclosing: "bbqueue.buffers",
is_private: false,
documentation: "This unit is based on BBqueue.Buffers and uses markers in the buffer to\ntrack the size of each commited write grants. The size of consequent read\ngrants will conrespond to the sizes of commited write grants.\n\nIt can be used to handle variable lenght packets:\n\n   Q   : aliased Framed_Buffer (64);\n   WG  : Write_Grant := Empty;\n   RG  : Read_Grant := Empty;\n   S   : Slice_Rec;\nbegin\n   Grant (Q, WG, 8); -- Get a worst case grant of size 8\n   Commit (Q, WG, 4); -- Only commit 4\n   Grant (Q, WG, 8); -- Get a worst case grant of size 8\n   Commit (Q, WG, 5); -- Only commit 5\n   Read (W, RG); -- Returns a grant of size 4",
documentation_snippet: "",
simple_types:    [
       {
       name: "Framed_Buffer",
       qualified_name: "BBqueue.Buffers.framed.Framed_Buffer",
       signature: "bbqueue.buffers.framed.framed_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Framed_Buffer (Size   : Buffer_Size)\nis limited private;",
       }   ,
       {
       name: "Read_Grant",
       qualified_name: "BBqueue.Buffers.framed.Read_Grant",
       signature: "bbqueue.buffers.framed.read_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Read_Grant is limited private;",
       }   ,
       {
       name: "Write_Grant",
       qualified_name: "BBqueue.Buffers.framed.Write_Grant",
       signature: "bbqueue.buffers.framed.write_grant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Grant is limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Framed_Count",
       qualified_name: "BBqueue.Buffers.framed.Framed_Count",
       signature: "bbqueue.buffers.framed.framed_count",
       enclosing: "",
       is_private: false,
       documentation: "The frame can take up to 9 bytes in addition to the allocated size. The\nsize of what can be allocated is therefore lower than for a non-framed\nbuffer.",
       documentation_snippet: "subtype Framed_Count\n  is Count range Count'First .. Count'Last - Max_Frame_Header_Size;",
       }   ,
   ]
,constants:    [
       {
       name: "Max_Frame_Header_Size",
       qualified_name: "BBqueue.Buffers.framed.Max_Frame_Header_Size",
       signature: "bbqueue.buffers.framed.max_frame_header_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Frame_Header_Size : constant := 9;",
       }   ,
   ]
,}
---

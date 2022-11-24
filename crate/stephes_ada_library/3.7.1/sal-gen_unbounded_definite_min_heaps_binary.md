---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Binary",
qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Binary",
signature: "sal.gen_unbounded_definite_min_heaps_binary",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nAn unbounded minimum binary heap of definite non-limited elements.\n\nReferences:\n\n[1] Introduction to Algorithms, Third Edition. Thomas H. Cormen,\nCharles E. Leiserson, Ronald L. Rivest, Clifford Stein. Chapter 6.\n\nCopyright (C) 2017 Stephen Leake.  All Rights Reserved.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Key_Type\n@formal Key\n@formal Set_Key\n@formal \"<\"\n@formal Initial_Size\n  Initial internal data array size.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Heap_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Binary.Heap_Type",
       signature: "sal.gen_unbounded_definite_min_heaps_binary.heap_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Heap_Type is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Heap",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Binary.Empty_Heap",
       signature: "sal.gen_unbounded_definite_min_heaps_binary.empty_heap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Heap : constant Heap_Type;",
       }   ,
   ]
,}
---

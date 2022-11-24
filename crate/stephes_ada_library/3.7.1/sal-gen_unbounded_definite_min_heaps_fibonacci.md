---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci",
qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci",
signature: "sal.gen_unbounded_definite_min_heaps_fibonacci",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nAn unbounded minimum Fibonacci heap of definite non-limited elements.\n\nReferences:\n\n[1] Introduction to Algorithms, Third Edition. Thomas H. Cormen,\nCharles E. Leiserson, Ronald L. Rivest, Clifford Stein. Chapter 19.\n\nCopyright (C) 2017 - 2022 Free Software Foundation, Inc.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Key_Type\n@formal Key\n@formal Set_Key\n@formal \"<\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_min_heaps_fibonacci.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci.Variable_Reference_Type",
       signature: "sal.gen_unbounded_definite_min_heaps_fibonacci.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Heap_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci.Heap_Type",
       signature: "sal.gen_unbounded_definite_min_heaps_fibonacci.heap_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Heap_Type is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Heap",
       qualified_name: "SAL.Gen_Unbounded_Definite_Min_Heaps_Fibonacci.Empty_Heap",
       signature: "sal.gen_unbounded_definite_min_heaps_fibonacci.empty_heap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Heap : constant Heap_Type;",
       }   ,
   ]
,}
---

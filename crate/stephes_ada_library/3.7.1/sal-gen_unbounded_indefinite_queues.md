---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Indefinite_Queues",
qualified_name: "SAL.Gen_Unbounded_Indefinite_Queues",
signature: "sal.gen_unbounded_indefinite_queues",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nAn unbounded queue of indefinite non-limited elements.\n\nCopyright (C) 2017, 2019 Stephen Leake.  All Rights Reserved.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Indefinite_Queues.Constant_Reference_Type",
       signature: "sal.gen_unbounded_indefinite_queues.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private\nwith Implicit_Dereference => Element;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Indefinite_Queues.Variable_Reference_Type",
       signature: "sal.gen_unbounded_indefinite_queues.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private\nwith Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Queue_Type",
       qualified_name: "SAL.Gen_Unbounded_Indefinite_Queues.Queue_Type",
       signature: "sal.gen_unbounded_indefinite_queues.queue_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Queue_Type is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Queue",
       qualified_name: "SAL.Gen_Unbounded_Indefinite_Queues.Empty_Queue",
       signature: "sal.gen_unbounded_indefinite_queues.empty_queue",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Queue : constant Queue_Type;",
       }   ,
   ]
,}
---

---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Bounded_Definite_Queues",
qualified_name: "SAL.Gen_Bounded_Definite_Queues",
signature: "sal.gen_bounded_definite_queues",
enclosing: "sal",
is_private: false,
documentation: "Users must check Is_Full before Add, Is_Empty before Remove.\n\n@formal Item_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Queue_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Queues.Queue_Type",
       signature: "sal.gen_bounded_definite_queues.queue_type",
       enclosing: "",
       is_private: false,
       documentation: "Size is maximum number of items in the queue.",
       documentation_snippet: "type Queue_Type (Size : Size_Type) is private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Size_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Queues.Size_Type",
       signature: "sal.gen_bounded_definite_queues.size_type",
       enclosing: "",
       is_private: false,
       documentation: "The upper limit is needed to avoid overflow in Peek.",
       documentation_snippet: "subtype Size_Type is Peek_Type range 1 .. Peek_Type'Last / 2;",
       }   ,
   ]
,}
---

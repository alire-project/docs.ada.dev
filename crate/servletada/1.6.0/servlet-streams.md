---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Streams",
qualified_name: "Servlet.Streams",
signature: "servlet.streams",
enclosing: "servlet",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Print_Stream",
       qualified_name: "Servlet.Streams.Print_Stream",
       signature: "servlet.streams.print_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Print_Stream is new Ada.Finalization.Limited_Controlled\n  and Util.Streams.Output_Stream with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Input_Stream_Access",
       qualified_name: "Servlet.Streams.Input_Stream_Access",
       signature: "servlet.streams.input_stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Input_Stream_Access is access all Input_Stream'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Input_Stream",
       qualified_name: "Servlet.Streams.Input_Stream",
       signature: "servlet.streams.input_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Input_Stream is Util.Streams.Buffered.Input_Buffer_Stream;",
       }   ,
   ]
,}
---

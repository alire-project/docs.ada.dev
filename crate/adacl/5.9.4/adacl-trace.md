---
crate: adacl
layout: gnatdoc
gnatdoc: {
name: "AdaCL.Trace",
qualified_name: "AdaCL.Trace",
signature: "adacl.trace",
enclosing: "adacl",
is_private: false,
documentation: "Name_Length : Lenght of trace String",
documentation_snippet: "",
simple_types:    [
       {
       name: "Destination",
       qualified_name: "AdaCL.Trace.Destination",
       signature: "adacl.trace.destination",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Destination is (Queue, Standard_Error, Standard_Output, File);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "AdaCL.Trace.Object",
       signature: "adacl.trace.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Name_Length : Positive) is new Base.Object with private;",
       }   ,
   ]
,}
---

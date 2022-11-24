---
crate: zeromq_ada
layout: gnatdoc
gnatdoc: {
name: "ZMQ",
qualified_name: "ZMQ",
signature: "zmq",
enclosing: "",
is_private: false,
documentation: "This is the Ada binding to 0MQ  The Intelligent Transport Layer\nhttp://www.zeromq.org/",
documentation_snippet: "",
record_types:    [
       {
       name: "Version_Type",
       qualified_name: "ZMQ.Version_Type",
       signature: "zmq.version_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Version_Type is record\n   Major : aliased Natural;\n   Minor : aliased Natural;\n   Patch : aliased Natural;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Binding_Version",
       qualified_name: "ZMQ.Binding_Version",
       signature: "zmq.binding_version",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Binding_Version : constant Version_Type := (4, 1, 5);",
       }   ,
   ]
,}
---

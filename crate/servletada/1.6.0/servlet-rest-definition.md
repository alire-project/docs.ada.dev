---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Rest.Definition",
qualified_name: "Servlet.Rest.Definition",
signature: "servlet.rest.definition",
enclosing: "servlet.rest",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Definition",
       qualified_name: "Servlet.Rest.Definition.Definition",
       signature: "servlet.rest.definition.definition",
       enclosing: "servlet.rest.definition",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Instance",
              qualified_name: "Servlet.Rest.Definition.Definition.Instance",
              signature: "servlet.rest.definition.definition.instance",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Instance : aliased Descriptor;",
              }          ,
          ]
,       }   ,
   ]
,tagged_types:    [
       {
       name: "Descriptor",
       qualified_name: "Servlet.Rest.Definition.Descriptor",
       signature: "servlet.rest.definition.descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Descriptor is new Servlet.Rest.Descriptor with record\n   Handler  : access procedure (Object : in out Object_Type;\n                                Req    : in out Servlet.Rest.Request'Class;\n                                Reply  : in out Servlet.Rest.Response'Class;\n                                Stream : in out Servlet.Rest.Output_Stream'Class);\nend record;",
       }   ,
   ]
,}
---

---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Algorithms",
qualified_name: "Agpl.Containers.Algorithms",
signature: "agpl.containers.algorithms",
enclosing: "agpl.containers",
is_private: false,
documentation: "Extra algorithms for containers",
documentation_snippet: "",
packages:    [
       {
       name: "Basic",
       qualified_name: "Agpl.Containers.Algorithms.Basic",
       signature: "agpl.containers.algorithms.basic",
       enclosing: "agpl.containers.algorithms",
       is_private: false,
       documentation: "\n@formal Container\n@formal Element_Type\n@formal Cursor\n  with function \"=\"     (L, R : Element_Type) return Boolean is <>;\n@formal Element",
       documentation_snippet: "",
packages:           [
              {
              name: "Conversions",
              qualified_name: "Agpl.Containers.Algorithms.Basic.Conversions",
              signature: "agpl.containers.algorithms.basic.conversions",
              enclosing: "agpl.containers.algorithms.basic",
              is_private: false,
              documentation: "",
              documentation_snippet: "",
              }          ,
              {
              name: "Fields",
              qualified_name: "Agpl.Containers.Algorithms.Basic.Fields",
              signature: "agpl.containers.algorithms.basic.fields",
              enclosing: "agpl.containers.algorithms.basic",
              is_private: false,
              documentation: "Getting parts of a container\n\n@formal Has_Element\n@formal First\n@formal Last\n@formal Next\n@formal Previous\n@formal Append",
              documentation_snippet: "",
              }          ,
          ]
,       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Containers.Algorithms.Log_Section",
       signature: "agpl.containers.algorithms.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.containers.algorithms\";",
       }   ,
   ]
,}
---

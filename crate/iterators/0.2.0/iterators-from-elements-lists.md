---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.From.Elements.Lists",
qualified_name: "Iterators.From.Elements.Lists",
signature: "iterators.from.elements.lists",
enclosing: "iterators.from.elements",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "Iterators.From.Elements.Lists.Constant_Reference_Type",
       signature: "iterators.from.elements.lists.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type\n  (Element : not null access constant Any_Element) Is\nnew Ada_Containers.Constant_Reference_Type (Element => Element);",
       }   ,
       {
       name: "Reference_Type",
       qualified_name: "Iterators.From.Elements.Lists.Reference_Type",
       signature: "iterators.from.elements.lists.reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference_Type\n  (Element : not null access Any_Element) is\n  new Ada_Containers.Reference_Type (Element => Element);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Container",
       qualified_name: "Iterators.From.Elements.Lists.Container",
       signature: "iterators.from.elements.lists.container",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Container is Ada_Containers.List;",
       }   ,
   ]
,}
---

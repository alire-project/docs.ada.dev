---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Bandwidth_Throttle",
qualified_name: "Agpl.Bandwidth_Throttle",
signature: "agpl.bandwidth_throttle",
enclosing: "agpl",
is_private: false,
documentation: "Bandwidth is the elements/second to allow\nPeriod is the period for feedback. Longer ones allow the use\n  of unused bandwidth for more time. (In milliseconds)",
documentation_snippet: "",
access_types:    [
       {
       name: "Object_access",
       qualified_name: "Agpl.Bandwidth_Throttle.Object_access",
       signature: "agpl.bandwidth_throttle.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_access is access all Object;",
       }   ,
   ]
,variables:    [
       {
       name: "Unlimited",
       qualified_name: "Agpl.Bandwidth_Throttle.Unlimited",
       signature: "agpl.bandwidth_throttle.unlimited",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Unlimited : aliased Object (Ada.Streams.Stream_Element_Count'Last, 1000);",
       }   ,
   ]
,}
---

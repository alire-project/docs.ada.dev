---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "Queue",
qualified_name: "Gpr_Build_Util.Queue",
signature: "gpr_build_util.queue",
enclosing: "gpr_build_util",
is_private: false,
documentation: "The queue of sources to be checked for compilation. There can be a\nsingle such queue per application.",
documentation_snippet: "",
record_types:    [
       {
       name: "Source_Info",
       qualified_name: "Gpr_Build_Util.Queue.Source_Info",
       signature: "gpr_build_util.queue.source_info",
       enclosing: "",
       is_private: false,
       documentation: "Information about files stored in the queue\n\n@field Tree\n@field Id\n@field Closure",
       documentation_snippet: "type Source_Info is\n   record\n      Tree    : Project_Tree_Ref := No_Project_Tree;\n      Id      : Source_Id        := No_Source;\n      Closure : Boolean          := False;\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Source_Info",
       qualified_name: "Gpr_Build_Util.Queue.No_Source_Info",
       signature: "gpr_build_util.queue.no_source_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Source_Info : constant Source_Info := (null, null, False);",
       }   ,
   ]
,}
---

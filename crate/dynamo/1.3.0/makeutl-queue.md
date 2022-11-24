---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Queue",
qualified_name: "Makeutl.Queue",
signature: "makeutl.queue",
enclosing: "makeutl",
is_private: false,
documentation: "The queue of sources to be checked for compilation. There can be a\nsingle such queue per application.",
documentation_snippet: "",
record_types:    [
       {
       name: "Source_Info",
       qualified_name: "Makeutl.Queue.Source_Info",
       signature: "makeutl.queue.source_info",
       enclosing: "",
       is_private: false,
       documentation: "Information about files stored in the queue. The exact information\ndepends on the builder, and in particular whether it only supports\nproject-based files (in which case we have a full Source_Id record).\n\n@field Format\n@field Tree\n@field Id\n@field Closure\n@field File\n@field Unit\n@field Index\n@field Project\n@field Sid",
       documentation_snippet: "type Source_Info (Format : Source_Info_Format := Format_Gprbuild) is\n   record\n      case Format is\n         when Format_Gprbuild =>\n            Tree    : Project_Tree_Ref := No_Project_Tree;\n            Id      : Source_Id        := No_Source;\n            Closure : Boolean          := False;\n         when Format_Gnatmake =>\n            File    : File_Name_Type := No_File;\n            Unit    : Unit_Name_Type := No_Unit_Name;\n            Index   : Int            := 0;\n            Project : Project_Id     := No_Project;\n            Sid     : Source_Id      := No_Source;\n      end case;\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Source_Info",
       qualified_name: "Makeutl.Queue.No_Source_Info",
       signature: "makeutl.queue.no_source_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Source_Info : constant Source_Info :=\n                   (Format_Gprbuild, null, null, False);",
       }   ,
   ]
,}
---

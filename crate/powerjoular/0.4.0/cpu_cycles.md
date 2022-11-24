---
crate: powerjoular
layout: gnatdoc
gnatdoc: {
name: "CPU_Cycles",
qualified_name: "CPU_Cycles",
signature: "cpu_cycles",
enclosing: "",
is_private: false,
documentation: "Type to store CPU cycles data",
documentation_snippet: "",
record_types:    [
       {
       name: "CPU_Cycles_Data",
       qualified_name: "CPU_Cycles.CPU_Cycles_Data",
       signature: "cpu_cycles.cpu_cycles_data",
       enclosing: "",
       is_private: false,
       documentation: "\n@field cuser\n  Time spend in user mode\n@field cnice\n  Time spent in user mode with low priority\n@field csystem\n  Time spent in system mode\n@field cidle\n  Time spent in the idle task\n@field cbusy\n  cbusy = cuser + cnice + csystem\n@field ctotal\n  ctotal = cuser + cnice + csystem + cidle",
       documentation_snippet: "type CPU_Cycles_Data is\n    record\n        cuser : Long_Integer;\n        cnice : Long_Integer;\n        csystem : Long_Integer;\n        cidle : Long_Integer;\n        cbusy : Long_Integer := 0;\n        ctotal : Long_Integer := 0;\n    end record;",
       }   ,
   ]
,}
---

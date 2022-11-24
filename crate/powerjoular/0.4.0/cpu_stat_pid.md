---
crate: powerjoular
layout: gnatdoc
gnatdoc: {
name: "CPU_STAT_PID",
qualified_name: "CPU_STAT_PID",
signature: "cpu_stat_pid",
enclosing: "",
is_private: false,
documentation: "Type to store PID CPU stat data",
documentation_snippet: "",
record_types:    [
       {
       name: "CPU_STAT_PID_Data",
       qualified_name: "CPU_STAT_PID.CPU_STAT_PID_Data",
       signature: "cpu_stat_pid.cpu_stat_pid_data",
       enclosing: "",
       is_private: false,
       documentation: "\n@field utime\n  User time\n@field stime\n  System time\n@field total_time\n  Total time",
       documentation_snippet: "type CPU_STAT_PID_Data is\n    record\n        utime : Long_Integer;\n        stime : Long_Integer;\n        total_time : Long_Integer;\n    end record;",
       }   ,
   ]
,}
---

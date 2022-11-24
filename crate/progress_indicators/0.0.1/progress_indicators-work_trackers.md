---
crate: progress_indicators
layout: gnatdoc
gnatdoc: {
name: "Progress_Indicators.Work_Trackers",
qualified_name: "Progress_Indicators.Work_Trackers",
signature: "progress_indicators.work_trackers",
enclosing: "progress_indicators",
is_private: false,
documentation: "Tracker used in the tracking of homogenous groups of work farmed out to\nmany tasks.  The goal is to track the amount of outstanding elements to\nprocess, without caring too much about any individual element of work.",
documentation_snippet: "",
record_types:    [
       {
       name: "Status_Report",
       qualified_name: "Progress_Indicators.Work_Trackers.Status_Report",
       signature: "progress_indicators.work_trackers.status_report",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status_Report is record\n    Completed : Natural := 0;\n    Total     : Natural := 0;\nend record;",
       }   ,
   ]
,}
---

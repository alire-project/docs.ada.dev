---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Samples",
qualified_name: "Samples",
signature: "samples",
enclosing: "",
is_private: false,
documentation: "----------------------
documentation_snippet: "",
simple_types:    [
       {
       name: "Sample",
       qualified_name: "Samples.Sample",
       signature: "samples.sample",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sample(bins: Positive) is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Measure",
       qualified_name: "Samples.Measure",
       signature: "samples.measure",
       enclosing: "",
       is_private: false,
       documentation: "\n@field quantile_levels\n  -----------
       documentation_snippet: "type Measure(quantile_levels: Positive) is record\n  mean,\n  std_dev,\n  stat_err: Real;\n  level   : Quantile_table(1..quantile_levels);\n  VaR     : Quantile_table(1..quantile_levels);\n  TailVaR : Quantile_table(1..quantile_levels);\nend record;",
       }   ,
   ]
,}
---
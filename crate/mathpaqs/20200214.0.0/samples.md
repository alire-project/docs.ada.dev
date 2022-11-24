---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Samples",
qualified_name: "Samples",
signature: "samples",
enclosing: "",
is_private: false,
documentation: "----------------------\n Random sample type --\n----------------------\n\n@formal Real\n@formal Quantile_table\n  Try to correct sample bin location error compared to actual occurrence\n  value, by locating the quantile boundary *within* the histogram.\n  It improves accuracy, but may look bad with discrete variables.\n@formal use_sub_histogram_index\n@formal fit_to_range",
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
       documentation: "\n@field quantile_levels\n  -----------\n   Moments --\n  -----------\n@field mean\n   = E(X), mathematical expectation\n   = sqrt(Var(X))\n  \n   Statistical error\n@field std_dev\n   = E(X), mathematical expectation\n   = sqrt(Var(X))\n  \n   Statistical error\n@field stat_err\n   = E(X), mathematical expectation\n   = sqrt(Var(X))\n  \n   Statistical error\n@field level\n@field VaR\n@field TailVaR",
       documentation_snippet: "type Measure(quantile_levels: Positive) is record\n  mean,\n  std_dev,\n  stat_err: Real;\n  level   : Quantile_table(1..quantile_levels);\n  VaR     : Quantile_table(1..quantile_levels);\n  TailVaR : Quantile_table(1..quantile_levels);\nend record;",
       }   ,
   ]
,}
---

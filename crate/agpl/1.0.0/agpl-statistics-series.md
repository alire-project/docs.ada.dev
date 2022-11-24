---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Statistics.Series",
qualified_name: "Agpl.Statistics.Series",
signature: "agpl.statistics.series",
enclosing: "agpl.statistics",
is_private: false,
documentation: "Depending on the actual precision of Number, some of the subprograms here\ncould give slightly off results due to the online computation of moments.\nSee http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#On-line_algorithm\n\n@formal Number",
documentation_snippet: "",
simple_types:    [
       {
       name: "Confidences",
       qualified_name: "Agpl.Statistics.Series.Confidences",
       signature: "agpl.statistics.series.confidences",
       enclosing: "",
       is_private: false,
       documentation: "Shameful kludge because I'm not up to date with my statistics.\n\n@enum CI_50\n@enum CI_68\n@enum CI_90\n@enum CI_95\n@enum CI_99",
       documentation_snippet: "type Confidences is (CI_50, CI_68, CI_90, CI_95, CI_99);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Serie",
       qualified_name: "Agpl.Statistics.Series.Serie",
       signature: "agpl.statistics.series.serie",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Serie is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Probability",
       qualified_name: "Agpl.Statistics.Series.Probability",
       signature: "agpl.statistics.series.probability",
       enclosing: "",
       is_private: false,
       documentation: "Proper version for any confidence interval",
       documentation_snippet: "subtype Probability is Float range 0.0 .. 1.0;",
       }   ,
   ]
,}
---

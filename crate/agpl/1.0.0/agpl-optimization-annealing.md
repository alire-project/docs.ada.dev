---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Optimization.Annealing",
qualified_name: "Agpl.Optimization.Annealing",
signature: "agpl.optimization.annealing",
enclosing: "agpl.optimization",
is_private: false,
documentation: "pragma Elaborate_Body;",
documentation_snippet: "",
packages:    [
       {
       name: "Manual_Cooling",
       qualified_name: "Agpl.Optimization.Annealing.Manual_Cooling",
       signature: "agpl.optimization.annealing.manual_cooling",
       enclosing: "agpl.optimization.annealing",
       is_private: false,
       documentation: "Expected package usage is to manually divide temperature when you need\nit.\nIn this way you can keep low temperatures for as long as necessary.\nOr, using Update, it will be done for you\n\n@formal Initial_Temperature\n@formal Ceiling_Temperature\n  When auto re-heating, go to this temperature\n@formal Settle_Umbral\n  When checking for no progress, this is the \"absolute zero\";\n  if not reached, no check.\n@formal Cool_Time\n  Time without progress that will cause cooling.\n@formal Settle_Time\n  Time without progress under Settle_Umbral until re-heating\n@formal Divisor\n  The amount to divide temperature if no progress",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Probability",
       qualified_name: "Agpl.Optimization.Annealing.Probability",
       signature: "agpl.optimization.annealing.probability",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Probability is new Float_0_1;",
       }   ,
       {
       name: "Temperature",
       qualified_name: "Agpl.Optimization.Annealing.Temperature",
       signature: "agpl.optimization.annealing.temperature",
       enclosing: "",
       is_private: false,
       documentation: "Valid temperature ranges",
       documentation_snippet: "type Temperature is new Float range 0.0 .. 1.0;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Acceptability",
       qualified_name: "Agpl.Optimization.Annealing.Acceptability",
       signature: "agpl.optimization.annealing.acceptability",
       enclosing: "",
       is_private: false,
       documentation: "Probability of keeping a new solution",
       documentation_snippet: "subtype Acceptability is Probability;",
       }   ,
       {
       name: "Float_0_1",
       qualified_name: "Agpl.Optimization.Annealing.Float_0_1",
       signature: "agpl.optimization.annealing.float_0_1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Float_0_1 is Float range 0.0 .. 1.0;",
       }   ,
   ]
,constants:    [
       {
       name: "Detail_Section",
       qualified_name: "Agpl.Optimization.Annealing.Detail_Section",
       signature: "agpl.optimization.annealing.detail_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Detail_Section : constant String := \"agpl.optimization.annealing.detail\";",
       }   ,
       {
       name: "Log_Section",
       qualified_name: "Agpl.Optimization.Annealing.Log_Section",
       signature: "agpl.optimization.annealing.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section    : constant String := \"agpl.optimization.annealing\";",
       }   ,
   ]
,}
---

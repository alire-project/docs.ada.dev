---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Manual_Cooling",
qualified_name: "Agpl.Optimization.Annealing.Manual_Cooling",
signature: "agpl.optimization.annealing.manual_cooling",
enclosing: "agpl.optimization.annealing",
is_private: false,
documentation: "Expected package usage is to manually divide temperature when you need\nit.\nIn this way you can keep low temperatures for as long as necessary.\nOr, using Update, it will be done for you\n\n@formal Initial_Temperature\n@formal Ceiling_Temperature\n  When auto re-heating, go to this temperature\n@formal Settle_Umbral\n  When checking for no progress, this is the \"absolute zero\";\n  if not reached, no check.\n@formal Cool_Time\n  Time without progress that will cause cooling.\n@formal Settle_Time\n  Time without progress under Settle_Umbral until re-heating\n@formal Divisor\n  The amount to divide temperature if no progress",
documentation_snippet: "",
}
---

---
crate: powerjoular
layout: gnatdoc
gnatdoc: {
name: "Intel_RAPL_sysfs",
qualified_name: "Intel_RAPL_sysfs",
signature: "intel_rapl_sysfs",
enclosing: "",
is_private: false,
documentation: "Type to store Intel RAPL energy data",
documentation_snippet: "",
record_types:    [
       {
       name: "Intel_RAPL_Data",
       qualified_name: "Intel_RAPL_sysfs.Intel_RAPL_Data",
       signature: "intel_rapl_sysfs.intel_rapl_data",
       enclosing: "",
       is_private: false,
       documentation: "\n@field psys\n  Energy for psys (whole SOC)\n@field pkg\n  Energy for all packages\n@field dram\n  Energy for all dram\n@field total_energy\n  Total energy\n@field psys_supported\n  if system supports psys\n@field pkg_supported\n  if system supports pkg 0\n@field dram_supported\n  if system support dram 0",
       documentation_snippet: "type Intel_RAPL_Data is\n    record\n        psys : Float;\n        pkg : Float;\n        dram : Float;\n       \n        total_energy : Float := 0.0;\n        \n        psys_supported : Boolean := False;\n        pkg_supported : Boolean := False;\n        dram_supported : Boolean := False;\n    end record;",
       }   ,
   ]
,}
---

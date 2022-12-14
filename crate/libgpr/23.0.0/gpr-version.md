---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Version",
qualified_name: "GPR.Version",
signature: "gpr.version",
enclosing: "gpr",
is_private: false,
documentation: "This package spec holds version information for the GPR tools.\n\nIt is patched on the fly during builds to match the current version, date\nand build type. Consider it as a compilable template rather than real\nsource.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Gnat_Build_Type",
       qualified_name: "GPR.Version.Gnat_Build_Type",
       signature: "gpr.version.gnat_build_type",
       enclosing: "",
       is_private: false,
       documentation: "See Get_Gnat_Build_Type below for the meaning of these values\n\n@enum Gnatpro\n@enum FSF\n@enum GPL",
       documentation_snippet: "type Gnat_Build_Type is (Gnatpro, FSF, GPL);",
       }   ,
   ]
,constants:    [
       {
       name: "Build_Type",
       qualified_name: "GPR.Version.Build_Type",
       signature: "gpr.version.build_type",
       enclosing: "",
       is_private: false,
       documentation: "Kind of GNAT Build:\n\n  FSF\n     GNAT FSF version. This version of GNAT is part of a Free Software\n     Foundation release of the GNU Compiler Collection (GCC). The bug\n     box generated by Comperr gives information on how to report bugs\n     and list the \"no warranty\" information.\n\n  Gnatpro\n     GNAT Professional version. This version of GNAT is supported by Ada\n     Core Technologies. The bug box generated by package Comperr gives\n     instructions on bug submission that include references to customer\n     number, gnattracker site etc.\n\n  GPL\n     GNAT GPL Edition. This is a special version of GNAT, released by\n     Ada Core Technologies and intended for academic users, and free\n     software developers. The bug box generated by the package Comperr\n     gives appropriate bug submission instructions that do not reference\n     customer number etc.",
       documentation_snippet: "Build_Type : constant Gnat_Build_Type := Gnatpro;",
       }   ,
       {
       name: "Current_Year",
       qualified_name: "GPR.Version.Current_Year",
       signature: "gpr.version.current_year",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Current_Year : constant String := \"2016\";",
       }   ,
       {
       name: "Date",
       qualified_name: "GPR.Version.Date",
       signature: "gpr.version.date",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Date : constant String := \"19940713\";",
       }   ,
       {
       name: "Gpr_Version",
       qualified_name: "GPR.Version.Gpr_Version",
       signature: "gpr.version.gpr_version",
       enclosing: "",
       is_private: false,
       documentation: "Static string identifying this version",
       documentation_snippet: "Gpr_Version : constant String := \"18.0w\";",
       }   ,
   ]
,}
---

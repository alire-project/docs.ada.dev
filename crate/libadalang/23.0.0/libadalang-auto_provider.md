---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Auto_Provider",
qualified_name: "Libadalang.Auto_Provider",
signature: "libadalang.auto_provider",
enclosing: "libadalang",
is_private: false,
documentation: "This package provides the capability to automatically discover the layout\nof source files in an Ada project, given a list of files, or a file name\npattern and a list of directories.\n\nIt is useful in order to easily run Libadalang on a complex project that\ndoes not have its own GPR project file.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Auto_Unit_Provider",
       qualified_name: "Libadalang.Auto_Provider.Auto_Unit_Provider",
       signature: "libadalang.auto_provider.auto_unit_provider",
       enclosing: "",
       is_private: false,
       documentation: "Unit provider for a given list of files",
       documentation_snippet: "type Auto_Unit_Provider is\n   new Libadalang.Analysis.Unit_Provider_Interface with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Source_Filename_Pattern",
       qualified_name: "Libadalang.Auto_Provider.Default_Source_Filename_Pattern",
       signature: "libadalang.auto_provider.default_source_filename_pattern",
       enclosing: "",
       is_private: false,
       documentation: "Default matchers for Ada source filenames. They match most usual file\nextensions used for Ada sources: ``.ads``, ``.adb``, ``.ada``, ``.spc``,\n``.bdy``, etc.",
       documentation_snippet: "Default_Source_Filename_Pattern : constant GNAT.Regpat.Pattern_Matcher :=\n  GNAT.Regpat.Compile (\"\\.(ad.|a|spc|bdy)$\");",
       }   ,
       {
       name: "Default_Source_Filename_Regexp",
       qualified_name: "Libadalang.Auto_Provider.Default_Source_Filename_Regexp",
       signature: "libadalang.auto_provider.default_source_filename_regexp",
       enclosing: "",
       is_private: false,
       documentation: "Default matchers for Ada source filenames. They match most usual file\nextensions used for Ada sources: ``.ads``, ``.adb``, ``.ada``, ``.spc``,\n``.bdy``, etc.",
       documentation_snippet: "Default_Source_Filename_Regexp : constant GNAT.Regexp.Regexp :=\n  GNAT.Regexp.Compile (\".*\\.(ad.|a|spc|bdy)\");",
       }   ,
   ]
,}
---

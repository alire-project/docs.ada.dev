---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Yaml.Parser",
qualified_name: "Yaml.Parser",
signature: "yaml.parser",
enclosing: "yaml",
is_private: false,
documentation: "this package implements a parser that generates an event stream from a\nYAML characters stream source.",
documentation_snippet: "",
record_types:    [
       {
       name: "Accessor",
       qualified_name: "Yaml.Parser.Accessor",
       signature: "yaml.parser.accessor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Accessor (Data : not null access Instance) is limited null record with\n  Implicit_Dereference => Data;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Warning_Handler",
       qualified_name: "Yaml.Parser.Warning_Handler",
       signature: "yaml.parser.warning_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Warning_Handler is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "Yaml.Parser.Instance",
       signature: "yaml.parser.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance is limited new Refcount_Base with private;",
       }   ,
       {
       name: "Reference",
       qualified_name: "Yaml.Parser.Reference",
       signature: "yaml.parser.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "Yaml.Parser.Class",
       signature: "yaml.parser.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
   ]
,}
---

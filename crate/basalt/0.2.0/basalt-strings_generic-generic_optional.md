---
crate: basalt
layout: gnatdoc
gnatdoc: {
name: "Generic_Optional",
qualified_name: "Basalt.Strings_Generic.Generic_Optional",
signature: "basalt.strings_generic.generic_optional",
enclosing: "basalt.strings_generic",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Optional",
       qualified_name: "Basalt.Strings_Generic.Generic_Optional.Optional",
       signature: "basalt.strings_generic.generic_optional.optional",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Optional (Valid : Boolean := False) is record\n   case Valid is\n      when True =>\n         Value : T;\n      when False =>\n         null;\n   end case;\nend record;",
       }   ,
   ]
,}
---

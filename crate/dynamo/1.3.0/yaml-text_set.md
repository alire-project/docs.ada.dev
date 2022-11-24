---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Yaml.Text_Set",
qualified_name: "Yaml.Text_Set",
signature: "yaml.text_set",
enclosing: "yaml",
is_private: false,
documentation: "part of AdaYaml, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"copying.txt\"\n\n@formal Value_Type",
documentation_snippet: "",
record_types:    [
       {
       name: "Holder",
       qualified_name: "Yaml.Text_Set.Holder",
       signature: "yaml.text_set.holder",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Holder is record\n   Hash : Ada.Containers.Hash_Type;\n   Key : Text.Reference;\n   Value : Value_Type;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Reference",
       qualified_name: "Yaml.Text_Set.Reference",
       signature: "yaml.text_set.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,}
---

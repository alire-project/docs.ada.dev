---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Sax.Attributes",
qualified_name: "Sax.Attributes",
signature: "sax.attributes",
enclosing: "sax",
is_private: false,
documentation: "In addition to the SAX standard, we have added an extra field to\nAttributes to memorize the default declaration for the attribute\n(REQUIRED, IMPLIED, FIXED).\nLikewise, enumerations are represented in a full structure, rather than\na simple string.\nWe have also merged the interfaces Attributes and Attributes_Impl, for\nease of use.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Attribute_Type",
       qualified_name: "Sax.Attributes.Attribute_Type",
       signature: "sax.attributes.attribute_type",
       enclosing: "",
       is_private: false,
       documentation: "See 3.3.1 in XML specifications. The last value \"Enumeration\"\ncorresponds to a model like \"(a|b)*\",...\n\n@enum Cdata\n@enum Id\n@enum Idref\n@enum Idrefs\n@enum Entity\n@enum Entities\n@enum Nmtoken\n@enum Nmtokens\n@enum Notation\n@enum Enumeration",
       documentation_snippet: "type Attribute_Type is\n  (Cdata, Id, Idref, Idrefs, Entity, Entities, Nmtoken, Nmtokens,\n   Notation, Enumeration);",
       }   ,
       {
       name: "Default_Declaration",
       qualified_name: "Sax.Attributes.Default_Declaration",
       signature: "sax.attributes.default_declaration",
       enclosing: "",
       is_private: false,
       documentation: "See 3.3.2 in XML specifications\n\n@enum Required\n@enum Implied\n@enum Fixed\n@enum Default",
       documentation_snippet: "type Default_Declaration is (Required, Implied, Fixed, Default);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Attributes",
       qualified_name: "Sax.Attributes.Attributes",
       signature: "sax.attributes.attributes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes is tagged private;",
       }   ,
   ]
,}
---

---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Copulas",
qualified_name: "Copulas",
signature: "copulas",
enclosing: "",
is_private: false,
documentation: "--------------------
documentation_snippet: "",
array_types:    [
       {
       name: "Generator_Vector",
       qualified_name: "Copulas.Generator_Vector",
       signature: "copulas.generator_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator_Vector is array (Integer range <>) of Generator;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Copula",
       qualified_name: "Copulas.Copula",
       signature: "copulas.copula",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Copula (dim : Positive) is abstract tagged private;",
       }   ,
       {
       name: "Gauss_Copula",
       qualified_name: "Copulas.Gauss_Copula",
       signature: "copulas.gauss_copula",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Gauss_Copula is new Copula with private;",
       }   ,
       {
       name: "Independent_Copula",
       qualified_name: "Copulas.Independent_Copula",
       signature: "copulas.independent_copula",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Independent_Copula is new Copula with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Copula_access",
       qualified_name: "Copulas.Copula_access",
       signature: "copulas.copula_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Copula_access is access Copula'Class;",
       }   ,
   ]
,}
---
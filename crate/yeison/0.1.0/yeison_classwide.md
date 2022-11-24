---
crate: yeison
layout: gnatdoc
gnatdoc: {
name: "Yeison_Classwide",
qualified_name: "Yeison_Classwide",
signature: "yeison_classwide",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Operators",
       qualified_name: "Yeison_Classwide.Operators",
       signature: "yeison_classwide.operators",
       enclosing: "yeison_classwide",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Any",
       qualified_name: "Yeison_Classwide.Any",
       signature: "yeison_classwide.any",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any is tagged private with\n  Constant_Indexing => Constant_Reference,\n  Integer_Literal => To_Int,\n  Real_Literal    => To_Real,\n  String_Literal  => To_Str;",
       }   ,
       {
       name: "Bool",
       qualified_name: "Yeison_Classwide.Bool",
       signature: "yeison_classwide.bool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bool is new Any with private;",
       }   ,
       {
       name: "Int",
       qualified_name: "Yeison_Classwide.Int",
       signature: "yeison_classwide.int",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Int is new Any with private with\n  Integer_Literal => To_Int;",
       }   ,
       {
       name: "Map",
       qualified_name: "Yeison_Classwide.Map",
       signature: "yeison_classwide.map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Map is new Any with private with\n  Aggregate => (Empty     => Empty,\n                Add_Named => Insert);",
       }   ,
       {
       name: "Real",
       qualified_name: "Yeison_Classwide.Real",
       signature: "yeison_classwide.real",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Real is new Any with private\n  with Real_Literal => To_Real;",
       }   ,
       {
       name: "Str",
       qualified_name: "Yeison_Classwide.Str",
       signature: "yeison_classwide.str",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Str is new Any with private\n  with String_Literal => To_Str;",
       }   ,
       {
       name: "Vec",
       qualified_name: "Yeison_Classwide.Vec",
       signature: "yeison_classwide.vec",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vec is new Any with private with\n  Aggregate => (Empty          => Empty,\n                Add_Unnamed    => Append);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Any_Composite",
       qualified_name: "Yeison_Classwide.Any_Composite",
       signature: "yeison_classwide.any_composite",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Any_Composite is Any'Class with\n  Dynamic_Predicate => Any_Composite in Map'Class | Vec'Class;",
       }   ,
       {
       name: "Any_Scalar",
       qualified_name: "Yeison_Classwide.Any_Scalar",
       signature: "yeison_classwide.any_scalar",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Any_Scalar is Any'Class with\n  Dynamic_Predicate => Any_Scalar in Bool | Int | Real | Str;",
       }   ,
   ]
,}
---

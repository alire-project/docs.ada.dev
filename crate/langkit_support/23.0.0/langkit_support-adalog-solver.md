---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Adalog.Solver",
qualified_name: "Langkit_Support.Adalog.Solver",
signature: "langkit_support.adalog.solver",
enclosing: "langkit_support.adalog",
is_private: false,
documentation: "\nCopyright (C) 2019-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Relation_Type",
       qualified_name: "Langkit_Support.Adalog.Solver.Relation_Type",
       signature: "langkit_support.adalog.solver.relation_type",
       enclosing: "",
       is_private: false,
       documentation: "Type for a relation. A relation is either an atomic relation, or a\ncompound relation, which can represent a tree of relations of unbounded\ndepth. Solving a relation will assign values to every logic variable\ninvolved in the relation or fail.\n\nA relation is manually ref-counted, and has an ownership share of every\nsub-relation. When the ref-count of a root relation, reaches 0, the\nownership share of each of its sub-relations is destroyed.",
       documentation_snippet: "type Relation_Type (<>) is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Relation",
       qualified_name: "Langkit_Support.Adalog.Solver.Relation",
       signature: "langkit_support.adalog.solver.relation",
       enclosing: "",
       is_private: false,
       documentation: "Type for a relation. A relation is either an atomic relation, or a\ncompound relation, which can represent a tree of relations of unbounded\ndepth. Solving a relation will assign values to every logic variable\ninvolved in the relation or fail.\n\nA relation is manually ref-counted, and has an ownership share of every\nsub-relation. When the ref-count of a root relation, reaches 0, the\nownership share of each of its sub-relations is destroyed.",
       documentation_snippet: "type Relation is access all Relation_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Relation_Array",
       qualified_name: "Langkit_Support.Adalog.Solver.Relation_Array",
       signature: "langkit_support.adalog.solver.relation_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Relation_Array is Relation_Vectors.Elements_Array;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Relation",
       qualified_name: "Langkit_Support.Adalog.Solver.No_Relation",
       signature: "langkit_support.adalog.solver.no_relation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Relation : constant Relation := null;",
       }   ,
   ]
,variables:    [
       {
       name: "No_Relation_Array",
       qualified_name: "Langkit_Support.Adalog.Solver.No_Relation_Array",
       signature: "langkit_support.adalog.solver.no_relation_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Relation_Array : Relation_Array renames Relation_Vectors.Empty_Array;",
       }   ,
   ]
,}
---

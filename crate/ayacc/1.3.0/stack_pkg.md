---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "stack_pkg",
qualified_name: "stack_pkg",
signature: "stack_pkg",
enclosing: "",
is_private: false,
documentation: "| Overview:\n| This package provides the stack abstract data type.  Element type is\n| a generic formal parameter to the package.  There are no explicit\n| bounds on the number of objects that can be pushed onto a given stack.\n| All standard stack operations are provided.\n|\n| The following is a complete list of operations, written in the order\n| in which they appear in the spec.  Overloaded subprograms are followed\n| by (n), where n is the number of subprograms of that name.\n|\n| Constructors:\n|        create \n|        push\n|        pop (2)\n|        copy\n| Query Operations:\n|        top\n|        size\n|        is_empty\n| Heap Management: \n|        destroy\n\n@formal elem_type\n  | Component element type.",
documentation_snippet: "",
simple_types:    [
       {
       name: "stack",
       qualified_name: "stack_pkg.stack",
       signature: "stack_pkg.stack",
       enclosing: "",
       is_private: false,
       documentation: "| The stack abstract data type.",
       documentation_snippet: "type stack is private;",
       }   ,
   ]
,}
---

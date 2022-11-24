---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "string_pkg",
qualified_name: "string_pkg",
signature: "string_pkg",
enclosing: "",
is_private: false,
documentation: "| Overview:\n| Package string_pkg exports an abstract data type, string_type.  A\n| string_type value is a sequence of characters.  The values have arbitrary\n| length.  For a value, s, with length, l, the individual characters are\n| numbered from 1 to l.  These values are immutable; characters cannot be\n| replaced or appended in a destructive fashion.\n|\n| In the documentation for this package, we are careful to distinguish\n| between string_type objects, which are Ada objects in the usual sense,\n| and string_type values, the members of this data abstraction as described\n| above.  A string_type value is said to be associated with, or bound to,\n| a string_type object after an assignment (:=) operation.\n|\n| The operations provided in this package fall into three categories:\n|\n| 1. Constructors:  These functions typically take one or more string_type\n|      objects as arguments.  They work with the values associated with\n|      these objects, and return new string_type values according to\n|      specification.  By a slight abuse of language, we will sometimes\n|      coerce from string_type objects to values for ease in description.\n|\n| 2. Heap Management:\n|      These operations (make_persistent, flush, mark, release) control the\n|      management of heap space.  Because string_type values are\n|      allocated on the heap, and the type is not limited, it is necessary\n|      for a user to assume some responsibility for garbage collection.\n|      String_type is not limited because of the convenience of\n|      the assignment operation, and the usefulness of being able to\n|      instantiate generic units that contain private type formals.\n|      ** Important: To use this package properly, it is necessary to read\n|      the descriptions of the operations in this section.\n|\n| 3. Queries:  These functions return information about the values\n|      that are associated with the argument objects.  The same conventions\n|      for description of operations used in (1) is adopted.\n|\n| A note about design decisions...  The decision to not make the type\n| limited causes two operations to be carried over from the representation.\n| These are the assignment operation, :=, and the \"equality\" operator, \"=\".\n| See the discussion at the beginning of the Heap Management section for a\n| discussion of :=.\n| See the spec for the first of the equal functions for a discussion of \"=\".\n|\n| The following is a complete list of operations, written in the order\n| in which they appear in the spec.  Overloaded subprograms are followed\n| by (n), where n is the number of subprograms of that name.\n|\n| 1. Constructors:\n|        Empty_String\n|        create\n|        \"&\" (3)\n|        substr\n|        splice\n|        insert (3)\n|        lower (2)\n|        upper (2)\n|        mixed (2)\n| 2. Heap Management:\n|        make_persistent (2)\n|        flush\n|        mark, release\n| 3. Queries:\n|        is_empty\n|        length\n|        value\n|        fetch\n|        equal (3)\n|        equivalent (3)\n|        \"<\" (3),\n|    \"<=\" (3)\n|        match_c\n|        match_not_c\n|        match_s (2)\n|        match_any (2)\n|        match_none (2)",
documentation_snippet: "",
simple_types:    [
       {
       name: "string_type",
       qualified_name: "string_pkg.string_type",
       signature: "string_pkg.string_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type string_type is private;",
       }   ,
   ]
,}
---

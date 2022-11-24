---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Tree_IO",
qualified_name: "Tree_IO",
signature: "tree_io",
enclosing: "",
is_private: false,
documentation: "This package contains the routines used to read and write the tree files\nused by ASIS. Only the actual read and write routines are here. The open,\ncreate and close routines are elsewhere (in Osint in the compiler, and in\nthe tree read driver for the tree read interface).",
documentation_snippet: "",
constants:    [
       {
       name: "ASIS_Version_Number",
       qualified_name: "Tree_IO.ASIS_Version_Number",
       signature: "tree_io.asis_version_number",
       enclosing: "",
       is_private: false,
       documentation: "ASIS Version. This is used to check for consistency between the compiler\nused to generate trees and an ASIS application that is reading the\ntrees. It must be incremented whenever a change is made to the tree\nformat that would result in the compiler being incompatible with an\nolder version of ASIS.\n\n27  Changes in the tree structures for expression functions\n28  Changes in Snames\n29  Changes in Sem_Ch3 (tree copying in case of discriminant constraint\n    for concurrent types).\n30  Add Check_Float_Overflow boolean to tree file\n31  Remove read/write of Debug_Pragmas_Disabled/Debug_Pragmas_Enabled\n32  Change the way entities are changed through Next_Entity field in\n    the hierarchy of child units\n33  Add copying subtrees for rewriting infix calls of operator\n    functions for the corresponding original nodes.\n34  Add read/write of Address_Is_Private, Ignore_Rep_Clauses,\n    Ignore_Style_Check_Pragmas, Multiple_Unit_Index. Also this\n    is the version where rep clauses are removed by -gnatI.",
       documentation_snippet: "ASIS_Version_Number : constant := 34;",
       }   ,
   ]
,}
---

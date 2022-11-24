---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Unit_Files",
qualified_name: "Libadalang.Unit_Files",
signature: "libadalang.unit_files",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
subtypes:    [
       {
       name: "Root_Nodes",
       qualified_name: "Libadalang.Unit_Files.Root_Nodes",
       signature: "libadalang.unit_files.root_nodes",
       enclosing: "",
       is_private: false,
       documentation: "Possible nodes at the root of analysis units. Since the grammar allows\nfor empty lists of compilation units, it is safe to assume that all\nanalysis units have non-null roots, even when there are parsing errors.",
       documentation_snippet: "subtype Root_Nodes is Ada_Node_Kind_Type with Static_Predicate =>\n   Root_Nodes in Ada_Compilation_Unit | Ada_Compilation_Unit_List\n               | Ada_Pragma_Node_List;",
       }   ,
   ]
,}
---

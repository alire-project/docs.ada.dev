---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "G_Matrices",
qualified_name: "G_Matrices",
signature: "g_matrices",
enclosing: "",
is_private: false,
documentation: "2005: ghosts of previous versions:\ntype IVector is array (Integer range <>) of Integer;\ntype IMatrix is array (Integer range <>, Integer range <>) of Integer;\ntype p_Matrix is access Matrix;\ntype p_Vector is access Vector;\ntype p_IMatrix is access IMatrix;\ntype p_IVector is access IVector;\n\n@formal Field_elt\n  Element of the algebraic field\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal Sqrt\n@formal \"+\"\n  binary oper.\n@formal \"-\"\n@formal \"*\"\n@formal \"/\"\n  no more \"=\" for Ada 83 compatibility\n  Change 2005: Vector, Matrix also as parameter, allows generic on generic\n  e.g. G_Matrices in generic FEK's body.\n@formal Vector\n@formal Matrix",
documentation_snippet: "",
}
---

---
crate: mathpaqs
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Beta_function",
    qualified_name: "Beta_function",
    signature: "beta_function",
    enclosing: "",
    is_private: false,
    documentation: "  Complete Beta integral\n                  1\n                  -\n                 | |  a-1     b-1\n                 |   t   (1-t)   dt.\n               | |\n                -\n                0\n\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Complex_Polynomial_Roots",
    qualified_name: "Complex_Polynomial_Roots",
    signature: "complex_polynomial_roots",
    enclosing: "",
    is_private: false,
    documentation: "Degree 2: Solves a x^2 + b x + c",
    documentation_snippet: "",
    },
    {
    name: "ConjGrad",
    qualified_name: "ConjGrad",
    signature: "conjgrad",
    enclosing: "",
    is_private: false,
    documentation: "Kind of preconditioner for iterative methods\n\n@formal Real\n@formal Index\n@formal Vector\n@formal Any_matrix\n  NB: 2 syntaxes for instanciating that as unconstrained type :\n  [Ada 95+] type Any_matrix (<>) is private;\n  [Ada 83]  type Any_matrix is private;\n@formal Get\n@formal Rows\n@formal Defined_symmetric\n  ---------------------\n   Vector operations --\n  ---------------------\n@formal Copy\n@formal \"*\"\n@formal Add_scaled\n@formal Scale\n  ----------------------------------\n    Matrix-vector multiplication  --\n  ----------------------------------\n@formal Mult",
    documentation_snippet: "",
    },
    {
    name: "Contours",
    qualified_name: "Contours",
    signature: "contours",
    enclosing: "",
    is_private: false,
    documentation: "======================================================================\n\n     Contours.ads\n\n     CONREC is a contouring subroutine for rectangularly spaced data.\n\n     It emits calls to a line drawing subroutine supplied by the user\n     which draws a contour map corresponding to floating-point data on\n     a randomly spaced rectangular grid. The coordinates emitted are\n     in the same units given in the x() and y() arrays.\n\n     Any number of contour levels may be specified but they must be\n     in order of increasing value.\n\n     procedure ConRec(d,x,y,z)\n       d: matrix of data to contour\n       x: data matrix column coordinates\n       y: data matrix row coordinates\n       z: contour levels in increasing order\n\n       Vecout: user-defined line drawing procedure, of the form\n               ( x1, y1, x2, y2, z: Real );\n\n     There is often the requirement to distinguish each contour\n     line with a different colour or a different line style. This\n     can be done in many ways using the contour values z for a\n     particular line segment.\n\n     A demo is available in file: cr_demo.adb\n\n     Author: Paul D. Bourke\n     Ada version: 23.I.1999, Gautier de Montmollin\n\n     This is part of the Mathpaqs collection of mathematical packages.\n     Latest version may be available at:\n         home page:     http://mathpaqs.sf.net/\n         project page:  http://sf.net/projects/mathpaqs/\n         mirror:        https://github.com/svn2github/mathpaqs\n======================================================================\n\n@formal Real\n  User-defined line drawing procedure:\n@formal Vecout",
    documentation_snippet: "",
    },
    {
    name: "Copulas",
    qualified_name: "Copulas",
    signature: "copulas",
    enclosing: "",
    is_private: false,
    documentation: "--------------------\n Root copula type --\n--------------------\n\n@formal Real\n   Here, any random generator can be provided: the Ada.Numerics.Float_Random\n   one, or another one. Rationale: some implementations (GNAT, Aonix) use a\n   very slow algorithm, the Blum-Blum-Shub 1986 one.\n  \n@formal RGN_Float\n  is Float for Ada.Numerics.Float_Random\n@formal Generator\n@formal Random\n@formal Integer_Vector",
    documentation_snippet: "",
    },
    {
    name: "Discrete_Random_Simulation",
    qualified_name: "Discrete_Random_Simulation",
    signature: "discrete_random_simulation",
    enclosing: "",
    is_private: false,
    documentation: "--------------------------------------------------------------------------\n  The function Index gives the appropriate index of an array Fx containing\n  a Cumulative Distribution Function (CDF), given a value in [0,1].\n  Index is given in three variants with different usefulness/performance\n  features (discussed in their specifications):\n\n     Index_Linear_Search\n     Index_Dichotomic_Search\n     Index_Alias_Method\n\n  The Fx array type represents an empiric random variable\n  with integer values, like 0,1,2,...n, and cumulative probabilities\n  p0, p0+p1, ... , p0+p1+...+pn = 1\n\n  Indeed, Index is an inverse CDF function.\n\n  For general discrete random variables with values that are not all integers\n  you can use an array x(i). Example: x(Index_Linear_Search(Random(gen), Fx)).\n\n  Caution:\n----------\n\n    1) The first probability value in the array must be 0.0. The array\n           represents the function F(x) = P(X<x) (variant of P with strict \"<\").\n\n    2) It is advised to avoid an 1.0 as final value for\n           the \"x=infinite case\" even if it looks fine, since\n           it will be drawn sometimes due to random U01 values\n           very close to 1 that satisfy, *numerically*, 1.0 <= U01.\n\n  Examples with correct data (more in Test_Discrete_Random_Simulation):\n\n     Flip-or-coin: (0.0, 0.5)\n\n     Dice: (0.0, 1.0/6.0, 2.0/6.0, 3.0/6.0, 4.0/6.0, 5.0/6.0)\n\n--------------------------------------------------------------------------\n\n@formal Probability_value\n@formal Probability_array",
    documentation_snippet: "",
    },
    {
    name: "Dormand_Prince_8",
    qualified_name: "Dormand_Prince_8",
    signature: "dormand_prince_8",
    enclosing: "",
    is_private: false,
    documentation: "a",
    documentation_snippet: "",
    },
    {
    name: "Error_function",
    qualified_name: "Error_function",
    signature: "error_function",
    enclosing: "",
    is_private: false,
    documentation: "History and notes about accuracy can be found in the\npackage body (implementation) in numerics/error_function.adb.\nSee random/test_normal.adb for a test.\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Estimators",
    qualified_name: "Estimators",
    signature: "estimators",
    enclosing: "",
    is_private: false,
    documentation: "Linear regression using the least squares criterion\nCompute a and b for the function v(u):= a + b * u such as\nsum(( v(x(i)) - y(i) ) ** 2) is minimal.\n\n@formal Real\n@formal Data_vector",
    documentation_snippet: "",
    },
    {
    name: "Euclidean_Ring_Tools",
    qualified_name: "Euclidean_Ring_Tools",
    signature: "euclidean_ring_tools",
    enclosing: "",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            EuRinToo.ads      (possibly extracted from MATHPAQS.ZIP)\n  Description:     Generic package for euclidean rings\n  Date/version:    22.12.1996\n  Author:          Gautier.deMontmollin@Maths.UniNe.CH\n----------------------------------------------------------------------------\n\n@formal ring_elt\n  ring element type\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  binary oper.\n@formal \"*\"\n@formal \"/\"\n  returns the quotient:  a= b*q + r\n  q:quotient, r:rest",
    documentation_snippet: "",
    },
    {
    name: "Formulas",
    qualified_name: "Formulas",
    signature: "formulas",
    enclosing: "",
    is_private: false,
    documentation: "TO DO:\n  - implement user functions\n  - (never-ending) improve Simplify (see misses at Test_Formulas)\n\n@formal Real\n  Payload can be a helper for user variables.\n  For instance, formulas can be associated to different objects where\n  user variables may have different values.\n@formal Payload_type\n@formal Evaluate_variable",
    documentation_snippet: "",
    },
    {
    name: "Frac",
    qualified_name: "Frac",
    signature: "frac",
    enclosing: "",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            Frac.ads          (possibly extracted from MATHPAQS.ZIP)\n  Description:     Generic package, gives back the field of quotients of\n                     an integral domain\n  Date/version:    22-Dec-1996\n  Author:          Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal ring_elt\n  ring element type\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal \"+\"\n  binary oper.\n@formal \"*\"",
    documentation_snippet: "",
    },
    {
    name: "Frac.Order",
    qualified_name: "Frac.Order",
    signature: "frac.order",
    enclosing: "frac",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            frac-order.ads\n  Description:     Child of the generic package 'Frac' which provides an\n                    order relation derived from the ring's order relation\n  Date/version:    22-Dec-1996\n  Author:          Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal \"<\"\n  order relation",
    documentation_snippet: "",
    },
    {
    name: "Frac_euclid",
    qualified_name: "Frac_euclid",
    signature: "frac_euclid",
    enclosing: "",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            frac_euclid.ads\n  Description:     Generic package, gives back the field of quotients of an\n                     euclidean ring (i.e. a ring with division; this allows\n                     for *reduction* of fractions)\n  Date/version:    22-Dec-1996\n  Author:          Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal ring_elt\n  ring element type\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal \"+\"\n  binary oper.\n@formal \"-\"\n@formal \"*\"\n@formal \"/\"\n  returns the quotient:  a= b*q + r\n  q:quotient, r:rest",
    documentation_snippet: "",
    },
    {
    name: "Frac_Euclid.Order",
    qualified_name: "Frac_Euclid.Order",
    signature: "frac_euclid.order",
    enclosing: "frac_euclid",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            frac_euclid-order.ads\n  Description:     Child of the generic package 'Frac_Euclid' which provides\n                    an order relation derived from the ring's order relation\n  Date/version:    22-Dec-1996\n  Author:          Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal \"<\"\n  order relation",
    documentation_snippet: "",
    },
    {
    name: "G_FEK",
    qualified_name: "G_FEK",
    signature: "g_fek",
    enclosing: "",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            g_fek.ads\n  Description:     Finite Elements Kernel (extracts)\n                   - generic -> ok for any precision!\n  Date / Version:  3-Feb-2005 ; 25-Apr-2000 ; ... ; 25.VI.1997\n  Author:          M. Bercovier, Jerusalem\n                   Ada version by G. de Montmollin\n                   http://gautiersblog.blogspot.com/\n----------------------------------------------------------------------------\n\n@formal FEK_Float\n@formal Vector\n@formal Matrix",
    documentation_snippet: "",
    },
    {
    name: "G_Matrices",
    qualified_name: "G_Matrices",
    signature: "g_matrices",
    enclosing: "",
    is_private: false,
    documentation: "2005: ghosts of previous versions:\ntype IVector is array (Integer range <>) of Integer;\ntype IMatrix is array (Integer range <>, Integer range <>) of Integer;\ntype p_Matrix is access Matrix;\ntype p_Vector is access Vector;\ntype p_IMatrix is access IMatrix;\ntype p_IVector is access IVector;\n\n@formal Field_elt\n  Element of the algebraic field\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal Sqrt\n@formal \"+\"\n  binary oper.\n@formal \"-\"\n@formal \"*\"\n@formal \"/\"\n  no more \"=\" for Ada 83 compatibility\n  Change 2005: Vector, Matrix also as parameter, allows generic on generic\n  e.g. G_Matrices in generic FEK's body.\n@formal Vector\n@formal Matrix",
    documentation_snippet: "",
    },
    {
    name: "Gamma_function",
    qualified_name: "Gamma_function",
    signature: "gamma_function",
    enclosing: "",
    is_private: false,
    documentation: "History and notes about accuracy can be found in the implementation\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Generic_Integer_Arrays",
    qualified_name: "Generic_Integer_Arrays",
    signature: "generic_integer_arrays",
    enclosing: "",
    is_private: false,
    documentation: "TYPES --\n\n@formal Integer_Type",
    documentation_snippet: "",
    },
    {
    name: "Generic_Random_Functions",
    qualified_name: "Generic_Random_Functions",
    signature: "generic_random_functions",
    enclosing: "",
    is_private: false,
    documentation: "-------------------------------------------------------------------------------\n   =======================================================================   --\n   1. Inverse Cumulative Distribution Functions and other simulation tools   --\n   =======================================================================   --\n-------------------------------------------------------------------------------\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Generic_Real_Linear_Equations",
    qualified_name: "Generic_Real_Linear_Equations",
    signature: "generic_real_linear_equations",
    enclosing: "",
    is_private: false,
    documentation: "Author: Jon Squire\nOriginal code here:\n  http://www.cs.umbc.edu/~squire/adaclass/gnatmath95/\nChanges:\n  - Generic_Real_Arrays = Ada.Numerics.Generic_Real_Arrays (Ada 2005)\n  - removed dependency on others non-standard packages\n  - (18-Mar-2015): Integer_Vector as generic parameter. Added a few \"_JS\"\n      suffixes to address ambiguities with Ada.Numerics.Generic_Real_Arrays\n  - many fixes\n\n@formal Real\n@formal Integer_Vector",
    documentation_snippet: "",
    },
    {
    name: "Graph",
    qualified_name: "Graph",
    signature: "graph",
    enclosing: "",
    is_private: false,
    documentation: "* Devices",
    documentation_snippet: "",
    },
    {
    name: "Graph.Cubic_curves",
    qualified_name: "Graph.Cubic_curves",
    signature: "graph.cubic_curves",
    enclosing: "graph",
    is_private: false,
    documentation: "* Coordinates of cubic curves in math plane",
    documentation_snippet: "",
    },
    {
    name: "Graph.F",
    qualified_name: "Graph.F",
    signature: "graph.f",
    enclosing: "graph",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            Graph.F.ads\n  Description:     Root package for fonts\n----------------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Bold",
    qualified_name: "Graph.F.Bold",
    signature: "graph.f.bold",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: bold.chr ; long font name: Bold",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Complex",
    qualified_name: "Graph.F.Complex",
    signature: "graph.f.complex",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: lcom.chr ; long font name: Complex",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.EuroStyle",
    qualified_name: "Graph.F.EuroStyle",
    signature: "graph.f.eurostyle",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: euro.chr ; long font name: EuroStyle",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Gothic",
    qualified_name: "Graph.F.Gothic",
    signature: "graph.f.gothic",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: goth.chr ; long font name: Gothic",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Helv",
    qualified_name: "Graph.F.Helv",
    signature: "graph.f.helv",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: h--c.chr ; long font name: Helv",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Helv_B",
    qualified_name: "Graph.F.Helv_B",
    signature: "graph.f.helv_b",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: hb-c.chr ; long font name: Helv_B",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Helv_BI",
    qualified_name: "Graph.F.Helv_BI",
    signature: "graph.f.helv_bi",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: hbic.chr ; long font name: Helv_BI",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Helv_I",
    qualified_name: "Graph.F.Helv_I",
    signature: "graph.f.helv_i",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: hi-c.chr ; long font name: Helv_I",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Noble",
    qualified_name: "Graph.F.Noble",
    signature: "graph.f.noble",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: nobl.chr ; long font name: Noble",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.SansSerif",
    qualified_name: "Graph.F.SansSerif",
    signature: "graph.f.sansserif",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: sans.chr ; long font name: SansSerif",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Script",
    qualified_name: "Graph.F.Script",
    signature: "graph.f.script",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: scri.chr ; long font name: Script",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Simple",
    qualified_name: "Graph.F.Simple",
    signature: "graph.f.simple",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: simp.chr ; long font name: Simple",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Small",
    qualified_name: "Graph.F.Small",
    signature: "graph.f.small",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: litt.chr ; long font name: Small",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.Triplex",
    qualified_name: "Graph.F.Triplex",
    signature: "graph.f.triplex",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: trip.chr ; long font name: Triplex",
    documentation_snippet: "",
    },
    {
    name: "Graph.F.TriScript",
    qualified_name: "Graph.F.TriScript",
    signature: "graph.f.triscript",
    enclosing: "graph.f",
    is_private: false,
    documentation: "< \"Graph for Ada\" font package, format: 12-Jul-2003 >--\n< File automatically generated by: chr2vect.pas     >--\n\n Source CHR file: tscr.chr ; long font name: TriScript",
    documentation_snippet: "",
    },
    {
    name: "Graph.PostScript_driver",
    qualified_name: "Graph.PostScript_driver",
    signature: "graph.postscript_driver",
    enclosing: "graph",
    is_private: false,
    documentation: "Create / Close PS file stream",
    documentation_snippet: "",
    },
    {
    name: "Graph.Standard_fonts",
    qualified_name: "Graph.Standard_fonts",
    signature: "graph.standard_fonts",
    enclosing: "graph",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            GrStafon.ads\n  Description:     Extension of Graph package: standard fonts,\n                       all in one package\n\n  Fonts included:  See below!\n\n  Date/version:    12-Jul-2003\n  Author:          G. de Montmollin\n----------------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Integer_Arrays_IO",
    qualified_name: "Integer_Arrays_IO",
    signature: "integer_arrays_io",
    enclosing: "",
    is_private: false,
    documentation: "instantiate: package Arrays_IO is new\n                            Integer_Arrays_IO(Integer, Integer_Arrays);\n\n@formal Integer_Type",
    documentation_snippet: "",
    },
    {
    name: "Multi_precision_integers",
    qualified_name: "Multi_precision_integers",
    signature: "multi_precision_integers",
    enclosing: "",
    is_private: false,
    documentation: "Integers for array indexing --",
    documentation_snippet: "",
    },
    {
    name: "Multi_precision_integers.Check",
    qualified_name: "Multi_precision_integers.Check",
    signature: "multi_precision_integers.check",
    enclosing: "multi_precision_integers",
    is_private: false,
    documentation: "check integrity",
    documentation_snippet: "",
    },
    {
    name: "Multi_precision_integers.IO",
    qualified_name: "Multi_precision_integers.IO",
    signature: "multi_precision_integers.io",
    enclosing: "multi_precision_integers",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Phi_function",
    qualified_name: "Phi_function",
    signature: "phi_function",
    enclosing: "",
    is_private: false,
    documentation: "History and notes about accuracy can be found in the\npackage body (implementation) in numerics/phi_function.adb.\nSee random/test_normal.adb for a test.\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Polynomials",
    qualified_name: "Polynomials",
    signature: "polynomials",
    enclosing: "",
    is_private: false,
    documentation: "\n@formal Field_elt\n@formal zero\n  0 and 1 elements\n@formal one\n  0 and 1 elements\n@formal \"-\"\n  unary oper.\n@formal \"+\"\n  binary oper.\n@formal \"-\"\n@formal \"*\"\n@formal \"/\"\n@formal \"=\"",
    documentation_snippet: "",
    },
    {
    name: "Polynomials.Output",
    qualified_name: "Polynomials.Output",
    signature: "polynomials.output",
    enclosing: "polynomials",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            polyoutp.ads\n  Description:     Supplement of package 'Polynomials': outputs\n  Date/version:    1-Feb-2005; 22.12.1996\n  Author:          Gautier de Montmollin\n----------------------------------------------------------------------------\n\n@formal Field_Put\n@formal \">\"",
    documentation_snippet: "",
    },
    {
    name: "Real_Arrays_IO",
    qualified_name: "Real_Arrays_IO",
    signature: "real_arrays_io",
    enclosing: "",
    is_private: false,
    documentation: "instantiate: package Arrays_IO is new Real_Arrays_IO(Float, Real_Arrays);\n\n@formal Real",
    documentation_snippet: "",
    },
    {
    name: "Samples",
    qualified_name: "Samples",
    signature: "samples",
    enclosing: "",
    is_private: false,
    documentation: "----------------------\n Random sample type --\n----------------------\n\n@formal Real\n@formal Quantile_table\n  Try to correct sample bin location error compared to actual occurrence\n  value, by locating the quantile boundary *within* the histogram.\n  It improves accuracy, but may look bad with discrete variables.\n@formal use_sub_histogram_index\n@formal fit_to_range",
    documentation_snippet: "",
    },
    {
    name: "Sparse",
    qualified_name: "Sparse",
    signature: "sparse",
    enclosing: "",
    is_private: false,
    documentation: "----------------------------------------------------------------------------\n  File:            sparse.ads\n  Description:     Sparse matrices, generic package\n                     Compressed Row Storage (CRS) format\n                     doc. @ http://www.netlib.org/\n\n  Date / Version:  01-Jan-2011 ; 21-Nov-2010 ;\n                   08-Jun-2001 ; ... ; 29-Mar-1999\n\n  Author:          Olivier Besson, Universite de Neuchatel & Cray research\n                   Olivier.Besson (at) UniNe.ch\n\n  Ada version:     Gautier de Montmollin\n                   http://gautiersblog.blogspot.com/\n\n  NB: From 8-Jun-2001 version, (bi)conjugate gradient algorithms\n      are detached in a package independent of matrix type\n----------------------------------------------------------------------------\n\n@formal Real\n@formal Index\n@formal Vector",
    documentation_snippet: "",
    },
    {
    name: "Sparse.Vector_Ops",
    qualified_name: "Sparse.Vector_Ops",
    signature: "sparse.vector_ops",
    enclosing: "sparse",
    is_private: false,
    documentation: "Implementations (package bodies) with or without BLAS\n\n@formal real\n@formal index\n@formal vector",
    documentation_snippet: "",
    },
    {
    name: "Test_Formulas_Pkg",
    qualified_name: "Test_Formulas_Pkg",
    signature: "test_formulas_pkg",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "U_Rand",
    qualified_name: "U_Rand",
    signature: "u_rand",
    enclosing: "",
    is_private: false,
    documentation: "------------------------------------------------------------------------\n The following is an implementation of a \"universal\" random number    --\n generator algorithm developed by Dr. George Marsaglia of the         --\n Supercomputer Computations Research Institute (SCRI) at Florida      --\n State University.  This generator has a period of ~2**144 and has    --\n been tailored for reproducibility in all CPU's with at least         --\n 16 bit integer arithmetic and 24 bit floating point.  This algorithm --\n does not generate random numbers < 2**-24.  At the end of this file  --\n you will find a self test program that checks generated results      --\n against known expected results and reports any inaccuracies.         --\n                                                                      --\n Further references: \"Toward a Universal Random Number Generator\",    --\n appearing in the Journal of The American Statistical Association.    --\n                                                                      --\n This code appeared in the March/April publication of SIGAda's        --\n Ada Letters and is considered public domain.  PCK                    --\n------------------------------------------------------------------------\n\n Jul-2009: GdM: - Made generic and task safe: no more globals\n                - Procedure name aliases to make the replacement\n                  of Ada95+'s Ada.Numerics.Float_Random easy.\n Mar-1988: Published in Ada Letters (Volume VIII, Number 2)\n\n@formal Real",
    documentation_snippet: "",
    },
]
, subprograms: [
    {
    name: "Arenstorf",
    qualified_name: "Arenstorf",
    signature: "arenstorf()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Arenstorf",
    },
    {
    name: "Arithmetic_Compression",
    qualified_name: "Arithmetic_Compression",
    signature: "arithmetic_compression()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure  Arithmetic_Compression",
    },
    {
    name: "BioMorph",
    qualified_name: "BioMorph",
    signature: "biomorph()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure BioMorph",
    },
    {
    name: "Champ_vt",
    qualified_name: "Champ_vt",
    signature: "champ_vt()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Champ_vt",
    },
    {
    name: "CR_Demo",
    qualified_name: "CR_Demo",
    signature: "cr_demo()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure CR_Demo",
    },
    {
    name: "Demo_FEK",
    qualified_name: "Demo_FEK",
    signature: "demo_fek()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Demo_FEK",
    },
    {
    name: "Diffchal",
    qualified_name: "Diffchal",
    signature: "diffchal()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Diffchal",
    },
    {
    name: "EDS_1",
    qualified_name: "EDS_1",
    signature: "eds_1()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure EDS_1",
    },
    {
    name: "Fractal",
    qualified_name: "Fractal",
    signature: "fractal()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Fractal",
    },
    {
    name: "GNAT_Int",
    qualified_name: "GNAT_Int",
    signature: "gnat_int()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure GNAT_Int",
    },
    {
    name: "pi_digits",
    qualified_name: "pi_digits",
    signature: "pi_digits()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure pi_digits",
    },
    {
    name: "pi_digits_GMP",
    qualified_name: "pi_digits_GMP",
    signature: "pi_digits_gmp()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure pi_digits_GMP",
    },
    {
    name: "pi_digits_timing",
    qualified_name: "pi_digits_timing",
    signature: "pi_digits_timing()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure pi_digits_timing",
    },
    {
    name: "Porscherie",
    qualified_name: "Porscherie",
    signature: "porscherie()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Porscherie",
    },
    {
    name: "PPM2Func",
    qualified_name: "PPM2Func",
    signature: "ppm2func()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure PPM2Func",
    },
    {
    name: "Show_floats_limits",
    qualified_name: "Show_floats_limits",
    signature: "show_floats_limits()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Show_floats_limits",
    },
    {
    name: "Sim_Alea",
    qualified_name: "Sim_Alea",
    signature: "sim_alea()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Sim_Alea",
    },
    {
    name: "Test_Beta",
    qualified_name: "Test_Beta",
    signature: "test_beta()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Beta",
    },
    {
    name: "Test_Cholesky",
    qualified_name: "Test_Cholesky",
    signature: "test_cholesky()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Cholesky",
    },
    {
    name: "Test_Complex_Polynomial_Roots",
    qualified_name: "Test_Complex_Polynomial_Roots",
    signature: "test_complex_polynomial_roots()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Complex_Polynomial_Roots",
    },
    {
    name: "Test_Copulas",
    qualified_name: "Test_Copulas",
    signature: "test_copulas()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Copulas",
    },
    {
    name: "Test_Discrete_Random_Simulation",
    qualified_name: "Test_Discrete_Random_Simulation",
    signature: "test_discrete_random_simulation()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Discrete_Random_Simulation",
    },
    {
    name: "Test_ERT",
    qualified_name: "Test_ERT",
    signature: "test_ert()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_ERT",
    },
    {
    name: "Test_Estimators",
    qualified_name: "Test_Estimators",
    signature: "test_estimators()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Estimators",
    },
    {
    name: "Test_Finite_distributed_random",
    qualified_name: "Test_Finite_distributed_random",
    signature: "test_finite_distributed_random()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Finite_distributed_random",
    },
    {
    name: "Test_Float_Poly",
    qualified_name: "Test_Float_Poly",
    signature: "test_float_poly()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Float_Poly",
    },
    {
    name: "Test_Formulas",
    qualified_name: "Test_Formulas",
    signature: "test_formulas()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Formulas",
    },
    {
    name: "Test_Gamma",
    qualified_name: "Test_Gamma",
    signature: "test_gamma()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Gamma",
    },
    {
    name: "Test_Generic_Real_Linear_Equations",
    qualified_name: "Test_Generic_Real_Linear_Equations",
    signature: "test_generic_real_linear_equations()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Generic_Real_Linear_Equations",
    },
    {
    name: "Test_Int",
    qualified_name: "Test_Int",
    signature: "test_int()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Int",
    },
    {
    name: "Test_Normal",
    qualified_name: "Test_Normal",
    signature: "test_normal()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Normal",
    },
    {
    name: "Test_Pareto",
    qualified_name: "Test_Pareto",
    signature: "test_pareto()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Pareto",
    },
    {
    name: "Test_Poisson",
    qualified_name: "Test_Poisson",
    signature: "test_poisson()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Poisson",
    },
    {
    name: "Test_QR",
    qualified_name: "Test_QR",
    signature: "test_qr()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_QR",
    },
    {
    name: "Test_random_performance",
    qualified_name: "Test_random_performance",
    signature: "test_random_performance()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_random_performance",
    },
    {
    name: "Test_Rationals",
    qualified_name: "Test_Rationals",
    signature: "test_rationals()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Rationals",
    },
    {
    name: "Test_RSA",
    qualified_name: "Test_RSA",
    signature: "test_rsa()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_RSA",
    },
    {
    name: "Test_Samples",
    qualified_name: "Test_Samples",
    signature: "test_samples()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Samples",
    },
    {
    name: "Test_Sparse",
    qualified_name: "Test_Sparse",
    signature: "test_sparse()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_Sparse",
    },
    {
    name: "Test_U_Rand",
    qualified_name: "Test_U_Rand",
    signature: "test_u_rand()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Test_U_Rand",
    },
    {
    name: "Time_display",
    qualified_name: "Time_display",
    signature: "time_display((ada.calendar.time, standard.boolean, standard.boolean) -> standard.string)$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "function Time_display(\n  T        : Calendar.Time:= Calendar.Clock;\n  Seconds  : Boolean      := True;\n  Intra_day: Boolean      := True\n)\n  return String",
    },
]
}
---

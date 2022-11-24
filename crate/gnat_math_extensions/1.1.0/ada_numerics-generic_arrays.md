---
crate: gnat_math_extensions
layout: gnatdoc
gnatdoc: {
name: "Ada_Numerics.Generic_Arrays",
qualified_name: "Ada_Numerics.Generic_Arrays",
signature: "ada_numerics.generic_arrays",
enclosing: "ada_numerics",
is_private: false,
documentation: "This package is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or\n(at your option) any later version.  It is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without\neven the implied warranty of MERCHANTABILITY or FITNESS FOR A\nPARTICULAR PURPOSE.\n\nAs a special exception under Section 7 of GPL version 3, you are\ngranted additional permissions described in the GCC Runtime\nLibrary Exception, version 3.1, as published by the Free Software\nFoundation.\n\nYou should have received a copy of the GNU General Public License\nand a copy of the GCC Runtime Library Exception along with this\nprogram; see the files COPYING3 and COPYING.RUNTIME respectively.\nIf not, see <http://www.gnu.org/licenses/>.\n\nCopyright Simon Wright <simon@pushface.org>",
documentation_snippet: "",
array_types:    [
       {
       name: "Generalized_Eigenvalue_Vector",
       qualified_name: "Ada_Numerics.Generic_Arrays.Generalized_Eigenvalue_Vector",
       signature: "ada_numerics.generic_arrays.generalized_eigenvalue_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generalized_Eigenvalue_Vector\n   is array (Integer range <>) of Generalized_Eigenvalue;",
       }   ,
   ]
,record_types:    [
       {
       name: "Generalized_Eigenvalue",
       qualified_name: "Ada_Numerics.Generic_Arrays.Generalized_Eigenvalue",
       signature: "ada_numerics.generic_arrays.generalized_eigenvalue",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generalized_Eigenvalue is record\n   Alpha : Complex_Types.Complex;\n   Beta  : Complex_Types.Complex;\nend record;",
       }   ,
   ]
,}
---

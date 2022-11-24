---
crate: avltrees
layout: gnatdoc
gnatdoc: {
name: "AVL_Trees",
qualified_name: "AVL_Trees",
signature: "avl_trees",
enclosing: "",
is_private: false,
documentation: "---------------------------------------------------------------------\n  Copyright 2021 Lev Kujawski\n\n  This file is part of AVLTREES.\n\n  AVLTREES is free software: you can redistribute it and/or modify\n  it under the terms of the GNU Lesser General Public License as\n  published by the Free Software Foundation, either version 3 of\n  the License, or (at your option) any later version.\n\n  AVLTREES is distributed in the hope that it will be useful,\n  but WITHOUT ANY WARRANTY; without even the implied warranty of\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n  GNU Lesser General Public License for more details.\n\n  You should have received a copy of the\n  GNU Lesser General Public License along with AVLTREES.\n  If not, see <https://www.gnu.org/licenses/>.\n\n  SPDX-License-Identifier: LGPL-3.0-or-later\n\n  File:          avltrees.ads (Ada Package Specification)\n  Language:      Ada (1987) [1]\n  Author:        Lev Kujawski\n  Description:\n    Self-balancing binary trees, based upon the algorithms developed\n    by G. M. Adelson-Velsky and E. M. Landis [2].\n\n  References:\n  [1] Programming languages - Ada, ISO/IEC 8652:1987, 15 Jun. 1987.\n  [2] G. M. Adelson-Velsky and E. M. Landis\n      Doklady Akademii Nauk SSSR 146 (1962), 263-266\n      English translation in\n      \"An algorithm for the organization of information\",\n      Soviet Math. Doklady 3 (1962) 1259-1263.\n\n---------------------------------------------------------------------\n\n@formal Key_T\n@formal Element_T\n@formal Is_Less_Than\n  The use of Is_Less_Than mitigates a GNAT hiding warning that\n  would otherwise occur with \"<\".",
documentation_snippet: "",
simple_types:    [
       {
       name: "T",
       qualified_name: "AVL_Trees.T",
       signature: "avl_trees.t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type T is limited private;",
       }   ,
   ]
,}
---

---
crate: excel_writer
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "CSV",
    qualified_name: "CSV",
    signature: "csv",
    enclosing: "",
    is_private: false,
    documentation: "Freeware, author: J-P. Rosen, http://www.adalog.fr/",
    documentation_snippet: "",
    },
    {
    name: "Excel_Out",
    qualified_name: "Excel_Out",
    signature: "excel_out",
    enclosing: "",
    is_private: false,
    documentation: "---------------------------------------------------------------\n The abstract Excel output stream root type.                 --\n From this package, you can use the following derived types: --\n    * Excel_Out_File    : output in a file                   --\n    * Excel_Out_String  : output in a string                 --\n Of course you can define your own derived types.            --\n---------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "IEEE_754",
    qualified_name: "IEEE_754",
    signature: "ieee_754",
    enclosing: "",
    is_private: false,
    documentation: "                                                                    --\n  package IEEE_754                Copyright (c)  Dmitry A. Kazakov  --\n  Interface                                      Luebeck            --\n                                                 Summer, 2008       --\n                                                                    --\n                                Last revision :  11:26 27 Jul 2008  --\n                                                                    --\n  This  library  is  free software; you can redistribute it and/or  --\n  modify it under the terms of the GNU General Public  License  as  --\n  published by the Free Software Foundation; either version  2  of  --\n  the License, or (at your option) any later version. This library  --\n  is distributed in the hope that it will be useful,  but  WITHOUT  --\n  ANY   WARRANTY;   without   even   the   implied   warranty   of  --\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU  --\n  General  Public  License  for  more  details.  You  should  have  --\n  received  a  copy  of  the GNU General Public License along with  --\n  this library; if not, write to  the  Free  Software  Foundation,  --\n  Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.    --\n                                                                    --\n  As a special exception, if other files instantiate generics from  --\n  this unit, or you link this unit with other files to produce  an  --\n  executable, this unit does not by  itself  cause  the  resulting  --\n  executable to be covered by the GNU General Public License. This  --\n  exception  does not however invalidate any other reasons why the  --\n  executable file might be covered by the GNU Public License.       --\n____________________________________________________________________--",
    documentation_snippet: "",
    },
    {
    name: "IEEE_754.Generic_Double_Precision",
    qualified_name: "IEEE_754.Generic_Double_Precision",
    signature: "ieee_754.generic_double_precision",
    enclosing: "ieee_754",
    is_private: false,
    documentation: "\n Float_64 -- 64-bit double-precision IEEE 754 float. The memory layout\n             is big endian, i.e. the byte containing the number's sign\n and  the  most  significant  bits  of the exponent is the first array\n element.  The  byte  containing  the  least  significant  bits of the\n mantissa is the last array element.\n\n\n@formal Number",
    documentation_snippet: "",
    },
    {
    name: "Spreadsheet_references",
    qualified_name: "Spreadsheet_references",
    signature: "spreadsheet_references",
    enclosing: "",
    is_private: false,
    documentation: "Freeware, author: G. de Montmollin",
    documentation_snippet: "",
    },
]
, subprograms: [
    {
    name: "BIFF_Dump",
    qualified_name: "BIFF_Dump",
    signature: "biff_dump()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure BIFF_Dump",
    },
    {
    name: "CSV2HTML",
    qualified_name: "CSV2HTML",
    signature: "csv2html()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure CSV2HTML",
    },
    {
    name: "CSV2TeX",
    qualified_name: "CSV2TeX",
    signature: "csv2tex()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure CSV2TeX",
    },
    {
    name: "CSV2XLS",
    qualified_name: "CSV2XLS",
    signature: "csv2xls()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure CSV2XLS",
    },
    {
    name: "EW_Test",
    qualified_name: "EW_Test",
    signature: "ew_test()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure EW_Test",
    },
    {
    name: "Excel_Out_Demo",
    qualified_name: "Excel_Out_Demo",
    signature: "excel_out_demo()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Excel_Out_Demo",
    },
    {
    name: "Spreadsheet_references_demo",
    qualified_name: "Spreadsheet_references_demo",
    signature: "spreadsheet_references_demo()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Spreadsheet_references_demo",
    },
]
}
---

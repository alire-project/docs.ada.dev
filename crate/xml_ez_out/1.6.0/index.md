---
crate: xml_ez_out
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "McKae",
    qualified_name: "McKae",
    signature: "mckae",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "McKae.XML",
    qualified_name: "McKae.XML",
    signature: "mckae.xml",
    enclosing: "mckae",
    is_private: false,
    documentation: "----------------------------------------------------------------------\n                                                                    --\n                     McKae Software Utilities                       --\n                                                                    --\n           Copyright (C) 2004 McKae Technologies                    --\n                                                                    --\n The  McKae   software  utilities   are  free  software;   you  can --\n redistribute it  and/or modify it  under terms of the  GNU General --\n Public  License  as published  by  the  Free Software  Foundation; --\n either version  2, or (at  your option) any later  version.  McKae --\n Software Utilities are  distributed in the hope that  they will be --\n useful,  but  WITHOUT  ANY  WARRANTY;  without  even  the  implied --\n warranty of  MERCHANTABILITY or FITNESS FOR  A PARTICULAR PURPOSE. --\n See the GNU  General Public License for more  details.  You should --\n have received a copy of the GNU General Public License distributed --\n with DTraq; see file COPYING.   If not, write to the Free Software --\n Foundation, 59  Temple Place -  Suite 330, Boston,  MA 02111-1307, --\n USA.                                                               --\n                                                                    --\n As a  special exception, if other files  instantiate generics from --\n this unit,  or you link this  unit with other files  to produce an --\n executable,  this unit  does  not by  itself  cause the  resulting --\n executable to be covered by  the GNU General Public License.  This --\n exception does  not however invalidate  any other reasons  why the --\n executable file might be covered by the GNU Public License.        --\n                                                                    --\n The McKae Software Utilities  are maintained by McKae Technologies --\n (http://www.mckae.com).                                            --\n----------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "McKae.XML.EZ_Out",
    qualified_name: "McKae.XML.EZ_Out",
    signature: "mckae.xml.ez_out",
    enclosing: "mckae.xml",
    is_private: false,
    documentation: "This package is the parent package for a collection of packages\n that provide a simple means of XML output generation to a\n variety of output media.",
    documentation_snippet: "",
    },
    {
    name: "McKae.XML.EZ_Out.Generic_Medium",
    qualified_name: "McKae.XML.EZ_Out.Generic_Medium",
    signature: "mckae.xml.ez_out.generic_medium",
    enclosing: "mckae.xml.ez_out",
    is_private: false,
    documentation: "-----------------------------------------------------------------\n This package provides the means to easily write XML elements and\n  associated attributes to a provided medium that provides the\n  required interface.\n\n@formal Output_Medium\n@formal Put\n@formal New_Line\n   DEPRECATED\n   Control formatting by setting the Current_Format variable in the\n   package spec.\n  \n   Specify whether the XML that is created is to have indenting and\n   line breaks.\n@formal Format\n  DEPRECATED\n  The maximum element nesting depth of an XML document\n@formal Max_Element_Nesting",
    documentation_snippet: "",
    },
    {
    name: "Mckae.XML.EZ_Out.String_Stream",
    qualified_name: "Mckae.XML.EZ_Out.String_Stream",
    signature: "mckae.xml.ez_out.string_stream",
    enclosing: "mckae.xml.ez_out",
    is_private: false,
    documentation: "A basic in-memory string-based XML document construction\n utility.  This is not intended to be a robust, full-function\n memory buffering package.",
    documentation_snippet: "",
    },
    {
    name: "String_Buffering",
    qualified_name: "Mckae.XML.EZ_Out.String_Stream.String_Buffering",
    signature: "mckae.xml.ez_out.string_stream.string_buffering",
    enclosing: "mckae.xml.ez_out.string_stream",
    is_private: false,
    documentation: "There's little point in having a small buffer for building XML\n documents, so the minimum size and expansion is 500 characters.",
    documentation_snippet: "",
    },
]
, subprograms: [
    {
    name: "Tmeztf",
    qualified_name: "Tmeztf",
    signature: "tmeztf()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Tmeztf",
    },
]
}
---

---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Network_Order",
qualified_name: "SAL.Network_Order",
signature: "sal.network_order",
enclosing: "sal",
is_private: false,
documentation: "Abstract :\n\nProvide conversions between network order storage element arrays\nand scalar types.\n\nNetwork order is little-bit-endian, big-byte-endian, 8 bit bytes.\n\nThe package SAL.Endianness defines the bit and word endianness for\nthe current processor.\n\nThe To_Network functions copy words from Item to Buffer (Last + 1\n..), changing to network byte order. On return, Last points to the\nlast byte written.\n\nThe From_Network functions copy words from Buffer (Last + 1 ..) to Item,\nchanging from network byte order. On return, Last points to the last byte\nread.\n\nFor scalar host types of size 16 or 32 bits, either use a type\nconversion in a call to one of the functions below, or instantiate\none of the child packages provided (to avoid the type conversion).\n\nCopyright (C) 2004, 2005, 2009, 2011, 2019 Stephen Leake.  All Rights Reserved.\n\nThis library is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or (at\nyour option) any later version. This library is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without even\nthe implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR\nPURPOSE. See the GNU General Public License for more details. You\nshould have received a copy of the GNU General Public License\ndistributed with this program; see file COPYING. If not, write to\nthe Free Software Foundation, 59 Temple Place - Suite 330, Boston,\nMA 02111-1307, USA.\n\nAs a special exception, if other files instantiate generics from\nthis unit, or you link this unit with other files to produce an\nexecutable, this  unit  does not  by itself cause  the resulting\nexecutable to be covered by the GNU General Public License. This\nexception does not however invalidate any other reasons why the\nexecutable file  might be covered by the  GNU Public License.",
documentation_snippet: "",
}
---

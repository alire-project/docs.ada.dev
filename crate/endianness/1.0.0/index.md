---
crate: endianness
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Endianness",
    qualified_name: "Endianness",
    signature: "endianness",
    enclosing: "",
    is_private: false,
    documentation: "@summary\nConvenience subprograms to convert between Big- and Little-endianness\n\n@description\nThis package contains a few convenient subprograms that allow you to\nsimply switch between native endianness of the running system and big\nor little endianness. Ada's byte order handling is quite sophisticated\nand it doesn't provide such routines at all. Hopefully, there is a\nGNAT.Byte_Swapping available in GNAT, but it only allows for simple\nswapping of bytes.\nThis package is built on top of GNAT.Byte_Swapping, but provides much\nsimpler programming interface.\n\nThis package provides generic function interfaces, but mostly you would\nbe better off utilizing already instantiated Endiannes.Standard and\nEndianness.Interfaces packages which initialize all of the provided\nfunctions for compatible types from Standard and Interfaces packages,\nrespectively.",
    documentation_snippet: "",
    },
    {
    name: "Endianness.Interfaces",
    qualified_name: "Endianness.Interfaces",
    signature: "endianness.interfaces",
    enclosing: "endianness",
    is_private: false,
    documentation: "@summary\nInstance of Endianness' functions for Interfaces' integer types",
    documentation_snippet: "",
    },
    {
    name: "Endianness.Standard",
    qualified_name: "Endianness.Standard",
    signature: "endianness.standard",
    enclosing: "endianness",
    is_private: false,
    documentation: "@summary\nInstance of Endianness' functions for Standard integer types",
    documentation_snippet: "",
    },
]
}
---

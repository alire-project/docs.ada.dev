---
crate: system_random
layout: gnatdoc
gnatdoc: {
name: "System_Random",
qualified_name: "System_Random",
signature: "system_random",
enclosing: "",
is_private: false,
documentation: "@summary\nAda interface to system sources of randomness\n\n@description\nThis package provides generic interface to OS' sources of randomeness.\nOn Windows, BCryptGenRandom() is used, on other platforms such as Linux,\nBSD, Mac OS portable getentropy() is used.\n\nThis is a generic package as it is intended to be used with user-defined\nbyte array type, that would later be converted to a seed value used to\nseed an appropriate strong PRNG algorithm.\n\n@formal Element\n  ELement type, must be mod 2**8, i.e. represent a byte\n@formal Index\n  Index type\n@formal Element_Array\n  An array of aliased Elements",
documentation_snippet: "",
}
---

---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Fmap",
qualified_name: "Fmap",
signature: "fmap",
enclosing: "",
is_private: false,
documentation: "This package keeps two mappings: from unit names to file names,\nand from file names to path names.\n\nThis mapping is used to communicate between the builder (gnatmake or\ngprbuild) and the compiler. The format of this mapping file is the\nfollowing:\nFor each source file, there are three lines in the mapping file:\n  Unit name with %b or %s added depending on whether it is a body or a spec\n            This line is omitted for file-based languages\n  File name\n  Path name (set to '/' if the file should be ignored in fact, ie for\n             a Locally_Removed_File in a project)",
documentation_snippet: "",
}
---

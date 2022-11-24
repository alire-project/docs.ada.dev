---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Internal.Conversions",
qualified_name: "Langkit_Support.Internal.Conversions",
signature: "langkit_support.internal.conversions",
enclosing: "langkit_support.internal",
is_private: false,
documentation: "Conversions between public and internal types.\n\nThese converters need visibility over the implementation details of the\npublic types (for instance components of Lk_Node), but we do not want to\nexpose them in the Langkit_Support.Generic_API package tree: publish\nhere declarations as proxies to the implementations in\nLangkit_Support.Generic_API bodies.\n\nConverters for analysis contexts.  See the corresponding export\ndeclaration in Langkit_Support.Generic_API.Analysis.",
documentation_snippet: "",
}
---

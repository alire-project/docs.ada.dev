---
crate: uri_ada
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "URI_Ada",
    qualified_name: "URI_Ada",
    signature: "uri_ada",
    enclosing: "",
    is_private: false,
    documentation: "Helper functions to identify URLs and their components.\n\nSee https://tools.ietf.org/html/rfc3986 for full details.\n\nhttp://user:pass@www.here.com:80/dir1/dir2/xyz.html?p=8&x=doh#anchor\n |                    |       | |          |       |         |\n protocol             host port path       file   parameters fragment\n\n      foo://example.com:8042/over/there?name=ferret#nose\n      \\_/   \\______________/\\_________/ \\_________/ \\__/\n       |           |            |            |        |\n    scheme     authority       path        query   fragment\n       |   _____________________|__\n      / \\ /                        \\\n      urn:example:animal:ferret:nose",
    documentation_snippet: "",
    },
]
, renamings: [
    {
    name: "URI",
    qualified_name: "URI",
    signature: "uri",
    enclosing: "",
    is_private: false,
    documentation: "Transitional, to be removed in next major version",
    documentation_snippet: "package URI renames URI_Ada;",
    },
]
, subprograms: [
    {
    name: "URI_Ada.Test",
    qualified_name: "URI_Ada.Test",
    signature: "uri_ada().test()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure URI_Ada.Test",
    },
]
}
---

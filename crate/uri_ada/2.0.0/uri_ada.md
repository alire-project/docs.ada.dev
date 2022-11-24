---
crate: uri_ada
layout: gnatdoc
gnatdoc: {
name: "URI_Ada",
qualified_name: "URI_Ada",
signature: "uri_ada",
enclosing: "",
is_private: false,
documentation: "Helper functions to identify URLs and their components.\n\nSee https://tools.ietf.org/html/rfc3986 for full details.\n\nhttp://user:pass@www.here.com:80/dir1/dir2/xyz.html?p=8&x=doh#anchor\n |                    |       | |          |       |         |\n protocol             host port path       file   parameters fragment\n\n      foo://example.com:8042/over/there?name=ferret#nose\n      \\_/   \\______________/\\_________/ \\_________/ \\__/\n       |           |            |            |        |\n    scheme     authority       path        query   fragment\n       |   _____________________|__\n      / \\ /                        \\\n      urn:example:animal:ferret:nose",
documentation_snippet: "",
simple_types:    [
       {
       name: "Parts",
       qualified_name: "URI_Ada.Parts",
       signature: "uri_ada.parts",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Parts is\n  (Scheme,\n   Authority,\n   Path,\n   Query,\n   Fragment);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Authority_String",
       qualified_name: "URI_Ada.Authority_String",
       signature: "uri_ada.authority_string",
       enclosing: "",
       is_private: false,
       documentation: "These operate on a previously extracted authority part, not a full URL.\nThey will return an empty string if the corresponding part is missing",
       documentation_snippet: "subtype Authority_String is String;",
       }   ,
   ]
,}
---

---
crate: ada_fuse
layout: gnatdoc
gnatdoc: {
name: "Fuse.Aux",
qualified_name: "Fuse.Aux",
signature: "fuse.aux",
enclosing: "fuse",
is_private: false,
documentation: "Auxiliary functions for passthrough filesystems.\n\nJust call these in your filesystem implementation or copy them if\nyou want to modify the behaviour.\n\nWe cannot read errno yet. So we just catch the most common errors\nby hand. If anything goes wrong an exception is raised and we\nreturn an IO error (EIO).",
documentation_snippet: "",
}
---

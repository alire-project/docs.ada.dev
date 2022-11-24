---
crate: ada_lua
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Lua",
    qualified_name: "Lua",
    signature: "lua",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Lua.Ada_Limited_Types",
    qualified_name: "Lua.Ada_Limited_Types",
    signature: "lua.ada_limited_types",
    enclosing: "lua",
    is_private: false,
    documentation: "Generic package that ease export and import to Lua of Ada limited types.\nNote that because of limitation of limited types, the To_Ada function\nreturns an access to the value instead of the value itself.\n\nOne approach to import a value from Lua is to do the following\n\ndeclare\n  Var : Ada_Type renames To_Ada (State, -1);\nbegin\n\nNote also that internally we are using light user data. In that case no\nuser data can be associated with the Lua object, so we cannot perform any\ntype checks when importing from Lua.\n\n@formal Ada_Type",
    documentation_snippet: "",
    },
    {
    name: "Lua.Ada_Types",
    qualified_name: "Lua.Ada_Types",
    signature: "lua.ada_types",
    enclosing: "lua",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Lua.Utils",
    qualified_name: "Lua.Utils",
    signature: "lua.utils",
    enclosing: "lua",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
]
}
---

---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Generic_API",
qualified_name: "Libadalang.Generic_API",
signature: "libadalang.generic_api",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
constants:    [
       {
       name: "Ada_Lang_Id",
       qualified_name: "Libadalang.Generic_API.Ada_Lang_Id",
       signature: "libadalang.generic_api.ada_lang_id",
       enclosing: "",
       is_private: false,
       documentation: "Unique identifier for Libadalang",
       documentation_snippet: "Ada_Lang_Id : constant Language_Id\n  with Import, External_Name => \"Libadalang__language_id\";",
       }   ,
   ]
,variables:    [
       {
       name: "Self_Id",
       qualified_name: "Libadalang.Generic_API.Self_Id",
       signature: "libadalang.generic_api.self_id",
       enclosing: "",
       is_private: false,
       documentation: "Shortcut for convenience in code generation",
       documentation_snippet: "Self_Id : Language_Id renames Ada_Lang_Id;",
       }   ,
   ]
,}
---

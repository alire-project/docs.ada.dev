---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "Projectile",
qualified_name: "Projectile",
signature: "projectile",
enclosing: "",
is_private: false,
documentation: "Shoot'n'loot\nCopyright (c) 2020 Fabien Chouteau",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Instance",
       qualified_name: "Projectile.Instance",
       signature: "projectile.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance\n  (Bank       : not null GESTE.Tile_Bank.Const_Ref;\n   Init_Frame : GESTE_Config.Tile_Index)\nis tagged limited\nprivate;",
       }   ,
   ]
,access_types:    [
       {
       name: "Ref",
       qualified_name: "Projectile.Ref",
       signature: "projectile.ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ref is access all Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "Projectile.Class",
       signature: "projectile.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
   ]
,}
---

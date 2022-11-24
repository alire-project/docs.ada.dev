---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Plugin.Pixi.Sprite",
qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite",
signature: "gnoga.gui.plugin.pixi.sprite",
enclosing: "gnoga.gui.plugin.pixi",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Sprite_Types\n-----------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Effect_Type",
       qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite.Effect_Type",
       signature: "gnoga.gui.plugin.pixi.sprite.effect_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Null_Effect\n  None effect\n@enum Bounce_Effect\n  Sprite bounces inside frame or angle limit\n@enum Loop_Effect\n  Sprite loops around frame or angle limit\n@enum Inside_Event_Effect\n  Event is sent when sprite is inside frame or angle and resets when fired\n@enum Outside_Event_Effect",
       documentation_snippet: "type Effect_Type is\n  (Null_Effect,\n   Bounce_Effect,\n   Loop_Effect,\n   Inside_Event_Effect,\n   Outside_Event_Effect);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Sprite_Type",
       qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite.Sprite_Type",
       signature: "gnoga.gui.plugin.pixi.sprite.sprite_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sprite_Type is new Container_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer_To_Sprite_Class",
       qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite.Pointer_To_Sprite_Class",
       signature: "gnoga.gui.plugin.pixi.sprite.pointer_to_sprite_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Sprite_Class is access all Sprite_Type'Class;",
       }   ,
       {
       name: "Sprite_Access",
       qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite.Sprite_Access",
       signature: "gnoga.gui.plugin.pixi.sprite.sprite_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sprite_Access is access all Sprite_Type;",
       }   ,
       {
       name: "Sprite_Event",
       qualified_name: "Gnoga.Gui.Plugin.Pixi.Sprite.Sprite_Event",
       signature: "gnoga.gui.plugin.pixi.sprite.sprite_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sprite_Event is access procedure\n  (Object       : in out Gnoga.Gui.Base.Base_Type'Class;\n   Effect_Event : in     Effect_Type);",
       }   ,
   ]
,}
---

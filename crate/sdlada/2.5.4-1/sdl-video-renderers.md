---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Renderers",
qualified_name: "SDL.Video.Renderers",
signature: "sdl.video.renderers",
enclosing: "sdl.video",
is_private: false,
documentation: "TODO: Finish this.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Renderer_Flags",
       qualified_name: "SDL.Video.Renderers.Renderer_Flags",
       signature: "sdl.video.renderers.renderer_flags",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Renderer_Flags is mod 2 ** 32 with\n  Convention => C;",
       }   ,
       {
       name: "Renderer_Flip",
       qualified_name: "SDL.Video.Renderers.Renderer_Flip",
       signature: "sdl.video.renderers.renderer_flip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Renderer_Flip is (None, Horizontal, Vertical, Both);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Renderer",
       qualified_name: "SDL.Video.Renderers.Renderer",
       signature: "sdl.video.renderers.renderer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Renderer is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Accelerated",
       qualified_name: "SDL.Video.Renderers.Accelerated",
       signature: "sdl.video.renderers.accelerated",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Accelerated            : constant Renderer_Flags := 16#0000_0002#;",
       }   ,
       {
       name: "Default_Renderer_Flags",
       qualified_name: "SDL.Video.Renderers.Default_Renderer_Flags",
       signature: "sdl.video.renderers.default_renderer_flags",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Renderer_Flags : constant Renderer_Flags := 16#0000_0000#;",
       }   ,
       {
       name: "Null_Renderer",
       qualified_name: "SDL.Video.Renderers.Null_Renderer",
       signature: "sdl.video.renderers.null_renderer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Renderer : constant Renderer;",
       }   ,
       {
       name: "Present_V_Sync",
       qualified_name: "SDL.Video.Renderers.Present_V_Sync",
       signature: "sdl.video.renderers.present_v_sync",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Present_V_Sync         : constant Renderer_Flags := 16#0000_0004#;",
       }   ,
       {
       name: "Software",
       qualified_name: "SDL.Video.Renderers.Software",
       signature: "sdl.video.renderers.software",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Software               : constant Renderer_Flags := 16#0000_0001#;",
       }   ,
       {
       name: "Target_Texture",
       qualified_name: "SDL.Video.Renderers.Target_Texture",
       signature: "sdl.video.renderers.target_texture",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Target_Texture         : constant Renderer_Flags := 16#0000_0008#;",
       }   ,
   ]
,}
---

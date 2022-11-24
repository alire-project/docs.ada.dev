---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Hints",
qualified_name: "SDL.Hints",
signature: "sdl.hints",
enclosing: "sdl",
is_private: false,
documentation: "TODO: Make this more robust using more functions and platform specific\npackages with error checking on returned values?\nWould be nice to have the compiler only allow that which is allowed on\na particular platform.\nIt would be nice to have the binding test the return values as well,\nraising an exception on values that are just wrong for a particular\nplatform, i.e. direct3d on Linux or Mac? Exception raised!",
documentation_snippet: "",
simple_types:    [
       {
       name: "Hint",
       qualified_name: "SDL.Hints.Hint",
       signature: "sdl.hints.hint",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Frame_Buffer_Acceleration\n@enum Render_Driver\n@enum Render_OpenGL_Shaders\n@enum Render_Scale_Quality\n@enum Render_VSync\n@enum Video_X11_XVidMode\n@enum Video_X11_Xinerama\n@enum Video_X11_XRandR\n@enum Grab_Keyboard\n@enum Video_Minimise_On_Focus_Loss\n@enum Idle_Timer_Disabled\n@enum IOS_Orientations\n@enum XInput_Enabled\n  win\n@enum Game_Controller_Config\n  win, mac, linux\n@enum Joystick_Allow_Background_Events\n@enum Allow_Topmost\n@enum Timer_Resolution\n  win7 and earlier",
       documentation_snippet: "type Hint is\n  (Frame_Buffer_Acceleration,\n   Render_Driver,\n   Render_OpenGL_Shaders,\n   Render_Scale_Quality,\n   Render_VSync,\n   Video_X11_XVidMode,\n   Video_X11_Xinerama,\n   Video_X11_XRandR,\n   Grab_Keyboard,\n   Video_Minimise_On_Focus_Loss,\n   Idle_Timer_Disabled,\n   IOS_Orientations,\n   XInput_Enabled,\n   Game_Controller_Config,\n   Joystick_Allow_Background_Events,\n   Allow_Topmost,\n   Timer_Resolution) with\n  Discard_Names => True;",
       }   ,
       {
       name: "Priorities",
       qualified_name: "SDL.Hints.Priorities",
       signature: "sdl.hints.priorities",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Priorities is (Default, Normal, Override) with\n  Convention => C;",
       }   ,
   ]
,}
---

---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Video.Windows.Manager",
qualified_name: "SDL.Video.Windows.Manager",
signature: "sdl.video.windows.manager",
enclosing: "sdl.video.windows",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Android",
       qualified_name: "SDL.Video.Windows.Manager.Android",
       signature: "sdl.video.windows.manager.android",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "EGL_Surface",
              qualified_name: "SDL.Video.Windows.Manager.Android.EGL_Surface",
              signature: "sdl.video.windows.manager.android.egl_surface",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type EGL_Surface   is new C_Address;",
              }          ,
              {
              name: "Native_Window",
              qualified_name: "SDL.Video.Windows.Manager.Android.Native_Window",
              signature: "sdl.video.windows.manager.android.native_window",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Native_Window is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "Cocoa",
       qualified_name: "SDL.Video.Windows.Manager.Cocoa",
       signature: "sdl.video.windows.manager.cocoa",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "NS_Window",
              qualified_name: "SDL.Video.Windows.Manager.Cocoa.NS_Window",
              signature: "sdl.video.windows.manager.cocoa.ns_window",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type NS_Window is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "Direct_FB",
       qualified_name: "SDL.Video.Windows.Manager.Direct_FB",
       signature: "sdl.video.windows.manager.direct_fb",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Direct_FB",
              qualified_name: "SDL.Video.Windows.Manager.Direct_FB.Direct_FB",
              signature: "sdl.video.windows.manager.direct_fb.direct_fb",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Direct_FB         is new C_Address;",
              }          ,
              {
              name: "Direct_FB_Surface",
              qualified_name: "SDL.Video.Windows.Manager.Direct_FB.Direct_FB_Surface",
              signature: "sdl.video.windows.manager.direct_fb.direct_fb_surface",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Direct_FB_Surface is new C_Address;",
              }          ,
              {
              name: "Direct_FB_Window",
              qualified_name: "SDL.Video.Windows.Manager.Direct_FB.Direct_FB_Window",
              signature: "sdl.video.windows.manager.direct_fb.direct_fb_window",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Direct_FB_Window  is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "Mir",
       qualified_name: "SDL.Video.Windows.Manager.Mir",
       signature: "sdl.video.windows.manager.mir",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Connection",
              qualified_name: "SDL.Video.Windows.Manager.Mir.Connection",
              signature: "sdl.video.windows.manager.mir.connection",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Connection is new C_Address;",
              }          ,
              {
              name: "Surface",
              qualified_name: "SDL.Video.Windows.Manager.Mir.Surface",
              signature: "sdl.video.windows.manager.mir.surface",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Surface    is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "UI_Kit",
       qualified_name: "SDL.Video.Windows.Manager.UI_Kit",
       signature: "sdl.video.windows.manager.ui_kit",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Window",
              qualified_name: "SDL.Video.Windows.Manager.UI_Kit.Window",
              signature: "sdl.video.windows.manager.ui_kit.window",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Window is new C_Address;",
              }          ,
          ]
,variables:           [
              {
              name: "Colour_Buffer",
              qualified_name: "SDL.Video.Windows.Manager.UI_Kit.Colour_Buffer",
              signature: "sdl.video.windows.manager.ui_kit.colour_buffer",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Colour_Buffer        : C.unsigned;",
              }          ,
              {
              name: "Frame_Buffer",
              qualified_name: "SDL.Video.Windows.Manager.UI_Kit.Frame_Buffer",
              signature: "sdl.video.windows.manager.ui_kit.frame_buffer",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Frame_Buffer         : C.unsigned;",
              }          ,
              {
              name: "Resolve_Frame_Buffer",
              qualified_name: "SDL.Video.Windows.Manager.UI_Kit.Resolve_Frame_Buffer",
              signature: "sdl.video.windows.manager.ui_kit.resolve_frame_buffer",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Resolve_Frame_Buffer : C.unsigned;",
              }          ,
          ]
,       }   ,
       {
       name: "Wayland",
       qualified_name: "SDL.Video.Windows.Manager.Wayland",
       signature: "sdl.video.windows.manager.wayland",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Display",
              qualified_name: "SDL.Video.Windows.Manager.Wayland.Display",
              signature: "sdl.video.windows.manager.wayland.display",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Display       is new C_Address;",
              }          ,
              {
              name: "Shell_Surface",
              qualified_name: "SDL.Video.Windows.Manager.Wayland.Shell_Surface",
              signature: "sdl.video.windows.manager.wayland.shell_surface",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Shell_Surface is new C_Address;",
              }          ,
              {
              name: "Surface",
              qualified_name: "SDL.Video.Windows.Manager.Wayland.Surface",
              signature: "sdl.video.windows.manager.wayland.surface",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Surface       is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "Win_RT",
       qualified_name: "SDL.Video.Windows.Manager.Win_RT",
       signature: "sdl.video.windows.manager.win_rt",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Inspectable",
              qualified_name: "SDL.Video.Windows.Manager.Win_RT.Inspectable",
              signature: "sdl.video.windows.manager.win_rt.inspectable",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Inspectable is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "Windows",
       qualified_name: "SDL.Video.Windows.Manager.Windows",
       signature: "sdl.video.windows.manager.windows",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "HDCs",
              qualified_name: "SDL.Video.Windows.Manager.Windows.HDCs",
              signature: "sdl.video.windows.manager.windows.hdcs",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type HDCs  is new C_Address;",
              }          ,
              {
              name: "HWNDs",
              qualified_name: "SDL.Video.Windows.Manager.Windows.HWNDs",
              signature: "sdl.video.windows.manager.windows.hwnds",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type HWNDs is new C_Address;",
              }          ,
          ]
,       }   ,
       {
       name: "X11",
       qualified_name: "SDL.Video.Windows.Manager.X11",
       signature: "sdl.video.windows.manager.x11",
       enclosing: "sdl.video.windows.manager",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Display",
              qualified_name: "SDL.Video.Windows.Manager.X11.Display",
              signature: "sdl.video.windows.manager.x11.display",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Display is new C_Address;",
              }          ,
              {
              name: "Window",
              qualified_name: "SDL.Video.Windows.Manager.X11.Window",
              signature: "sdl.video.windows.manager.x11.window",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Window  is new Interfaces.Unsigned_32;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "WM_Types",
       qualified_name: "SDL.Video.Windows.Manager.WM_Types",
       signature: "sdl.video.windows.manager.wm_types",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WM_Types is (WM_Unknown,\n                  WM_Windows,\n                  WM_X11,\n                  WM_Direct_FB,\n                  WM_Cocoa,\n                  WM_UI_Kit,\n                  WM_Wayland,\n                  WM_Mir,\n                  WM_Win_RT,\n                  WM_Android) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Information",
       qualified_name: "SDL.Video.Windows.Manager.Information",
       signature: "sdl.video.windows.manager.information",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Information (WM : WM_Types) is\n   record\n      case WM is\n         when WM_Unknown =>\n            null;\n         when WM_Windows =>\n            HWND                     : Windows.HWNDs;\n            HDC                      : Windows.HDCs;\n         when WM_Win_RT =>\n            RT_Inspectable           : Win_RT.Inspectable;\n         when WM_X11 =>\n            X11_Display              : X11.Display;\n            X11_Window               : X11.Window;\n         when WM_Direct_FB =>\n            DFB_Main_Interface       : Direct_FB.Direct_FB;\n            DFB_Window               : Direct_FB.Direct_FB_Window;\n            DFB_Surface              : Direct_FB.Direct_FB_Surface;\n         when WM_Cocoa =>\n            Cocoa_Window             : Cocoa.NS_Window;\n         when WM_UI_Kit =>\n            UIK_Window               : UI_Kit.Window;\n            UIK_Frame_Buffer         : UI_Kit.Window;\n            UIK_Colour_Buffer        : UI_Kit.Window;\n            UIK_Resolve_Frame_Buffer : UI_Kit.Window;\n         when WM_Wayland =>\n            Wayland_Display          : Wayland.Display;\n            Wayland_Surface          : Wayland.Surface;\n            Wayland_Shell_Surface    : Wayland.Shell_Surface;\n         when WM_Mir =>\n            Mir_Connection           : Mir.Connection;\n            Mir_Surface              : Mir.Surface;\n         when WM_Android =>\n            Android_Window           : Android.Native_Window;\n            Android_Surface          : Android.EGL_Surface;\n      end case;\n   end record with\n  Unchecked_Union;",
       }   ,
       {
       name: "WM_Info",
       qualified_name: "SDL.Video.Windows.Manager.WM_Info",
       signature: "sdl.video.windows.manager.wm_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WM_Info is\n   record\n      Version    : SDL.Versions.Version;\n      Sub_System : WM_Types;\n      Info       : Information (WM => WM_Unknown);\n   end record with\n  Convention => C;",
       }   ,
   ]
,access_types:    [
       {
       name: "C_Address",
       qualified_name: "SDL.Video.Windows.Manager.C_Address",
       signature: "sdl.video.windows.manager.c_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type C_Address is access all Interfaces.Unsigned_32 with\n  Convention => C;",
       }   ,
   ]
,}
---

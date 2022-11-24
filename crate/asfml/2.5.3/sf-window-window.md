---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Window.Window",
qualified_name: "Sf.Window.Window",
signature: "sf.window.window",
enclosing: "sf.window",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Enumeration of window creation styles\n/\n//////////////////////////////////////////////////////////\n/< No border / title bar (this flag and all others are mutually exclusive)\n/< Title bar + fixed border\n/< Titlebar + resizable border + maximize button\n/< Titlebar + close button\n/< Fullscreen mode (this flag and all others are mutually exclusive)\n/< Default window style",
documentation_snippet: "",
simple_types:    [
       {
       name: "sfContextAttribute",
       qualified_name: "Sf.Window.Window.sfContextAttribute",
       signature: "sf.window.window.sfcontextattribute",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfContextAttribute is new sfUint32;",
       }   ,
       {
       name: "sfWindowStyle",
       qualified_name: "Sf.Window.Window.sfWindowStyle",
       signature: "sf.window.window.sfwindowstyle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfWindowStyle is new sfUint32;",
       }   ,
   ]
,record_types:    [
       {
       name: "sfContextSettings",
       qualified_name: "Sf.Window.Window.sfContextSettings",
       signature: "sf.window.window.sfcontextsettings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfContextSettings is record\n   depthBits : aliased sfUint32;\n   stencilBits : aliased sfUint32;\n   antialiasingLevel : aliased sfUint32;\n   majorVersion : aliased sfUint32;\n   minorVersion : aliased sfUint32;\n   attributeFlags : aliased sfUint32;\n   sRgbCapable : aliased sfBool;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "sfClose",
       qualified_name: "Sf.Window.Window.sfClose",
       signature: "sf.window.window.sfclose",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfClose : constant sfWindowStyle := 4;",
       }   ,
       {
       name: "sfContextCore",
       qualified_name: "Sf.Window.Window.sfContextCore",
       signature: "sf.window.window.sfcontextcore",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfContextCore : constant sfContextAttribute := 1;",
       }   ,
       {
       name: "sfContextDebug",
       qualified_name: "Sf.Window.Window.sfContextDebug",
       signature: "sf.window.window.sfcontextdebug",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfContextDebug : constant sfContextAttribute := 4;",
       }   ,
       {
       name: "sfContextDefault",
       qualified_name: "Sf.Window.Window.sfContextDefault",
       signature: "sf.window.window.sfcontextdefault",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfContextDefault : constant sfContextAttribute := 0;",
       }   ,
       {
       name: "sfDefaultContextSettings",
       qualified_name: "Sf.Window.Window.sfDefaultContextSettings",
       signature: "sf.window.window.sfdefaultcontextsettings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfDefaultContextSettings : constant sfContextSettings;",
       }   ,
       {
       name: "sfDefaultStyle",
       qualified_name: "Sf.Window.Window.sfDefaultStyle",
       signature: "sf.window.window.sfdefaultstyle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfDefaultStyle : constant sfWindowStyle := 7;",
       }   ,
       {
       name: "sfFullscreen",
       qualified_name: "Sf.Window.Window.sfFullscreen",
       signature: "sf.window.window.sffullscreen",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfFullscreen : constant sfWindowStyle := 8;",
       }   ,
       {
       name: "sfNone",
       qualified_name: "Sf.Window.Window.sfNone",
       signature: "sf.window.window.sfnone",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfNone : constant sfWindowStyle := 0;",
       }   ,
       {
       name: "sfResize",
       qualified_name: "Sf.Window.Window.sfResize",
       signature: "sf.window.window.sfresize",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfResize : constant sfWindowStyle := 2;",
       }   ,
       {
       name: "sfTitlebar",
       qualified_name: "Sf.Window.Window.sfTitlebar",
       signature: "sf.window.window.sftitlebar",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTitlebar : constant sfWindowStyle := 1;",
       }   ,
   ]
,}
---
---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Images",
qualified_name: "SDL.Images",
signature: "sdl.images",
enclosing: "sdl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Formats",
       qualified_name: "SDL.Images.Formats",
       signature: "sdl.images.formats",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Formats is (Targa, Cursor, Icon, BMP, GIF, JPG, LBM, PCX, PNG, PNM, TIFF, XCF, XPM, XV, WEBP);",
       }   ,
       {
       name: "Init_Image_Flags",
       qualified_name: "SDL.Images.Init_Image_Flags",
       signature: "sdl.images.init_image_flags",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Init_Image_Flags is new SDL.Init_Flags;",
       }   ,
   ]
,constants:    [
       {
       name: "Enable_Everything",
       qualified_name: "SDL.Images.Enable_Everything",
       signature: "sdl.images.enable_everything",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Enable_Everything : constant Init_Image_Flags := Enable_JPG or Enable_PNG or Enable_TIFF or Enable_WEBP;",
       }   ,
       {
       name: "Enable_JPG",
       qualified_name: "SDL.Images.Enable_JPG",
       signature: "sdl.images.enable_jpg",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Enable_JPG        : constant Init_Image_Flags := 16#0000_0001#;",
       }   ,
       {
       name: "Enable_PNG",
       qualified_name: "SDL.Images.Enable_PNG",
       signature: "sdl.images.enable_png",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Enable_PNG        : constant Init_Image_Flags := 16#0000_0002#;",
       }   ,
       {
       name: "Enable_TIFF",
       qualified_name: "SDL.Images.Enable_TIFF",
       signature: "sdl.images.enable_tiff",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Enable_TIFF       : constant Init_Image_Flags := 16#0000_0004#;",
       }   ,
       {
       name: "Enable_WEBP",
       qualified_name: "SDL.Images.Enable_WEBP",
       signature: "sdl.images.enable_webp",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Enable_WEBP       : constant Init_Image_Flags := 16#0000_0008#;",
       }   ,
   ]
,}
---

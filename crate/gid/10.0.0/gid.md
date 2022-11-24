---
crate: gid
layout: gnatdoc
gnatdoc: {
name: "GID",
qualified_name: "GID",
signature: "gid",
enclosing: "",
is_private: false,
documentation: "-------------------------------
documentation_snippet: "",
simple_types:    [
       {
       name: "Display_mode",
       qualified_name: "GID.Display_mode",
       signature: "gid.display_mode",
       enclosing: "",
       is_private: false,
       documentation: "For bitmap pictures, the result is exactly the same, but
       documentation_snippet: "type Display_mode is (fast, nice);",
       }   ,
       {
       name: "Image_descriptor",
       qualified_name: "GID.Image_descriptor",
       signature: "gid.image_descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Image_descriptor is private;",
       }   ,
       {
       name: "Image_format_type",
       qualified_name: "GID.Image_format_type",
       signature: "gid.image_format_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Image_format_type is\n  (\n    BMP, FITS, GIF, JPEG, PNG, PNM, QOI, TGA, TIFF\n  );",
       }   ,
       {
       name: "Orientation",
       qualified_name: "GID.Orientation",
       signature: "gid.orientation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Orientation is (\n  Unchanged,\n  Rotation_90, Rotation_180, Rotation_270\n);",
       }   ,
   ]
,constants:    [
       {
       name: "reference",
       qualified_name: "GID.reference",
       signature: "gid.reference",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL..........^
       documentation_snippet: "reference : constant String := \"14-Apr-2022\";",
       }   ,
       {
       name: "version",
       qualified_name: "GID.version",
       signature: "gid.version",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL..........^
       documentation_snippet: "version   : constant String := \"010\";",
       }   ,
       {
       name: "web",
       qualified_name: "GID.web",
       signature: "gid.web",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL..........^
       documentation_snippet: "web       : constant String := \"http://gen-img-dec.sf.net/\";",
       }   ,
   ]
,}
---
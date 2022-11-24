---
crate: gid
layout: gnatdoc
gnatdoc: {
name: "GID",
qualified_name: "GID",
signature: "gid",
enclosing: "",
is_private: false,
documentation: "-------------------------------\n GID - Generic Image Decoder --\n-------------------------------\n\n  Purpose:\n\n     The Generic Image Decoder is a package for decoding a broad\n     variety of image formats, from any data stream, to any kind\n     of medium, be it an in-memory bitmap, a GUI object,\n     some other stream, arrays of floating-point initial data\n     for scientific calculations, a browser element, a device,...\n     Animations are supported.\n\n     The code is unconditionally portable, independent of the\n     choice of operating system, processor, endianess and compiler.\n\n  Image types currently supported:\n\n     BMP, GIF, JPEG, PNG, PNM, QOI, TGA\n\n  Credits:\n\n     - André van Splunter: GIF's LZW decoder in Ada\n     - Martin J. Fiedler: most of the JPEG decoder (from NanoJPEG)\n\n     More credits in gid_work.xls, sheet \"credits\".\n\n  Copyright (c) Gautier de Montmollin 2010 .. 2022\n\n  Permission is hereby granted, free of charge, to any person obtaining a copy\n  of this software and associated documentation files (the \"Software\"), to deal\n  in the Software without restriction, including without limitation the rights\n  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n  copies of the Software, and to permit persons to whom the Software is\n  furnished to do so, subject to the following conditions:\n\n  The above copyright notice and this permission notice shall be included in\n  all copies or substantial portions of the Software.\n\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n  THE SOFTWARE.\n\n  NB: this is the MIT License, as found 2-May-2010 on the site\n  http://www.opensource.org/licenses/mit-license.php",
documentation_snippet: "",
simple_types:    [
       {
       name: "Display_mode",
       qualified_name: "GID.Display_mode",
       signature: "gid.display_mode",
       enclosing: "",
       is_private: false,
       documentation: "For bitmap pictures, the result is exactly the same, but\ninterlaced images' larger pixels are drawn in full during decoding.\n\n@enum fast\n@enum nice",
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
       documentation: "Hopefully the latest version is at that URL..........^\nThere is a mirror too @ https://github.com/zertovitch/gid",
       documentation_snippet: "reference : constant String := \"14-Apr-2022\";",
       }   ,
       {
       name: "version",
       qualified_name: "GID.version",
       signature: "gid.version",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL..........^\nThere is a mirror too @ https://github.com/zertovitch/gid",
       documentation_snippet: "version   : constant String := \"010\";",
       }   ,
       {
       name: "web",
       qualified_name: "GID.web",
       signature: "gid.web",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL..........^\nThere is a mirror too @ https://github.com/zertovitch/gid",
       documentation_snippet: "web       : constant String := \"http://gen-img-dec.sf.net/\";",
       }   ,
   ]
,}
---

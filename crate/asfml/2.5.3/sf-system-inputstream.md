---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.System.InputStream",
qualified_name: "Sf.System.InputStream",
signature: "sf.system.inputstream",
enclosing: "sf.system",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
record_types:    [
       {
       name: "sfInputStream",
       qualified_name: "Sf.System.InputStream.sfInputStream",
       signature: "sf.system.inputstream.sfinputstream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInputStream is record\n   read     : sfInputStreamReadFunc;\n   seek     : sfInputStreamSeekFunc;\n   tell     : sfInputStreamTellFunc;\n   getSize  : sfInputStreamGetSizeFunc;\n   userData : Standard.System.Address;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "sfInputStreamGetSizeFunc",
       qualified_name: "Sf.System.InputStream.sfInputStreamGetSizeFunc",
       signature: "sf.system.inputstream.sfinputstreamgetsizefunc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInputStreamGetSizeFunc is access function (userData : Standard.System.Address) return sfInt64;",
       }   ,
       {
       name: "sfInputStreamReadFunc",
       qualified_name: "Sf.System.InputStream.sfInputStreamReadFunc",
       signature: "sf.system.inputstream.sfinputstreamreadfunc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInputStreamReadFunc is access function\n  (data     : Standard.System.Address;\n   size     : sfInt64;\n   userData : Standard.System.Address) return sfInt64;",
       }   ,
       {
       name: "sfInputStreamSeekFunc",
       qualified_name: "Sf.System.InputStream.sfInputStreamSeekFunc",
       signature: "sf.system.inputstream.sfinputstreamseekfunc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInputStreamSeekFunc is access function (position : sfInt64;\n                                               userData : Standard.System.Address) return sfInt64;",
       }   ,
       {
       name: "sfInputStreamTellFunc",
       qualified_name: "Sf.System.InputStream.sfInputStreamTellFunc",
       signature: "sf.system.inputstream.sfinputstreamtellfunc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInputStreamTellFunc is access function (userData : Standard.System.Address) return sfInt64;",
       }   ,
   ]
,}
---

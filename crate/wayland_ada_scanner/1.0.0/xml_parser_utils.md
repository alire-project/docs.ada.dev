---
crate: wayland_ada_scanner
layout: gnatdoc
gnatdoc: {
name: "Xml_Parser_Utils",
qualified_name: "Xml_Parser_Utils",
signature: "xml_parser_utils",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2018 - 2019 Joakim Strandberg <joakim@mequinox.se>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
record_types:    [
       {
       name: "Interval",
       qualified_name: "Xml_Parser_Utils.Interval",
       signature: "xml_parser_utils.interval",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Interval is record\n   First : Positive;\n   Last  : Natural;\nend record;",
       }   ,
       {
       name: "Intervals_Ref",
       qualified_name: "Xml_Parser_Utils.Intervals_Ref",
       signature: "xml_parser_utils.intervals_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Intervals_Ref\n  (Element : not null access constant Interval_Vectors.Vector)\nis limited null record with Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Interval_Identifier",
       qualified_name: "Xml_Parser_Utils.Interval_Identifier",
       signature: "xml_parser_utils.interval_identifier",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Interval_Identifier is tagged limited private;",
       }   ,
   ]
,}
---

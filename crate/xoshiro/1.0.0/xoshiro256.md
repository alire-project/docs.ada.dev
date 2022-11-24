---
crate: xoshiro
layout: gnatdoc
gnatdoc: {
name: "Xoshiro256",
qualified_name: "Xoshiro256",
signature: "xoshiro256",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2022 onox <denkpadje@gmail.com>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Generator",
       qualified_name: "Xoshiro256.Generator",
       signature: "xoshiro256.generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator is limited private;",
       }   ,
       {
       name: "Unsigned_64",
       qualified_name: "Xoshiro256.Unsigned_64",
       signature: "xoshiro256.unsigned_64",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unsigned_64 is mod 2 ** 64\n  with Size => 64;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Unit_Interval",
       qualified_name: "Xoshiro256.Unit_Interval",
       signature: "xoshiro256.unit_interval",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Unit_Interval is Long_Float range 0.0 .. 1.0;",
       }   ,
   ]
,}
---

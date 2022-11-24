---
crate: canberra_ada
layout: gnatdoc
gnatdoc: {
name: "Canberra",
qualified_name: "Canberra",
signature: "canberra",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2020 onox <denkpadje@gmail.com>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Role",
       qualified_name: "Canberra.Role",
       signature: "canberra.role",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Role is (Event, Music);",
       }   ,
       {
       name: "Status_Type",
       qualified_name: "Canberra.Status_Type",
       signature: "canberra.status_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Status_Type is (Available, Playing, Finished, Canceled, Failed);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Context",
       qualified_name: "Canberra.Context",
       signature: "canberra.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is tagged limited private;",
       }   ,
       {
       name: "Sound",
       qualified_name: "Canberra.Sound",
       signature: "canberra.sound",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sound is tagged limited private;",
       }   ,
   ]
,}
---

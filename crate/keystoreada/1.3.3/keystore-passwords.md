---
crate: keystoreada
layout: gnatdoc
gnatdoc: {
name: "Keystore.Passwords",
qualified_name: "Keystore.Passwords",
signature: "keystore.passwords",
enclosing: "keystore",
is_private: false,
documentation: "---------------------------------------------------------------------\n  keystore-passwords -- Password provider\n  Copyright (C) 2019 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "Provider",
       qualified_name: "Keystore.Passwords.Provider",
       signature: "keystore.passwords.provider",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Provider is limited interface;",
       }   ,
       {
       name: "Slot_Provider",
       qualified_name: "Keystore.Passwords.Slot_Provider",
       signature: "keystore.passwords.slot_provider",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Slot_Provider is limited interface and Provider;",
       }   ,
   ]
,access_types:    [
       {
       name: "Provider_Access",
       qualified_name: "Keystore.Passwords.Provider_Access",
       signature: "keystore.passwords.provider_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Provider_Access is access all Provider'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Tag_Type",
       qualified_name: "Keystore.Passwords.Tag_Type",
       signature: "keystore.passwords.tag_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Tag_Type is Interfaces.Unsigned_32;",
       }   ,
   ]
,}
---

---
crate: keystoreada
layout: gnatdoc
gnatdoc: {
name: "Keystore.Passwords.Keys",
qualified_name: "Keystore.Passwords.Keys",
signature: "keystore.passwords.keys",
enclosing: "keystore.passwords",
is_private: false,
documentation: "---------------------------------------------------------------------\n  keystore-passwords-keys -- Key provider\n  Copyright (C) 2019, 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "Key_Provider",
       qualified_name: "Keystore.Passwords.Keys.Key_Provider",
       signature: "keystore.passwords.keys.key_provider",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_Provider is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Key_Provider_Access",
       qualified_name: "Keystore.Passwords.Keys.Key_Provider_Access",
       signature: "keystore.passwords.keys.key_provider_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key_Provider_Access is access all Key_Provider'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "DEFAULT_KEY_LENGTH",
       qualified_name: "Keystore.Passwords.Keys.DEFAULT_KEY_LENGTH",
       signature: "keystore.passwords.keys.default_key_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DEFAULT_KEY_LENGTH : constant := 32 + 16 + 32;",
       }   ,
   ]
,}
---

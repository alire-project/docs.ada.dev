---
crate: keystoreada
layout: gnatdoc
gnatdoc: {
name: "Keystore.Properties",
qualified_name: "Keystore.Properties",
signature: "keystore.properties",
enclosing: "keystore",
is_private: false,
documentation: "---------------------------------------------------------------------\n  keystore-properties -- Property manager on top of keystore\n  Copyright (C) 2020 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Manager",
       qualified_name: "Keystore.Properties.Manager",
       signature: "keystore.properties.manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Manager is new Util.Properties.Manager with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Wallet_File_Access",
       qualified_name: "Keystore.Properties.Wallet_File_Access",
       signature: "keystore.properties.wallet_file_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wallet_File_Access is access all Keystore.Files.Wallet_File'Class;",
       }   ,
   ]
,}
---

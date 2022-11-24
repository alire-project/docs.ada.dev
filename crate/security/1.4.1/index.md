---
crate: security
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Security",
    qualified_name: "Security",
    signature: "security",
    enclosing: "",
    is_private: false,
    documentation: "------------------------------\nPrincipal\n------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Security.Auth",
    qualified_name: "Security.Auth",
    signature: "security.auth",
    enclosing: "security",
    is_private: false,
    documentation: "Use an authentication server implementing OpenID 2.0.",
    documentation_snippet: "",
    },
    {
    name: "Security.Contexts",
    qualified_name: "Security.Contexts",
    signature: "security.contexts",
    enclosing: "security",
    is_private: false,
    documentation: "---------------------------------------------------------------------\n  security-contexts -- Context to provide security information and verify permissions\n  Copyright (C) 2011, 2012 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Security.Controllers",
    qualified_name: "Security.Controllers",
    signature: "security.controllers",
    enclosing: "security",
    is_private: false,
    documentation: "---------------------------------------------------------------------\n  security-controllers -- Controllers to verify a security permission\n  Copyright (C) 2011, 2012 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Security.Controllers.Roles",
    qualified_name: "Security.Controllers.Roles",
    signature: "security.controllers.roles",
    enclosing: "security.controllers",
    is_private: false,
    documentation: "------------------------------\nSecurity Controller\n------------------------------\nThe <b>Role_Controller</b> implements a simple role based permissions check.\nThe permission is granted if the user has the role defined by the controller.",
    documentation_snippet: "",
    },
    {
    name: "Security.Controllers.URLs",
    qualified_name: "Security.Controllers.URLs",
    signature: "security.controllers.urls",
    enclosing: "security.controllers",
    is_private: false,
    documentation: "------------------------------\nSecurity Controller\n------------------------------\nThe <b>URL_Controller</b> implements the permission check for URL permissions.\nIt uses the URL policy manager to verify the permission.",
    documentation_snippet: "",
    },
    {
    name: "Security.OAuth",
    qualified_name: "Security.OAuth",
    signature: "security.oauth",
    enclosing: "security",
    is_private: false,
    documentation: "OAuth 2.0: Section 10.2.2. Initial Registry Contents\nRFC 6749: 11.2.2.  Initial Registry Contents",
    documentation_snippet: "",
    },
    {
    name: "Security.OAuth.Clients",
    qualified_name: "Security.OAuth.Clients",
    signature: "security.oauth.clients",
    enclosing: "security.oauth",
    is_private: false,
    documentation: "Note: OAuth 1.0 could be implemented but since it's being deprecated\nit's not worth doing it.",
    documentation_snippet: "",
    },
    {
    name: "Security.OAuth.File_Registry",
    qualified_name: "Security.OAuth.File_Registry",
    signature: "security.oauth.file_registry",
    enclosing: "security.oauth",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Security.OAuth.JWT",
    qualified_name: "Security.OAuth.JWT",
    signature: "security.oauth.jwt",
    enclosing: "security.oauth",
    is_private: false,
    documentation: "Exception raised if the encoded token is invalid or cannot be decoded.",
    documentation_snippet: "",
    },
    {
    name: "Security.OAuth.Servers",
    qualified_name: "Security.OAuth.Servers",
    signature: "security.oauth.servers",
    enclosing: "security.oauth",
    is_private: false,
    documentation: "Minimum length for the server private key (160 bits min length).\n(See NIST Special Publication 800-107)",
    documentation_snippet: "",
    },
    {
    name: "Security.Permissions",
    qualified_name: "Security.Permissions",
    signature: "security.permissions",
    enclosing: "security",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Definition",
    qualified_name: "Security.Permissions.Definition",
    signature: "security.permissions.definition",
    enclosing: "security.permissions",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Security.Policies",
    qualified_name: "Security.Policies",
    signature: "security.policies",
    enclosing: "security",
    is_private: false,
    documentation: "---------------------------------------------------------------------\n  security-policies -- Security Policies\n  Copyright (C) 2010, 2011, 2012, 2015, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Reader_Config",
    qualified_name: "Security.Policies.Reader_Config",
    signature: "security.policies.reader_config",
    enclosing: "security.policies",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Security.Policies.Roles",
    qualified_name: "Security.Policies.Roles",
    signature: "security.policies.roles",
    enclosing: "security.policies",
    is_private: false,
    documentation: "---------------------------------------------------------------------\n  security-policies-roles -- Role based policies\n  Copyright (C) 2010, 2011, 2012, 2017, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Security.Policies.URLs",
    qualified_name: "Security.Policies.URLs",
    signature: "security.policies.urls",
    enclosing: "security.policies",
    is_private: false,
    documentation: "---------------------------------------------------------------------\n  security-policies-urls -- URL security policy\n  Copyright (C) 2010, 2011, 2012, 2017, 2018, 2019 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
    documentation_snippet: "",
    },
    {
    name: "Security.Random",
    qualified_name: "Security.Random",
    signature: "security.random",
    enclosing: "security",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
]
}
---

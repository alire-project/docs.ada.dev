---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Routes.Servlets.Faces",
qualified_name: "ASF.Routes.Servlets.Faces",
signature: "asf.routes.servlets.faces",
enclosing: "asf.routes.servlets",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-routes-servlets-faces -- faces request routing\n  Copyright (C) 2015 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Faces_Route_Type",
       qualified_name: "ASF.Routes.Servlets.Faces.Faces_Route_Type",
       signature: "asf.routes.servlets.faces.faces_route_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Faces_Route_Type is new Servlet_Route_Type with record\n   View    : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Faces_Route_Type_Access",
       qualified_name: "ASF.Routes.Servlets.Faces.Faces_Route_Type_Access",
       signature: "asf.routes.servlets.faces.faces_route_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Faces_Route_Type_Access is access all Faces_Route_Type'Class;",
       }   ,
   ]
,}
---

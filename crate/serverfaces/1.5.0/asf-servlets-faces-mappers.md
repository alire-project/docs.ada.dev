---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Servlets.Faces.Mappers",
qualified_name: "ASF.Servlets.Faces.Mappers",
signature: "asf.servlets.faces.mappers",
enclosing: "asf.servlets.faces",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-servlets-faces-mappers -- Read faces specific configuration files\n  Copyright (C) 2015, 2017 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Reader_Config",
       qualified_name: "ASF.Servlets.Faces.Mappers.Reader_Config",
       signature: "asf.servlets.faces.mappers.reader_config",
       enclosing: "asf.servlets.faces.mappers",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Config",
              qualified_name: "ASF.Servlets.Faces.Mappers.Reader_Config.Config",
              signature: "asf.servlets.faces.mappers.reader_config.config",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Config : aliased Servlet_Config;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Servlet_Fields",
       qualified_name: "ASF.Servlets.Faces.Mappers.Servlet_Fields",
       signature: "asf.servlets.faces.mappers.servlet_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Fields is (URL_MAPPING, URL_PATTERN, VIEW_ID);",
       }   ,
   ]
,record_types:    [
       {
       name: "Servlet_Config",
       qualified_name: "ASF.Servlets.Faces.Mappers.Servlet_Config",
       signature: "asf.servlets.faces.mappers.servlet_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Config is limited record\n   URL_Pattern      : Util.Beans.Objects.Object;\n   View_Id          : Util.Beans.Objects.Object;\n   Handler          : Servlet_Registry_Access;\n   Context          : EL.Contexts.ELContext_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Servlet_Config_Access",
       qualified_name: "ASF.Servlets.Faces.Mappers.Servlet_Config_Access",
       signature: "asf.servlets.faces.mappers.servlet_config_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Config_Access is access all Servlet_Config;",
       }   ,
   ]
,}
---

---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Core.Mappers",
qualified_name: "Servlet.Core.Mappers",
signature: "servlet.core.mappers",
enclosing: "servlet.core",
is_private: false,
documentation: "---------------------------------------------------------------------\n  servlet-servlets-mappers -- Read servlet configuration files\n  Copyright (C) 2011, 2015, 2017 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Reader_Config",
       qualified_name: "Servlet.Core.Mappers.Reader_Config",
       signature: "servlet.core.mappers.reader_config",
       enclosing: "servlet.core.mappers",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Config",
              qualified_name: "Servlet.Core.Mappers.Reader_Config.Config",
              signature: "servlet.core.mappers.reader_config.config",
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
       qualified_name: "Servlet.Core.Mappers.Servlet_Fields",
       signature: "servlet.core.mappers.servlet_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Fields is (FILTER_MAPPING, FILTER_NAME, SERVLET_NAME,\n                        URL_PATTERN, SERVLET_MAPPING,\n                        CONTEXT_PARAM, PARAM_NAME, PARAM_VALUE,\n                        MIME_MAPPING, MIME_TYPE, EXTENSION,\n                        ERROR_PAGE, ERROR_CODE, LOCATION);",
       }   ,
   ]
,record_types:    [
       {
       name: "Servlet_Config",
       qualified_name: "Servlet.Core.Mappers.Servlet_Config",
       signature: "servlet.core.mappers.servlet_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Config is limited record\n   Filter_Name      : Util.Beans.Objects.Object;\n   Servlet_Name     : Util.Beans.Objects.Object;\n   URL_Patterns     : Util.Beans.Objects.Vectors.Vector;\n   Param_Name       : Util.Beans.Objects.Object;\n   Param_Value      : Util.Beans.Objects.Object;\n   Mime_Type        : Util.Beans.Objects.Object;\n   Extension        : Util.Beans.Objects.Object;\n   Error_Code       : Util.Beans.Objects.Object;\n   Location         : Util.Beans.Objects.Object;\n   Handler          : Servlet_Registry_Access;\n   Context          : EL.Contexts.ELContext_Access;\n   Override_Context : Boolean := True;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Servlet_Config_Access",
       qualified_name: "Servlet.Core.Mappers.Servlet_Config_Access",
       signature: "servlet.core.mappers.servlet_config_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Servlet_Config_Access is access all Servlet_Config;",
       }   ,
   ]
,}
---

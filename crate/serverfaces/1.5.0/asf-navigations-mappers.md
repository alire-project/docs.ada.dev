---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Navigations.Mappers",
qualified_name: "ASF.Navigations.Mappers",
signature: "asf.navigations.mappers",
enclosing: "asf.navigations",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-navigations-mappers -- Read XML navigation files\n  Copyright (C) 2010, 2011, 2017, 2018 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Reader_Config",
       qualified_name: "ASF.Navigations.Mappers.Reader_Config",
       signature: "asf.navigations.mappers.reader_config",
       enclosing: "asf.navigations.mappers",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Config",
              qualified_name: "ASF.Navigations.Mappers.Reader_Config.Config",
              signature: "asf.navigations.mappers.reader_config.config",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Config : aliased Nav_Config;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Navigation_Case_Fields",
       qualified_name: "ASF.Navigations.Mappers.Navigation_Case_Fields",
       signature: "asf.navigations.mappers.navigation_case_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Navigation_Case_Fields is (FROM_VIEW_ID, OUTCOME, ACTION, TO_VIEW, REDIRECT, CONDITION,\n                                CONTENT, CONTENT_TYPE, NAVIGATION_CASE, NAVIGATION_RULE,\n                                STATUS);",
       }   ,
   ]
,record_types:    [
       {
       name: "Nav_Config",
       qualified_name: "ASF.Navigations.Mappers.Nav_Config",
       signature: "asf.navigations.mappers.nav_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Nav_Config is limited record\n   Outcome      : Util.Beans.Objects.Object;\n   Action       : Util.Beans.Objects.Object;\n   To_View      : Util.Beans.Objects.Object;\n   From_View    : Util.Beans.Objects.Object;\n   Redirect     : Boolean := False;\n   Condition    : Util.Beans.Objects.Object;\n   Content      : Util.Beans.Objects.Object;\n   Content_Type : Util.Beans.Objects.Object;\n   Status       : Natural := 0;\n   Context      : EL.Contexts.ELContext_Access;\n   Handler      : Navigation_Handler_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Nav_Config_Access",
       qualified_name: "ASF.Navigations.Mappers.Nav_Config_Access",
       signature: "asf.navigations.mappers.nav_config_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Nav_Config_Access is access all Nav_Config;",
       }   ,
   ]
,}
---

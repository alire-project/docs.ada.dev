---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Beans.Mappers",
qualified_name: "ASF.Beans.Mappers",
signature: "asf.beans.mappers",
enclosing: "asf.beans",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-beans-mappers -- Read XML managed bean declarations\n  Copyright (C) 2010, 2011, 2017 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Reader_Config",
       qualified_name: "ASF.Beans.Mappers.Reader_Config",
       signature: "asf.beans.mappers.reader_config",
       enclosing: "asf.beans.mappers",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Config",
              qualified_name: "ASF.Beans.Mappers.Reader_Config.Config",
              signature: "asf.beans.mappers.reader_config.config",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Config : aliased Managed_Bean;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Managed_Bean_Fields",
       qualified_name: "ASF.Beans.Mappers.Managed_Bean_Fields",
       signature: "asf.beans.mappers.managed_bean_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Managed_Bean_Fields is (FIELD_NAME,\n                             FIELD_CLASS,\n                             FIELD_SCOPE,\n                             FIELD_MANAGED_BEAN,\n                             FIELD_PROPERTY,\n                             FIELD_PROPERTY_NAME,\n                             FIELD_PROPERTY_VALUE,\n                             FIELD_PROPERTY_CLASS);",
       }   ,
   ]
,record_types:    [
       {
       name: "Managed_Bean",
       qualified_name: "ASF.Beans.Mappers.Managed_Bean",
       signature: "asf.beans.mappers.managed_bean",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Managed_Bean is limited record\n   Name         : Util.Beans.Objects.Object;\n   Class        : Util.Beans.Objects.Object;\n   Scope        : Scope_Type := REQUEST_SCOPE;\n   Factory      : Bean_Factory_Access  := null;\n   Params       : ASF.Beans.Parameter_Bean_Ref.Ref;\n   Prop_Name    : Util.Beans.Objects.Object;\n   Prop_Value   : Util.Beans.Objects.Object;\n   Context      : EL.Contexts.ELContext_Access := null;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Bean_Factory_Access",
       qualified_name: "ASF.Beans.Mappers.Bean_Factory_Access",
       signature: "asf.beans.mappers.bean_factory_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bean_Factory_Access is access all ASF.Beans.Bean_Factory;",
       }   ,
       {
       name: "Managed_Bean_Access",
       qualified_name: "ASF.Beans.Mappers.Managed_Bean_Access",
       signature: "asf.beans.mappers.managed_bean_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Managed_Bean_Access is access all Managed_Bean;",
       }   ,
   ]
,}
---

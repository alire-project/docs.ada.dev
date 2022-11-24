---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Applications.Main.Configs",
qualified_name: "ASF.Applications.Main.Configs",
signature: "asf.applications.main.configs",
enclosing: "asf.applications.main",
is_private: false,
documentation: "Read the configuration file associated with the application.  This includes:\n<ul>\n   <li>The servlet and filter mappings</li>\n   <li>The managed bean definitions</li>\n   <li>The navigation rules</li>\n</ul>",
documentation_snippet: "",
packages:    [
       {
       name: "Parameter",
       qualified_name: "ASF.Applications.Main.Configs.Parameter",
       signature: "asf.applications.main.configs.parameter",
       enclosing: "asf.applications.main.configs",
       is_private: false,
       documentation: "Returns the configuration parameter.\n\n@formal Name\n  The default value.\n@formal Default",
       documentation_snippet: "",
       }   ,
       {
       name: "Reader_Config",
       qualified_name: "ASF.Applications.Main.Configs.Reader_Config",
       signature: "asf.applications.main.configs.reader_config",
       enclosing: "asf.applications.main.configs",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Prop_Context",
              qualified_name: "ASF.Applications.Main.Configs.Reader_Config.Prop_Context",
              signature: "asf.applications.main.configs.reader_config.prop_context",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Prop_Context : aliased EL.Contexts.Properties.Property_Resolver;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Application_Fields",
       qualified_name: "ASF.Applications.Main.Configs.Application_Fields",
       signature: "asf.applications.main.configs.application_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Fields is (TAG_MESSAGE_BUNDLE, TAG_MESSAGE_VAR,\n                            TAG_DEFAULT_LOCALE, TAG_SUPPORTED_LOCALE);",
       }   ,
   ]
,record_types:    [
       {
       name: "Application_Config",
       qualified_name: "ASF.Applications.Main.Configs.Application_Config",
       signature: "asf.applications.main.configs.application_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Config is limited record\n   Name    : Util.Beans.Objects.Object;\n   App     : ASF.Contexts.Faces.Application_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Application_Config_Access",
       qualified_name: "ASF.Applications.Main.Configs.Application_Config_Access",
       signature: "asf.applications.main.configs.application_config_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Application_Config_Access is access all Application_Config;",
       }   ,
   ]
,}
---

---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Applications.Views",
qualified_name: "ASF.Applications.Views",
signature: "asf.applications.views",
enclosing: "asf.applications",
is_private: false,
documentation: "---------------------------------------------------------------------\n  applications.views -- Ada Web Application\n  Copyright (C) 2009, 2010, 2011, 2012, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "View_Handler",
       qualified_name: "ASF.Applications.Views.View_Handler",
       signature: "asf.applications.views.view_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Handler is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Local_Array_Access",
       qualified_name: "ASF.Applications.Views.Local_Array_Access",
       signature: "asf.applications.views.local_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Local_Array_Access is access Util.Locales.Locale_Array;",
       }   ,
       {
       name: "View_Handler_Access",
       qualified_name: "ASF.Applications.Views.View_Handler_Access",
       signature: "asf.applications.views.view_handler_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Handler_Access is access all View_Handler'Class;",
       }   ,
   ]
,}
---

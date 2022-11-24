---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Lifecycles",
qualified_name: "ASF.Lifecycles",
signature: "asf.lifecycles",
enclosing: "asf",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-lifecycles -- Lifecycle\n  Copyright (C) 2010, 2011, 2012, 2018, 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Phase_Controller_Array",
       qualified_name: "ASF.Lifecycles.Phase_Controller_Array",
       signature: "asf.lifecycles.phase_controller_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Controller_Array is array (Phase_Type) of Phase_Controller_Access;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Lifecycle",
       qualified_name: "ASF.Lifecycles.Lifecycle",
       signature: "asf.lifecycles.lifecycle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lifecycle is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Phase_Controller",
       qualified_name: "ASF.Lifecycles.Phase_Controller",
       signature: "asf.lifecycles.phase_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Controller is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Lifecycle_Access",
       qualified_name: "ASF.Lifecycles.Lifecycle_Access",
       signature: "asf.lifecycles.lifecycle_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lifecycle_Access is access all Lifecycle'Class;",
       }   ,
       {
       name: "Phase_Controller_Access",
       qualified_name: "ASF.Lifecycles.Phase_Controller_Access",
       signature: "asf.lifecycles.phase_controller_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phase_Controller_Access is access all Phase_Controller'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Phase_Type",
       qualified_name: "ASF.Lifecycles.Phase_Type",
       signature: "asf.lifecycles.phase_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Phase_Type is\n  Events.Phases.Phase_Type range Events.Phases.RESTORE_VIEW .. Events.Phases.RENDER_RESPONSE;",
       }   ,
   ]
,}
---

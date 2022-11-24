---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Protected_Datastore",
qualified_name: "Agpl.Protected_Datastore",
signature: "agpl.protected_datastore",
enclosing: "agpl",
is_private: false,
documentation: "A collection of protected data with notifiers",
documentation_snippet: "",
record_types:    [
       {
       name: "Functor",
       qualified_name: "Agpl.Protected_Datastore.Functor",
       signature: "agpl.protected_datastore.functor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Functor is abstract tagged null record;",
       }   ,
       {
       name: "Key_Listener",
       qualified_name: "Agpl.Protected_Datastore.Key_Listener",
       signature: "agpl.protected_datastore.key_listener",
       enclosing: "",
       is_private: false,
       documentation: "Something that wants to be notified when a key is stored",
       documentation_snippet: "type Key_Listener is abstract tagged limited null record;",
       }   ,
       {
       name: "Object_Data",
       qualified_name: "Agpl.Protected_Datastore.Object_Data",
       signature: "agpl.protected_datastore.object_data",
       enclosing: "",
       is_private: false,
       documentation: "This is data to be kept in the datastore",
       documentation_snippet: "type Object_Data is abstract tagged null record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Data_Handle",
       qualified_name: "Agpl.Protected_Datastore.Data_Handle",
       signature: "agpl.protected_datastore.data_handle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Handle is new Object_Data_Handles.Object with null record;",
       }   ,
       {
       name: "Object",
       qualified_name: "Agpl.Protected_Datastore.Object",
       signature: "agpl.protected_datastore.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Key_Listener_Access",
       qualified_name: "Agpl.Protected_Datastore.Key_Listener_Access",
       signature: "agpl.protected_datastore.key_listener_access",
       enclosing: "",
       is_private: false,
       documentation: "Processing here should be as fast as possible, since all chained calls\nare synchronous.\nCare is to be taken to not cause recursive calling!! This is up to the\nclients.",
       documentation_snippet: "type Key_Listener_Access is access all Key_Listener'Class;",
       }   ,
       {
       name: "Object_Access",
       qualified_name: "Agpl.Protected_Datastore.Object_Access",
       signature: "agpl.protected_datastore.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Access is access Object'Class;",
       }   ,
       {
       name: "Object_Data_Access",
       qualified_name: "Agpl.Protected_Datastore.Object_Data_Access",
       signature: "agpl.protected_datastore.object_data_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Data_Access is access all Object_Data'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Object_Key",
       qualified_name: "Agpl.Protected_Datastore.Object_Key",
       signature: "agpl.protected_datastore.object_key",
       enclosing: "",
       is_private: false,
       documentation: "This is the indexing type",
       documentation_snippet: "subtype Object_Key is String;",
       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Protected_Datastore.Log_Section",
       signature: "agpl.protected_datastore.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.protected_datastore\";",
       }   ,
   ]
,}
---

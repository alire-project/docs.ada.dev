---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Client.Storage",
qualified_name: "Gnoga.Client.Storage",
signature: "gnoga.client.storage",
enclosing: "gnoga.client",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Storage_Type\n-----------------------------------------------------------------------\n  Base class for client side storage of data.\n  In order to ease access to client side data, the Storage_Type can be\n  accessed using any object instead of just through the parent window.\n  One local and one session storage is available across an entire\n  location defined as scheme://domain:port.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Local_Storage_Type",
       qualified_name: "Gnoga.Client.Storage.Local_Storage_Type",
       signature: "gnoga.client.storage.local_storage_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Local_Storage_Type is new Storage_Type with private;",
       }   ,
       {
       name: "Session_Storage_Type",
       qualified_name: "Gnoga.Client.Storage.Session_Storage_Type",
       signature: "gnoga.client.storage.session_storage_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Storage_Type is new Storage_Type with private;",
       }   ,
       {
       name: "Storage_Type",
       qualified_name: "Gnoga.Client.Storage.Storage_Type",
       signature: "gnoga.client.storage.storage_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Type is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Local_Storage_Access",
       qualified_name: "Gnoga.Client.Storage.Local_Storage_Access",
       signature: "gnoga.client.storage.local_storage_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Local_Storage_Access is access all Local_Storage_Type;",
       }   ,
       {
       name: "Pointer_To_Local_Storage_Class",
       qualified_name: "Gnoga.Client.Storage.Pointer_To_Local_Storage_Class",
       signature: "gnoga.client.storage.pointer_to_local_storage_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Local_Storage_Class is access all Local_Storage_Type'Class;",
       }   ,
       {
       name: "Pointer_To_Session_Storage_Class",
       qualified_name: "Gnoga.Client.Storage.Pointer_To_Session_Storage_Class",
       signature: "gnoga.client.storage.pointer_to_session_storage_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Session_Storage_Class is access all Session_Storage_Type'Class;",
       }   ,
       {
       name: "Pointer_To_Storage_Class",
       qualified_name: "Gnoga.Client.Storage.Pointer_To_Storage_Class",
       signature: "gnoga.client.storage.pointer_to_storage_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Storage_Class is access all Storage_Type'Class;",
       }   ,
       {
       name: "Session_Storage_Access",
       qualified_name: "Gnoga.Client.Storage.Session_Storage_Access",
       signature: "gnoga.client.storage.session_storage_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Storage_Access is access all Session_Storage_Type;",
       }   ,
       {
       name: "Storage_Access",
       qualified_name: "Gnoga.Client.Storage.Storage_Access",
       signature: "gnoga.client.storage.storage_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Access is access all Storage_Type;",
       }   ,
   ]
,}
---

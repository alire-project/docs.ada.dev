---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Sessions",
qualified_name: "ADO.Sessions",
signature: "ado.sessions",
enclosing: "ado",
is_private: false,
documentation: "Raised if the database connection is not open.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Connection_Status",
       qualified_name: "ADO.Sessions.Connection_Status",
       signature: "ado.sessions.connection_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connection_Status is (OPEN, CLOSED);",
       }   ,
       {
       name: "Session_Record",
       qualified_name: "ADO.Sessions.Session_Record",
       signature: "ado.sessions.session_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Record is limited private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Master_Session",
       qualified_name: "ADO.Sessions.Master_Session",
       signature: "ado.sessions.master_session",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Master_Session is new Session with private;",
       }   ,
       {
       name: "Object_Factory",
       qualified_name: "ADO.Sessions.Object_Factory",
       signature: "ado.sessions.object_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Factory is tagged private;",
       }   ,
       {
       name: "Session",
       qualified_name: "ADO.Sessions.Session",
       signature: "ado.sessions.session",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Session_Record_Access",
       qualified_name: "ADO.Sessions.Session_Record_Access",
       signature: "ado.sessions.session_record_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Record_Access is access all Session_Record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Database_Connection",
       qualified_name: "ADO.Sessions.Database_Connection",
       signature: "ado.sessions.database_connection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Database_Connection is Connections.Database_Connection;",
       }   ,
   ]
,}
---

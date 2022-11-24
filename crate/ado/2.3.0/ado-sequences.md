---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Sequences",
qualified_name: "ADO.Sequences",
signature: "ado.sequences",
enclosing: "ado",
is_private: false,
documentation: "Exception raised when the sequence generator fails to allocate an id.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Factory",
       qualified_name: "ADO.Sequences.Factory",
       signature: "ado.sequences.factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory is limited private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Generator",
       qualified_name: "ADO.Sequences.Generator",
       signature: "ado.sequences.generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Factory_Access",
       qualified_name: "ADO.Sequences.Factory_Access",
       signature: "ado.sequences.factory_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Factory_Access is access all Factory;",
       }   ,
       {
       name: "Generator_Access",
       qualified_name: "ADO.Sequences.Generator_Access",
       signature: "ado.sequences.generator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator_Access is access all Generator'Class;",
       }   ,
       {
       name: "Generator_Factory",
       qualified_name: "ADO.Sequences.Generator_Factory",
       signature: "ado.sequences.generator_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator_Factory is access\n  function (Sess_Factory : in Session_Factory_Access)\n            return Generator_Access;",
       }   ,
       {
       name: "Session_Factory_Access",
       qualified_name: "ADO.Sequences.Session_Factory_Access",
       signature: "ado.sequences.session_factory_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Session_Factory_Access is access all ADO.Sessions.Factory.Session_Factory'Class;",
       }   ,
   ]
,}
---

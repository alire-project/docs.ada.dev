---
crate: uri_mime
layout: gnatdoc
gnatdoc: {
name: "URI",
qualified_name: "URI",
signature: "uri",
enclosing: "",
is_private: false,
documentation: "TCP Port Number",
documentation_snippet: "",
simple_types:    [
       {
       name: "Port_Number",
       qualified_name: "URI.Port_Number",
       signature: "uri.port_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Port_Number is range 0 .. 65535;",
       }   ,
   ]
,record_types:    [
       {
       name: "URL",
       qualified_name: "URI.URL",
       signature: "uri.url",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "        type URL is record\n		Scheme_Present : Boolean := False;\n		Scheme : Unbounded_String;\n		Authority_Present : Boolean := False;\n		User_Info_Present : Boolean := False;\n		User_Info : Unbounded_String;\n		Host : Unbounded_String;\n		Port_Present : Boolean := False;\n		Port : Port_Number := 0;\n		Path : Unbounded_String;\n		Query_Present : Boolean := False;\n		Query : Unbounded_String;\n		Fragment_Present : Boolean := False;\n		Fragment : Unbounded_String;\n	end record;",
       }   ,
   ]
,}
---

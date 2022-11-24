---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Server",
qualified_name: "Servlet.Server",
signature: "servlet.server",
enclosing: "servlet",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Configuration",
       qualified_name: "Servlet.Server.Configuration",
       signature: "servlet.server.configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Configuration is record\n   Listening_Port        : Port_Number := 8080;\n   Max_Connection        : Positive := 5;\n   Buffer_Size           : Positive := 128 * 1024;\n   Accept_Queue_Size     : Positive := 63;\n   Upload_Size_Limit     : Positive := 16#500_000#;\n   Input_Line_Size_Limit : Positive := 16#4000#;\n   Reuse_Address         : Boolean := True;\n   TCP_No_Delay          : Boolean := False;\n   Upload_Directory      : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Container",
       qualified_name: "Servlet.Server.Container",
       signature: "servlet.server.container",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Container is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Port_Number",
       qualified_name: "Servlet.Server.Port_Number",
       signature: "servlet.server.port_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Port_Number is Natural range 0 .. 65535;",
       }   ,
   ]
,}
---

---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Debug",
qualified_name: "GL.Debug",
signature: "gl.debug",
enclosing: "gl",
is_private: false,
documentation: "part of OpenGLAda, (c) 2021 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Message_Severity_Restriction",
       qualified_name: "GL.Debug.Message_Severity_Restriction",
       signature: "gl.debug.message_severity_restriction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Message_Severity_Restriction is\n  (Dont_Care, Notification, High, Medium, Low);",
       }   ,
       {
       name: "Message_Source_Restriction",
       qualified_name: "GL.Debug.Message_Source_Restriction",
       signature: "gl.debug.message_source_restriction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Message_Source_Restriction is\n  (Dont_Care, Api, Window_System, Shader_Compiler, Third_Party, Application,\n   Other);",
       }   ,
       {
       name: "Message_Type_Restriction",
       qualified_name: "GL.Debug.Message_Type_Restriction",
       signature: "gl.debug.message_type_restriction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Message_Type_Restriction is\n  (Dont_Care, Error, Deprecated_Behavior, Undefined_Behavior, Portability,\n   Performance, Other, Marker, Push_Group, Pop_Group);",
       }   ,
   ]
,interface_types:    [
       {
       name: "Message_Receiver",
       qualified_name: "GL.Debug.Message_Receiver",
       signature: "gl.debug.message_receiver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Message_Receiver is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Stream_Logger",
       qualified_name: "GL.Debug.Stream_Logger",
       signature: "gl.debug.stream_logger",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Logger is new Message_Receiver with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Message_Severity",
       qualified_name: "GL.Debug.Message_Severity",
       signature: "gl.debug.message_severity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Message_Severity is Message_Severity_Restriction\n  range Notification .. Low;",
       }   ,
       {
       name: "Message_Source",
       qualified_name: "GL.Debug.Message_Source",
       signature: "gl.debug.message_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Message_Source is Message_Source_Restriction range Api .. Other;",
       }   ,
       {
       name: "Message_Type",
       qualified_name: "GL.Debug.Message_Type",
       signature: "gl.debug.message_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Message_Type is Message_Type_Restriction range Error .. Pop_Group;",
       }   ,
   ]
,}
---

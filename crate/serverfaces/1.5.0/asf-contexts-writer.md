---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Contexts.Writer",
qualified_name: "ASF.Contexts.Writer",
signature: "asf.contexts.writer",
enclosing: "asf.contexts",
is_private: false,
documentation: "------------------------------\nIO Writer\n------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "IOWriter",
       qualified_name: "ASF.Contexts.Writer.IOWriter",
       signature: "asf.contexts.writer.iowriter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IOWriter is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Response_Writer",
       qualified_name: "ASF.Contexts.Writer.Response_Writer",
       signature: "asf.contexts.writer.response_writer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Response_Writer is new ASF.Streams.Print_Stream with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Response_Writer_Access",
       qualified_name: "ASF.Contexts.Writer.Response_Writer_Access",
       signature: "asf.contexts.writer.response_writer_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Response_Writer_Access is access all Response_Writer'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ResponseWriter",
       qualified_name: "ASF.Contexts.Writer.ResponseWriter",
       signature: "asf.contexts.writer.responsewriter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ResponseWriter is Response_Writer;",
       }   ,
       {
       name: "ResponseWriter_Access",
       qualified_name: "ASF.Contexts.Writer.ResponseWriter_Access",
       signature: "asf.contexts.writer.responsewriter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ResponseWriter_Access is Response_Writer_Access;",
       }   ,
   ]
,}
---

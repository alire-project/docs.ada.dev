---
crate: uri_mime
layout: gnatdoc
gnatdoc: {
name: "MIME",
qualified_name: "MIME",
signature: "mime",
enclosing: "",
is_private: false,
documentation: "A single parameter in a MIME type, separated from the base type with \";\"",
documentation_snippet: "",
record_types:    [
       {
       name: "MIME_Type",
       qualified_name: "MIME.MIME_Type",
       signature: "mime.mime_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@field General\n  \"image\"\n@field Specific\n  \"svg\"\n@field Suffix\n  \"xml\"\n@field Parameters",
       documentation_snippet: "        type MIME_Type is record\n		General : Unbounded_String; -- \"image\n		Specific : Unbounded_String; -- \"svg\n		Suffix : Unbounded_String; -- \"xml\n		-- Parameters\n		-- Parameters\n		Parameters : Vector;\n	end record;",
       }   ,
       {
       name: "Parameter",
       qualified_name: "MIME.Parameter",
       signature: "mime.parameter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "        type Parameter is record\n		Name : Unbounded_String;\n		Value : Unbounded_String;\n	end record;",
       }   ,
   ]
,}
---

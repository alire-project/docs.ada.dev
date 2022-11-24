---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Template_Parser",
qualified_name: "Gnoga.Server.Template_Parser",
signature: "gnoga.server.template_parser",
enclosing: "gnoga.server",
is_private: false,
documentation: "Gnoga.Server.Template_Parser uses PHP, Python or Ada as template parsing\nengines. It also makes it possible to leverage and reuse existing\nweb resources until they can be ported to Gnoga. To use Python instead\nof PHP see Gnoga.Server.Template_Parser.Python. If only simple parsing\nis needed (find and replace), use Gnoga.Server.Template_Parse.Simple\nthat uses Ada.Text_IO\n\nNote: Template_Parser is not intended to be used for web site / app\n      development but for tools or for use by apps to manipulate files.\n      That doesn't mean you couldn't develop an entire site using it\n      and production sites have been made with it. Keep in mind though\n      that the security advantages of Gnoga are reduced if you are using\n      a CGI like approach using a template_parser based on PHP or\n      Python.",
documentation_snippet: "",
array_types:    [
       {
       name: "View_Data_Array",
       qualified_name: "Gnoga.Server.Template_Parser.View_Data_Array",
       signature: "gnoga.server.template_parser.view_data_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Data_Array is array (Positive range <>) of View_Data;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "View_Data",
       qualified_name: "Gnoga.Server.Template_Parser.View_Data",
       signature: "gnoga.server.template_parser.view_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Data is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,}
---

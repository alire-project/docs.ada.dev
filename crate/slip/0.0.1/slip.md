---
crate: slip
layout: gnatdoc
gnatdoc: {
name: "slip",
qualified_name: "slip",
signature: "slip",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "t_slip",
       qualified_name: "slip.t_slip",
       signature: "slip.t_slip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_slip is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "t_buffer",
       qualified_name: "slip.t_buffer",
       signature: "slip.t_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_buffer is array (Natural range <>) of Unsigned_8;",
       }   ,
   ]
,record_types:    [
       {
       name: "t_decode_result",
       qualified_name: "slip.t_decode_result",
       signature: "slip.t_decode_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_decode_result\n  (\n   has_byte : Boolean := False\n  )\nis\n   record\n      case has_byte is\n         when True =>\n            byte: Unsigned_8;\n         when False =>\n            null;\n      end case;\n   end record;",
       }   ,
   ]
,}
---

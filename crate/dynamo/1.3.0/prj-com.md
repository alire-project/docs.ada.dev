---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Com",
qualified_name: "Prj.Com",
signature: "prj.com",
enclosing: "prj",
is_private: false,
documentation: "The following package declares a Fail procedure that is used in the\nProject Manager.",
documentation_snippet: "",
access_types:    [
       {
       name: "Fail_Proc",
       qualified_name: "Prj.Com.Fail_Proc",
       signature: "prj.com.fail_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fail_Proc is access procedure (S : String);",
       }   ,
   ]
,variables:    [
       {
       name: "Fail",
       qualified_name: "Prj.Com.Fail",
       signature: "prj.com.fail",
       enclosing: "",
       is_private: false,
       documentation: "This procedure is used in the project facility, instead of directly\ncalling Osint.Fail. It may be specified by tools to do clean up before\ncalling Osint.Fail, or to simply report an error and return.",
       documentation_snippet: "Fail : Fail_Proc := Osint.Fail'Access;",
       }   ,
   ]
,}
---

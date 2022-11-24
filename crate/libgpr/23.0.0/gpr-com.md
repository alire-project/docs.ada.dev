---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Com",
qualified_name: "GPR.Com",
signature: "gpr.com",
enclosing: "gpr",
is_private: false,
documentation: "The following package declares a Fail procedure that is used in the\nProject Manager.",
documentation_snippet: "",
access_types:    [
       {
       name: "Fail_Proc",
       qualified_name: "GPR.Com.Fail_Proc",
       signature: "gpr.com.fail_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fail_Proc is access procedure (S : String);",
       }   ,
   ]
,variables:    [
       {
       name: "Fail",
       qualified_name: "GPR.Com.Fail",
       signature: "gpr.com.fail",
       enclosing: "",
       is_private: false,
       documentation: "This procedure is used in the project facility, instead of directly\ncalling Project.Osint.Fail. It may be specified by tools to do clean\nup before calling Project.Osint.Fail, or to simply report an error and\nreturn.",
       documentation_snippet: "Fail : Fail_Proc := GPR.Osint.Fail'Access;",
       }   ,
   ]
,}
---

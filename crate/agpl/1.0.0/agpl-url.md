---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.URL",
qualified_name: "Agpl.URL",
signature: "agpl.url",
enclosing: "agpl",
is_private: false,
documentation: "The general URL form as described in RFC2616 is:\n\nhttp_URL = \"http:\" \"//\" host [ \":\" port ] [ abs_path [ \"?\" query ]]\n\nNote also that there are different RFC describing URL like the 2616 and\n1738 but they use different terminologies. Here we try to follow the\nnames used in RFC2616 but we have implemented some extensions at the\nend of this package. For example the way Path and File are separated or\nthe handling of user/password which is explicitly not allowed in the\nRFC but are used and supported in many browsers. Here are the extended\nURL supported:\n\nhttp://username:password@www.here.com:80/dir1/dir2/xyz.html?p=8&x=doh\n |                            |       | |          |       |\n protocol                     host port path       file    parameters\n\n                                        <--  pathname  -->",
documentation_snippet: "",
constants:    [
       {
       name: "Default_Encoding_Set",
       qualified_name: "Agpl.URL.Default_Encoding_Set",
       signature: "agpl.url.default_encoding_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Encoding_Set   : constant Strings.Maps.Character_Set;",
       }   ,
       {
       name: "Requiring_Encoding_Set",
       qualified_name: "Agpl.URL.Requiring_Encoding_Set",
       signature: "agpl.url.requiring_encoding_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Requiring_Encoding_Set : constant Strings.Maps.Character_Set;",
       }   ,
   ]
,}
---

---
crate: gnatdist_garlic
layout: gnatdoc
gnatdoc: {
name: "XE_Scan",
qualified_name: "XE_Scan",
signature: "xe_scan",
enclosing: "",
is_private: false,
documentation: "This package provides routines to scan the configuration file.",
documentation_snippet: "",
record_types:    [
       {
       name: "Location_Type",
       qualified_name: "XE_Scan.Location_Type",
       signature: "xe_scan.location_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Location_Type is\n   record\n      Line  : XE_Types.Int;\n      First : XE_Types.Text_Ptr;\n      Last  : XE_Types.Text_Ptr;\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Location",
       qualified_name: "XE_Scan.Null_Location",
       signature: "xe_scan.null_location",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Location  : constant Location_Type := (0, 0, 0);",
       }   ,
   ]
,variables:    [
       {
       name: "Token",
       qualified_name: "XE_Scan.Token",
       signature: "xe_scan.token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Token      : Token_Type;",
       }   ,
       {
       name: "Token_Name",
       qualified_name: "XE_Scan.Token_Name",
       signature: "xe_scan.token_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Token_Name : XE_Types.Name_Id;",
       }   ,
   ]
,}
---

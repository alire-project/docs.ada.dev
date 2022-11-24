---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Network.IpAddress",
qualified_name: "Sf.Network.IpAddress",
signature: "sf.network.ipaddress",
enclosing: "sf.network",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
array_types:    [
       {
       name: "sfAddress_Array",
       qualified_name: "Sf.Network.IpAddress.sfAddress_Array",
       signature: "sf.network.ipaddress.sfaddress_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfAddress_Array is array (0 .. 15) of aliased sfInt8;",
       }   ,
   ]
,record_types:    [
       {
       name: "sfIpAddress",
       qualified_name: "Sf.Network.IpAddress.sfIpAddress",
       signature: "sf.network.ipaddress.sfipaddress",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfIpAddress is record\n   address : sfAddress_Array;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Any",
       qualified_name: "Sf.Network.IpAddress.Any",
       signature: "sf.network.ipaddress.any",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Any : aliased constant sfIpAddress;",
       }   ,
       {
       name: "Broadcast",
       qualified_name: "Sf.Network.IpAddress.Broadcast",
       signature: "sf.network.ipaddress.broadcast",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Broadcast : aliased constant sfIpAddress;",
       }   ,
       {
       name: "LocalHost",
       qualified_name: "Sf.Network.IpAddress.LocalHost",
       signature: "sf.network.ipaddress.localhost",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "LocalHost : aliased constant sfIpAddress;",
       }   ,
       {
       name: "None",
       qualified_name: "Sf.Network.IpAddress.None",
       signature: "sf.network.ipaddress.none",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "None : aliased constant sfIpAddress;",
       }   ,
   ]
,}
---

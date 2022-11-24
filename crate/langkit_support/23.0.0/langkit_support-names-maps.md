---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Names.Maps",
qualified_name: "Langkit_Support.Names.Maps",
signature: "langkit_support.names.maps",
enclosing: "langkit_support.names",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0\n\n@formal Element_Type",
documentation_snippet: "",
record_types:    [
       {
       name: "Lookup_Result",
       qualified_name: "Langkit_Support.Names.Maps.Lookup_Result",
       signature: "langkit_support.names.maps.lookup_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lookup_Result (Present : Boolean := False) is record\n   case Present is\n      when False => null;\n      when True  => Element : Element_Type;\n   end case;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Map",
       qualified_name: "Langkit_Support.Names.Maps.Map",
       signature: "langkit_support.names.maps.map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Map (Casing : Casing_Convention := Camel_With_Underscores)\nis tagged limited private;",
       }   ,
   ]
,constants:    [
       {
       name: "Absent_Lookup_Result",
       qualified_name: "Langkit_Support.Names.Maps.Absent_Lookup_Result",
       signature: "langkit_support.names.maps.absent_lookup_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Absent_Lookup_Result : constant Lookup_Result := (Present => False);",
       }   ,
   ]
,}
---

---
crate: xml_ez_out
layout: gnatdoc
gnatdoc: {
name: "McKae.XML.EZ_Out.Generic_Medium",
qualified_name: "McKae.XML.EZ_Out.Generic_Medium",
signature: "mckae.xml.ez_out.generic_medium",
enclosing: "mckae.xml.ez_out",
is_private: false,
documentation: "-----------------------------------------------------------------\n This package provides the means to easily write XML elements and\n  associated attributes to a provided medium that provides the\n  required interface.\n\n@formal Output_Medium\n@formal Put\n@formal New_Line\n   DEPRECATED\n   Control formatting by setting the Current_Format variable in the\n   package spec.\n  \n   Specify whether the XML that is created is to have indenting and\n   line breaks.\n@formal Format\n  DEPRECATED\n  The maximum element nesting depth of an XML document\n@formal Max_Element_Nesting",
documentation_snippet: "",
simple_types:    [
       {
       name: "Attribute_Value_Pairs",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.Attribute_Value_Pairs",
       signature: "mckae.xml.ez_out.generic_medium.attribute_value_pairs",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attribute_Value_Pairs is private;",
       }   ,
       {
       name: "Standalone_Values",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.Standalone_Values",
       signature: "mckae.xml.ez_out.generic_medium.standalone_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Standalone_Values is (Yes, No, Omit);",
       }   ,
   ]
,array_types:    [
       {
       name: "Attributes_List",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.Attributes_List",
       signature: "mckae.xml.ez_out.generic_medium.attributes_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attributes_List is array(Natural range <>) of Attribute_Value_Pairs;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Attributes",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.No_Attributes",
       signature: "mckae.xml.ez_out.generic_medium.no_attributes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Attributes : constant Attributes_List;",
       }   ,
   ]
,variables:    [
       {
       name: "Current_Format",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.Current_Format",
       signature: "mckae.xml.ez_out.generic_medium.current_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Current_Format   : Formatting_Options := Format;",
       }   ,
       {
       name: "Default_Output_Null_Attributes",
       qualified_name: "McKae.XML.EZ_Out.Generic_Medium.Default_Output_Null_Attributes",
       signature: "mckae.xml.ez_out.generic_medium.default_output_null_attributes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Output_Null_Attributes : Boolean := False;",
       }   ,
   ]
,}
---

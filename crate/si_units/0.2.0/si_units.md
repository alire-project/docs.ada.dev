---
crate: si_units
layout: gnatdoc
gnatdoc: {
name: "SI_Units",
qualified_name: "SI_Units",
signature: "si_units",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
subtypes:    [
       {
       name: "Unit_Name",
       qualified_name: "SI_Units.Unit_Name",
       signature: "si_units.unit_name",
       enclosing: "",
       is_private: false,
       documentation: "Restrict the possibility of a unit name: A unit name can be empty (see\nNo_Unit), but if it isn't, it shall not start with something weird like\ncontrol characters (which includes tabs), or whitespace.  It could start\nwith digits and other weird stuff, though.",
       documentation_snippet: "subtype Unit_Name is Ada.Strings.UTF_Encoding.UTF_8_String with\n  Dynamic_Predicate =>\n    (Unit_Name = No_Unit or else\n       (Unit_Name'Length > 0 and then\n          (for all C of Unit_Name (Unit_Name'First .. Unit_Name'First) =>\n             not Ada.Characters.Handling.Is_Control (C) and\n             not Ada.Characters.Handling.Is_Space (C))));",
       }   ,
   ]
,constants:    [
       {
       name: "No_Unit",
       qualified_name: "SI_Units.No_Unit",
       signature: "si_units.no_unit",
       enclosing: "",
       is_private: false,
       documentation: "Designated value for \"no unit name\", i.e. the empty string.\n\nNormally, when this package and its children are used, we would expect a\nnon-empty string for any unit (hence the type predicate below), but we\nallow the empty string as a special exception.",
       documentation_snippet: "No_Unit : constant Ada.Strings.UTF_Encoding.UTF_8_String;",
       }   ,
   ]
,}
---

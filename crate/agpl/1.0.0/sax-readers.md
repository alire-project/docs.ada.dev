---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Sax.Readers",
qualified_name: "Sax.Readers",
signature: "sax.readers",
enclosing: "sax",
is_private: false,
documentation: "---------------------------------------------------------------------\n                XML/Ada - An XML suite for Ada95                   --\n                                                                   --\n                       Copyright (C) 2001-2002                     --\n                            ACT-Europe                             --\n                                                                   --\n This library is free software; you can redistribute it and/or     --\n modify it under the terms of the GNU General Public               --\n License as published by the Free Software Foundation; either      --\n version 2 of the License, or (at your option) any later version.  --\n                                                                   --\n This library is distributed in the hope that it will be useful,   --\n but WITHOUT ANY WARRANTY; without even the implied warranty of    --\n MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU --\n General Public License for more details.                          --\n                                                                   --\n You should have received a copy of the GNU General Public         --\n License along with this library; if not, write to the             --\n Free Software Foundation, Inc., 59 Temple Place - Suite 330,      --\n Boston, MA 02111-1307, USA.                                       --\n                                                                   --\n As a special exception, if other files instantiate generics from  --\n this unit, or you link this unit with other files to produce an   --\n executable, this  unit  does not  by itself cause  the resulting  --\n executable to be covered by the GNU General Public License. This  --\n exception does not however invalidate any other reasons why the   --\n executable file  might be covered by the  GNU Public License.     --\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Reader",
       qualified_name: "Sax.Readers.Reader",
       signature: "sax.readers.reader",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reader is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "External_General_Entities_Feature",
       qualified_name: "Sax.Readers.External_General_Entities_Feature",
       signature: "sax.readers.external_general_entities_feature",
       enclosing: "",
       is_private: false,
       documentation: "If True, include all external general text entities.\nIf False, these are not included, and will be reported with\nContent_Handlers.Skipped_Entity.\n\nDefault is True",
       documentation_snippet: "External_General_Entities_Feature : constant String :=\n  \"http://xml.org/sax/features/external-general-entities\";",
       }   ,
       {
       name: "External_Parameter_Entities_Feature",
       qualified_name: "Sax.Readers.External_Parameter_Entities_Feature",
       signature: "sax.readers.external_parameter_entities_feature",
       enclosing: "",
       is_private: false,
       documentation: "If True, include all external parameter entities, including the\nexternal DTD subset. Parameter entities are the ones defined in DTDs\nand whose name starts with '%'",
       documentation_snippet: "External_Parameter_Entities_Feature : constant String :=\n  \"http://xml.org/sax/features/external-parameter-entities\";",
       }   ,
       {
       name: "Namespace_Feature",
       qualified_name: "Sax.Readers.Namespace_Feature",
       signature: "sax.readers.namespace_feature",
       enclosing: "",
       is_private: false,
       documentation: "Controls general namespace processing. If it is true (the default),\nnamespace URIs will be used in events.\nIn fact, this is only given for full compatibility with the SAX\nstandard. As authorized in the standard, this parser will always\nreport URIs to the Start_Element and End_Element callbacks.\n\nDefault is True.",
       documentation_snippet: "Namespace_Feature : constant String :=\n  \"http://www.xml.org/sax/features/namespace\";",
       }   ,
       {
       name: "Namespace_Prefixes_Feature",
       qualified_name: "Sax.Readers.Namespace_Prefixes_Feature",
       signature: "sax.readers.namespace_prefixes_feature",
       enclosing: "",
       is_private: false,
       documentation: "Controls the reporting of qNames and namespace attributes (xmlns*) to\nthe application.\nWhen this is False (the default), qNames may optionaly be reported,\nand namespace attributes must not be reported.",
       documentation_snippet: "Namespace_Prefixes_Feature : constant String :=\n  \"http://www.xml.org/sax/features/namespace-prefixes\";",
       }   ,
       {
       name: "Parameter_Entities_Feature",
       qualified_name: "Sax.Readers.Parameter_Entities_Feature",
       signature: "sax.readers.parameter_entities_feature",
       enclosing: "",
       is_private: false,
       documentation: "True if the SAX parser will reports parameter entities through its\nLexical_Handler.",
       documentation_snippet: "Parameter_Entities_Feature : constant String :=\n  \"http://xml.org/sax/features/lexical-handler/parameter-entities\";",
       }   ,
       {
       name: "Validation_Feature",
       qualified_name: "Sax.Readers.Validation_Feature",
       signature: "sax.readers.validation_feature",
       enclosing: "",
       is_private: false,
       documentation: "If True (not the default), a number of additional tests are performed\nwhile parsing the document, most notably that the document matches\nthe DTD (internal and external subset).",
       documentation_snippet: "Validation_Feature : constant String :=\n  \"http://www.xml.org/sax/features/validation\";",
       }   ,
   ]
,}
---

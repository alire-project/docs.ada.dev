---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Yaml",
qualified_name: "Yaml",
signature: "yaml",
enclosing: "",
is_private: false,
documentation: "occurs when the lexical analysis of a YAML character streams discovers\nill-formed input.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Collection_Style_Type",
       qualified_name: "Yaml.Collection_Style_Type",
       signature: "yaml.collection_style_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Collection_Style_Type is (Any, Block, Flow) with\n  Convention => C;",
       }   ,
       {
       name: "Event_Kind",
       qualified_name: "Yaml.Event_Kind",
       signature: "yaml.event_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event_Kind is (Stream_Start, Stream_End, Document_Start, Document_End,\n                    Alias, Scalar, Sequence_Start, Sequence_End,\n                    Mapping_Start, Mapping_End, Annotation_Start,\n                    Annotation_End);",
       }   ,
       {
       name: "Scalar_Style_Type",
       qualified_name: "Yaml.Scalar_Style_Type",
       signature: "yaml.scalar_style_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Scalar_Style_Type is\n  (Any, Plain, Single_Quoted, Double_Quoted, Literal, Folded) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Event",
       qualified_name: "Yaml.Event",
       signature: "yaml.event",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Kind\n  Start_Position is first character, End_Position is after last\n  character. this is necessary for zero-length events.\n@field Start_Position\n@field End_Position\n@field Version\n@field Implicit_Start\n@field Implicit_End\n@field Collection_Style\n@field Collection_Properties\n@field Annotation_Properties\n@field Namespace\n@field Name\n@field Scalar_Properties\n@field Content\n@field Scalar_Style\n@field Target",
       documentation_snippet: "type Event (Kind : Event_Kind := Stream_End) is record\n   Start_Position, End_Position : Mark;\n   case Kind is\n      when Document_Start =>\n         Version : Text.Reference;\n         Implicit_Start : Boolean := True;\n      when Document_End =>\n         Implicit_End : Boolean;\n      when Mapping_Start | Sequence_Start =>\n         Collection_Style : Collection_Style_Type := Any;\n         Collection_Properties : Properties;\n      when Annotation_Start =>\n         Annotation_Properties : Properties;\n         Namespace : Text.Reference;\n         Name : Text.Reference;\n      when Scalar =>\n         Scalar_Properties : Properties;\n         Content : Text.Reference;\n         Scalar_Style : Scalar_Style_Type := Any;\n      when Alias =>\n         Target : Text.Reference;\n      when Mapping_End | Sequence_End | Annotation_End | Stream_Start |\n           Stream_End => null;\n   end case;\nend record;",
       }   ,
       {
       name: "Mark",
       qualified_name: "Yaml.Mark",
       signature: "yaml.mark",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mark is record\n   Index, Line, Column : Mark_Position;\nend record;",
       }   ,
       {
       name: "Properties",
       qualified_name: "Yaml.Properties",
       signature: "yaml.properties",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Properties is record\n   Anchor, Tag : Text.Reference;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Refcount_Base",
       qualified_name: "Yaml.Refcount_Base",
       signature: "yaml.refcount_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Refcount_Base is abstract limited new\n  Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Flow_Scalar_Style_Type",
       qualified_name: "Yaml.Flow_Scalar_Style_Type",
       signature: "yaml.flow_scalar_style_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Flow_Scalar_Style_Type is Scalar_Style_Type range Literal .. Folded;",
       }   ,
       {
       name: "Mark_Position",
       qualified_name: "Yaml.Mark_Position",
       signature: "yaml.mark_position",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mark_Position is Positive;",
       }   ,
   ]
,constants:    [
       {
       name: "Standard_Annotation_Namespace",
       qualified_name: "Yaml.Standard_Annotation_Namespace",
       signature: "yaml.standard_annotation_namespace",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Standard_Annotation_Namespace : constant Text.Reference;",
       }   ,
   ]
,}
---

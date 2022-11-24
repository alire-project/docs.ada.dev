---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Element.Multimedia",
qualified_name: "Gnoga.Gui.Element.Multimedia",
signature: "gnoga.gui.element.multimedia",
enclosing: "gnoga.gui.element",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Multimedia_Types\n-----------------------------------------------------------------------\n  Base type for multimedia Elements",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Audio_Type",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Audio_Type",
       signature: "gnoga.gui.element.multimedia.audio_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Type is new Multimedia_Type with private;",
       }   ,
       {
       name: "Multimedia_Type",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Multimedia_Type",
       signature: "gnoga.gui.element.multimedia.multimedia_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Multimedia_Type is new Gnoga.Gui.Element.Element_Type with private;",
       }   ,
       {
       name: "Video_Type",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Video_Type",
       signature: "gnoga.gui.element.multimedia.video_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Video_Type is new Multimedia_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Audio_Access",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Audio_Access",
       signature: "gnoga.gui.element.multimedia.audio_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Access is access all Audio_Type;",
       }   ,
       {
       name: "Multimedia_Access",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Multimedia_Access",
       signature: "gnoga.gui.element.multimedia.multimedia_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Multimedia_Access is access all Multimedia_Type;",
       }   ,
       {
       name: "Pointer_To_Audio_Class",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Pointer_To_Audio_Class",
       signature: "gnoga.gui.element.multimedia.pointer_to_audio_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Audio_Class is access all Audio_Type'Class;",
       }   ,
       {
       name: "Pointer_To_Multimedia_Class",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Pointer_To_Multimedia_Class",
       signature: "gnoga.gui.element.multimedia.pointer_to_multimedia_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Multimedia_Class is access all Multimedia_Type'Class;",
       }   ,
       {
       name: "Pointer_To_Video_Class",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Pointer_To_Video_Class",
       signature: "gnoga.gui.element.multimedia.pointer_to_video_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Video_Class is access all Video_Type'Class;",
       }   ,
       {
       name: "Video_Access",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Video_Access",
       signature: "gnoga.gui.element.multimedia.video_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Video_Access is access all Video_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Volume_Range",
       qualified_name: "Gnoga.Gui.Element.Multimedia.Volume_Range",
       signature: "gnoga.gui.element.multimedia.volume_range",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Volume_Range is Float range 0.0 .. 1.0;",
       }   ,
   ]
,}
---

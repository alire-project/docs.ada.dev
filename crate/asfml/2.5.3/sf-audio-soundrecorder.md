---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Audio.SoundRecorder",
qualified_name: "Sf.Audio.SoundRecorder",
signature: "sf.audio.soundrecorder",
enclosing: "sf.audio",
is_private: false,
documentation: "/< Type of the callback used when starting a capture",
documentation_snippet: "",
access_types:    [
       {
       name: "sfSoundRecorderProcessCallback",
       qualified_name: "Sf.Audio.SoundRecorder.sfSoundRecorderProcessCallback",
       signature: "sf.audio.soundrecorder.sfsoundrecorderprocesscallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSoundRecorderProcessCallback is access function\n  (arg1     : access sfInt16;\n   arg2     : sfSize_t;\n   userData : Standard.System.Address) return sfBool;",
       }   ,
       {
       name: "sfSoundRecorderStartCallback",
       qualified_name: "Sf.Audio.SoundRecorder.sfSoundRecorderStartCallback",
       signature: "sf.audio.soundrecorder.sfsoundrecorderstartcallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSoundRecorderStartCallback is access function\n  (userData : Standard.System.Address) return sfBool;",
       }   ,
       {
       name: "sfSoundRecorderStopCallback",
       qualified_name: "Sf.Audio.SoundRecorder.sfSoundRecorderStopCallback",
       signature: "sf.audio.soundrecorder.sfsoundrecorderstopcallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSoundRecorderStopCallback is access procedure (userData : Standard.System.Address);",
       }   ,
   ]
,}
---

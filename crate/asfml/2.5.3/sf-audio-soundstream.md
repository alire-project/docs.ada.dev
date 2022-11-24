---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Audio.SoundStream",
qualified_name: "Sf.Audio.SoundStream",
signature: "sf.audio.soundstream",
enclosing: "sf.audio",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ sfSoundStreamChunk defines the data to fill by the\n/ OnGetData callback\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
record_types:    [
       {
       name: "sfSoundStreamChunk",
       qualified_name: "Sf.Audio.SoundStream.sfSoundStreamChunk",
       signature: "sf.audio.soundstream.sfsoundstreamchunk",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Samples\n  /< Pointer to the audio samples\n@field NbSamples\n  /< Number of samples pointed by Samples",
       documentation_snippet: "type sfSoundStreamChunk is record\n   Samples   : sfInt16_Ptr;\n   NbSamples : aliased sfUint32;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "sfSoundStreamGetDataCallback",
       qualified_name: "Sf.Audio.SoundStream.sfSoundStreamGetDataCallback",
       signature: "sf.audio.soundstream.sfsoundstreamgetdatacallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSoundStreamGetDataCallback is access\n  function (chunk : access sfSoundStreamChunk;\n            userData : Standard.System.Address) return sfBool;",
       }   ,
       {
       name: "sfSoundStreamSeekCallback",
       qualified_name: "Sf.Audio.SoundStream.sfSoundStreamSeekCallback",
       signature: "sf.audio.soundstream.sfsoundstreamseekcallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSoundStreamSeekCallback is access\n  procedure (time : Sf.System.Time.sfTime; userData : Standard.System.Address);",
       }   ,
   ]
,}
---

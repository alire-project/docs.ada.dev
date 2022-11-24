---
crate: pygamer_simulator
layout: gnatdoc
gnatdoc: {
name: "PyGamer.Audio",
qualified_name: "PyGamer.Audio",
signature: "pygamer.audio",
enclosing: "pygamer",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Sample_Rate_Kind",
       qualified_name: "PyGamer.Audio.Sample_Rate_Kind",
       signature: "pygamer.audio.sample_rate_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sample_Rate_Kind is (SR_11025, SR_22050, SR_44100, SR_96000);",
       }   ,
   ]
,array_types:    [
       {
       name: "Data_Array",
       qualified_name: "PyGamer.Audio.Data_Array",
       signature: "pygamer.audio.data_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Array is array (Natural range <>) of aliased Interfaces.Unsigned_16;",
       }   ,
   ]
,access_types:    [
       {
       name: "Audio_Callback",
       qualified_name: "PyGamer.Audio.Audio_Callback",
       signature: "pygamer.audio.audio_callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Callback is access procedure (Left, Right : out Data_Array);",
       }   ,
   ]
,}
---

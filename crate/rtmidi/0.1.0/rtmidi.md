---
crate: rtmidi
layout: gnatdoc
gnatdoc: {
name: "RtMIDI",
qualified_name: "RtMIDI",
signature: "rtmidi",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "MIDI_In",
       qualified_name: "RtMIDI.MIDI_In",
       signature: "rtmidi.midi_in",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MIDI_In is limited private;",
       }   ,
       {
       name: "MIDI_Out",
       qualified_name: "RtMIDI.MIDI_Out",
       signature: "rtmidi.midi_out",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MIDI_Out is limited private;",
       }   ,
       {
       name: "RtMidiApi",
       qualified_name: "RtMIDI.RtMidiApi",
       signature: "rtmidi.rtmidiapi",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RtMidiApi is\n  (API_UNSPECIFIED,\n   API_MACOSX_CORE,\n   API_LINUX_ALSA,\n   API_UNIX_JACK,\n   API_WINDOWS_MM,\n   API_RTMIDI_DUMMY,\n   API_NUM)\n  with Convention => C;",
       }   ,
   ]
,access_types:    [
       {
       name: "Input_Callback_C",
       qualified_name: "RtMIDI.Input_Callback_C",
       signature: "rtmidi.input_callback_c",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Input_Callback_C is access procedure\n  (Time_Stamp   : Interfaces.C.double;\n   Message      : System.Address;\n   Message_Size : Interfaces.C.size_t;\n   User_Data    : System.Address)\n  with Convention => C;",
       }   ,
   ]
,}
---

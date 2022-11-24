---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Events.Events",
qualified_name: "SDL.Events.Events",
signature: "sdl.events.events",
enclosing: "sdl.events",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Event_Selector",
       qualified_name: "SDL.Events.Events.Event_Selector",
       signature: "sdl.events.events.event_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Event_Selector is (Is_Event,\n                        Is_Window_Event,\n                        Is_Keyboard_Event,\n                        Is_Text_Editing_Event,\n                        Is_Text_Input_Event,\n                        Is_Mouse_Motion_Event,\n                        Is_Mouse_Button_Event,\n                        Is_Mouse_Wheel_Event,\n                        Is_Joystick_Axis_Event,\n                        Is_Joystick_Ball_Event,\n                        Is_Joystick_Hat_Event,\n                        Is_Joystick_Button_Event,\n                        Is_Joystick_Device_Event,\n                        Is_Controller_Axis_Event,\n                        Is_Controller_Button_Event,\n                        Is_Controller_Device_Event,\n                        Is_Touch_Finger_Event,\n                        Is_Touch_Multi_Gesture_Event,\n                        Is_Touch_Dollar_Gesture,\n                        Is_Drop_Event);",
       }   ,
   ]
,record_types:    [
       {
       name: "Events",
       qualified_name: "SDL.Events.Events.Events",
       signature: "sdl.events.events.events",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Events (Event_Type : Event_Selector := Is_Event) is\n   record\n      case Event_Type is\n         when Is_Window_Event =>\n            Window               : SDL.Events.Windows.Window_Events;\n         when Is_Keyboard_Event =>\n            Keyboard             : SDL.Events.Keyboards.Keyboard_Events;\n         when Is_Text_Editing_Event =>\n            Text_Editing         : SDL.Events.Keyboards.Text_Editing_Events;\n         when Is_Text_Input_Event =>\n            Text_Input           : SDL.Events.Keyboards.Text_Input_Events;\n         when Is_Mouse_Motion_Event =>\n            Mouse_Motion         : SDL.Events.Mice.Motion_Events;\n         when Is_Mouse_Button_Event =>\n            Mouse_Button         : SDL.Events.Mice.Button_Events;\n         when Is_Mouse_Wheel_Event =>\n            Mouse_Wheel          : SDL.Events.Mice.Wheel_Events;\n         when Is_Joystick_Axis_Event =>\n            Joystick_Axis        : SDL.Events.Joysticks.Axis_Events;\n         when Is_Joystick_Ball_Event =>\n            Joystick_Ball        : SDL.Events.Joysticks.Ball_Events;\n         when Is_Joystick_Hat_Event =>\n            Joystick_Hat         : SDL.Events.Joysticks.Hat_Events;\n         when Is_Joystick_Button_Event =>\n            Joystick_Button      : SDL.Events.Joysticks.Button_Events;\n         when Is_Joystick_Device_Event =>\n            Joystick_Device      : SDL.Events.Joysticks.Device_Events;\n         when Is_Controller_Axis_Event =>\n            Controller_Axis      : SDL.Events.Controllers.Axis_Events;\n         when Is_Controller_Button_Event =>\n            Controller_Button    : SDL.Events.Controllers.Button_Events;\n         when Is_Controller_Device_Event =>\n            Controller_Device    : SDL.Events.Controllers.Device_Events;\n         when Is_Touch_Finger_Event =>\n            Touch_Finger         : SDL.Events.Touches.Finger_Events;\n         when Is_Touch_Multi_Gesture_Event =>\n            Touch_Multi_Gesture  : SDL.Events.Touches.Multi_Gesture_Events;\n         when Is_Touch_Dollar_Gesture =>\n            Touch_Dollar_Gesture : SDL.Events.Touches.Dollar_Events;\n         when Is_Drop_Event =>\n            Drop                 : SDL.Events.Files.Drop_Events;\n         when others =>\n            Common               : Common_Events;\n      end case;\n   end record with\n  Unchecked_Union,\n  Convention => C;",
       }   ,
   ]
,}
---

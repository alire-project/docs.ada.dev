---
crate: emojis
layout: gnatdoc
gnatdoc: {
name: "Emojis",
qualified_name: "Emojis",
signature: "emojis",
enclosing: "",
is_private: false,
documentation: "SPDX-License-Identifier: Apache-2.0\n\nCopyright (c) 2021 onox <denkpadje@gmail.com>\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.",
documentation_snippet: "",
array_types:    [
       {
       name: "Label_Mappings",
       qualified_name: "Emojis.Label_Mappings",
       signature: "emojis.label_mappings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Label_Mappings is array (Positive range <>) of Text_Label_Pair;",
       }   ,
   ]
,record_types:    [
       {
       name: "Text_Label_Pair",
       qualified_name: "Emojis.Text_Label_Pair",
       signature: "emojis.text_label_pair",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Label_Pair is record\n   Text, Label : SU.Unbounded_String;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Completion_Mappings",
       qualified_name: "Emojis.Completion_Mappings",
       signature: "emojis.completion_mappings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Completion_Mappings is String_List;",
       }   ,
       {
       name: "String_List",
       qualified_name: "Emojis.String_List",
       signature: "emojis.string_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype String_List is Strings.String_List;",
       }   ,
   ]
,constants:    [
       {
       name: "Lower_Case_Text_Emojis",
       qualified_name: "Emojis.Lower_Case_Text_Emojis",
       signature: "emojis.lower_case_text_emojis",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lower_Case_Text_Emojis : constant Completion_Mappings :=\n  (+\":o\", +\":p\", +\"XD\");",
       }   ,
       {
       name: "Text_Emojis",
       qualified_name: "Emojis.Text_Emojis",
       signature: "emojis.text_emojis",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Text_Emojis : constant Label_Mappings :=\n  ((+\":)\", +\"slightly_smiling_face\"),\n   (+\";)\", +\"wink\"),\n   (+\":D\", +\"grinning\"),\n   (+\":'D\", +\"sweat_smile\"),\n   (+\":')\", +\"sweat_smile\"),\n   (+\":\"\")\", +\"joy\"),\n   (+\"XD\", +\"laughing\"),\n   (+\"X'D\", +\"rolling_on_the_floor_laughing\"),\n   (+\":o\", +\"open_mouth\"),\n   (+\":O\", +\"open_mouth\"),\n   (+\">:(\", +\"angry\"),\n   (+\":(\", +\"slightly_frowning_face\"),\n   (+\"-_-\", +\"unamused\"),\n   (+\":'(\", +\"cry\"),\n   (+\":\"\"(\", +\"sob\"),\n   (+\":p\", +\"stuck_out_tongue\"),\n   (+\":P\", +\"stuck_out_tongue\"),\n   (+\";p\", +\"stuck_out_tongue_winking_eye\"),\n   (+\";P\", +\"stuck_out_tongue_winking_eye\"),\n   (+\"B)\", +\"sunglasses\"),\n   (+\":+)\", +\"clown_face\"),\n   (+\":(=\", +\"hot_face\"),\n   (+\"o_O\", +\"face_with_raised_eyebrow\"),\n   (+\"O_o\", +\"face_with_raised_eyebrow\"),\n   (+\"XO=\", +\"face_vomiting\"),\n   (+\"<3\", +\"orange_heart\"));",
       }   ,
   ]
,}
---

---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki",
qualified_name: "Wiki",
signature: "wiki",
enclosing: "",
is_private: false,
documentation: "Defines the possible wiki syntax supported by the parser.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Format_Type",
       qualified_name: "Wiki.Format_Type",
       signature: "wiki.format_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Format_Type is (BOLD, STRONG, ITALIC, EMPHASIS, CODE, SUPERSCRIPT, SUBSCRIPT, STRIKEOUT,\n                     PREFORMAT, INS, UNDERLINE, CITE);",
       }   ,
       {
       name: "Html_Tag",
       qualified_name: "Wiki.Html_Tag",
       signature: "wiki.html_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Html_Tag is\n  (\n   ROOT_HTML_TAG,\n   HEAD_TAG, TITLE_TAG, BASE_TAG, LINK_TAG, META_TAG, STYLE_TAG,\n   BODY_TAG, ARTICLE_TAG, SECTION_TAG, NAV_TAG, ASIDE_TAG,\n   H1_TAG, H2_TAG, H3_TAG, H4_TAG, H5_TAG, H6_TAG,\n   HEADER_TAG, FOOTER_TAG,\n   ADDRESS_TAG,\n   P_TAG, HR_TAG, PRE_TAG, BLOCKQUOTE_TAG,\n   OL_TAG, UL_TAG, LI_TAG,\n   DL_TAG, DT_TAG, DD_TAG,\n   FIGURE_TAG, FIGCAPTION_TAG,\n   DIV_TAG, MAIN_TAG,\n   A_TAG, EM_TAG, STRONG_TAG, SMALL_TAG,\n   S_TAG, CITE_TAG, Q_TAG, DFN_TAG, ABBR_TAG,\n   DATA_TAG, TIME_TAG, CODE_TAG, VAR_TAG, SAMP_TAG,\n   KBD_TAG, SUB_TAG, SUP_TAG,\n   I_TAG, B_TAG, U_TAG,\n   MARK_TAG, RUBY_TAG, RB_TAG, RT_TAG, RTC_TAG,\n   RP_TAG, BDI_TAG, BDO_TAG, SPAN_TAG,\n   BR_TAG, WBR_TAG,\n   INS_TAG, DEL_TAG,\n   IMG_TAG,\n   IFRAME_TAG,\n   EMBED_TAG,\n   OBJECT_TAG,\n   PARAM_TAG,\n   VIDEO_TAG,\n   AUDIO_TAG,\n   SOURCE_TAG,\n   TRACK_TAG,\n   MAP_TAG,\n   AREA_TAG,\n   TABLE_TAG, CAPTION_TAG, COLGROUP_TAG, COL_TAG,\n   TBODY_TAG, THEAD_TAG, TFOOT_TAG,\n   TR_TAG, TD_TAG, TH_TAG,\n   FORM_TAG, LABEL_TAG, INPUT_TAG,\n   BUTTON_TAG, SELECT_TAG, DATALIST_TAG, OPTGROUP_TAG,\n   OPTION_TAG, TEXTAREA_TAG, KEYGEN_TAG, OUTPUT_TAG,\n   PROGRESS_TAG, METER_TAG, FIELDSET_TAG, LEGEND_TAG,\n   SCRIPT_TAG, NOSCRIPT_TAG,\n   TEMPLATE_TAG, CANVAS_TAG,\n   TT_TAG,\n   UNKNOWN_TAG\n  );",
       }   ,
       {
       name: "Wiki_Syntax",
       qualified_name: "Wiki.Wiki_Syntax",
       signature: "wiki.wiki_syntax",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wiki_Syntax\n   is (\n      SYNTAX_GOOGLE,\n      SYNTAX_CREOLE,\n      SYNTAX_DOTCLEAR,\n      SYNTAX_PHPBB,\n      SYNTAX_MEDIA_WIKI,\n      SYNTAX_MARKDOWN,\n      SYNTAX_TEXTILE,\n      SYNTAX_HTML);",
       }   ,
   ]
,array_types:    [
       {
       name: "Format_Map",
       qualified_name: "Wiki.Format_Map",
       signature: "wiki.format_map",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Format_Map is array (Format_Type) of Boolean;",
       }   ,
       {
       name: "Tag_Boolean_Array",
       qualified_name: "Wiki.Tag_Boolean_Array",
       signature: "wiki.tag_boolean_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Boolean_Array is array (Html_Tag) of Boolean;",
       }   ,
   ]
,access_types:    [
       {
       name: "String_Access",
       qualified_name: "Wiki.String_Access",
       signature: "wiki.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is access constant String;",
       }   ,
   ]
,constants:    [
       {
       name: "No_End_Tag",
       qualified_name: "Wiki.No_End_Tag",
       signature: "wiki.no_end_tag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_End_Tag   : constant Tag_Boolean_Array :=\n  (\n   BASE_TAG   => True,\n   LINK_TAG   => True,\n   META_TAG   => True,\n   IMG_TAG    => True,\n   HR_TAG     => True,\n   BR_TAG     => True,\n   WBR_TAG    => True,\n   INPUT_TAG  => True,\n   KEYGEN_TAG => True,\n   others     => False);",
       }   ,
       {
       name: "Tag_Omission",
       qualified_name: "Wiki.Tag_Omission",
       signature: "wiki.tag_omission",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Tag_Omission : constant Tag_Boolean_Array :=\n  (\n   LI_TAG    => True,\n   DT_TAG    => True,\n   DD_TAG    => True,\n   RB_TAG    => True,\n   RT_TAG    => True,\n   RTC_TAG   => True,\n   RP_TAG    => True,\n   TH_TAG    => True,\n   TD_TAG    => True,\n   TR_TAG    => True,\n   TBODY_TAG => True,\n   THEAD_TAG => True,\n   TFOOT_TAG => True,\n   OPTGROUP_TAG => True,\n   OPTION_TAG   => True,\n   others    => False);",
       }   ,
       {
       name: "Tag_Text",
       qualified_name: "Wiki.Tag_Text",
       signature: "wiki.tag_text",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Tag_Text : constant Tag_Boolean_Array :=\n  (\n    A_TAG      => True,\n    EM_TAG     => True,\n    STRONG_TAG => True,\n    SMALL_TAG  => True,\n    S_TAG      => True,\n    CITE_TAG   => True,\n    Q_TAG      => True,\n    DFN_TAG    => True,\n    ABBR_TAG   => True,\n    TIME_TAG   => True,\n    CODE_TAG   => True,\n    VAR_TAG    => True,\n    SAMP_TAG   => True,\n    KBD_TAG    => True,\n    SUB_TAG    => True,\n    SUP_TAG    => True,\n    I_TAG      => True,\n    B_TAG      => True,\n    MARK_TAG   => True,\n    RUBY_TAG   => True,\n    RT_TAG     => True,\n    RP_TAG     => True,\n    BDI_TAG    => True,\n    BDO_TAG    => True,\n    SPAN_TAG   => True,\n    INS_TAG    => True,\n    DEL_TAG    => True,\n    TT_TAG     => True,\n    UNKNOWN_TAG => True,\n    others     => False\n  );",
       }   ,
   ]
,}
---

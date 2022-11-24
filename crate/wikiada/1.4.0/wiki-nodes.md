---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Nodes",
qualified_name: "Wiki.Nodes",
signature: "wiki.nodes",
enclosing: "wiki",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Node_Kind",
       qualified_name: "Wiki.Nodes.Node_Kind",
       signature: "wiki.nodes.node_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Kind is (N_NONE,\n                   N_LINE_BREAK,\n                   N_HORIZONTAL_RULE,\n                   N_TOC_DISPLAY,\n                   N_PARAGRAPH,\n                   N_LIST_ITEM_END,\n                   N_LIST_END,\n                   N_NUM_LIST_END,\n                   N_LIST_ITEM,\n                   N_END_DEFINITION,\n                   N_NEWLINE,\n                   N_TOC_ENTRY,\n                   N_HEADER,\n                   N_BLOCKQUOTE,\n                   N_INDENT,\n                   N_NUM_LIST_START,\n                   N_LIST_START,\n                   N_DEFINITION,\n                   N_TAG_START,\n                   N_TABLE,\n                   N_ROW,\n                   N_COLUMN,\n                   N_TOC,\n                   N_QUOTE,\n                   N_PREFORMAT,\n                   N_TEXT,\n                   N_LINK,\n                   N_LINK_REF,\n                   N_LINK_REF_END,\n                   N_IMAGE);",
       }   ,
       {
       name: "Node_List",
       qualified_name: "Wiki.Nodes.Node_List",
       signature: "wiki.nodes.node_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_List is limited private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Node_Type",
       qualified_name: "Wiki.Nodes.Node_Type",
       signature: "wiki.nodes.node_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Type (Kind : Node_Kind; Len : Natural) is limited record\n   Parent     : Node_Type_Access;\n   case Kind is\n      when N_HEADER | N_BLOCKQUOTE | N_INDENT\n         | N_NUM_LIST_START | N_LIST_START | N_DEFINITION =>\n         Level  : Natural := 0;\n         Content   : Node_List_Access;\n      when N_TEXT =>\n         Format : Format_Map;\n         Text   : Wiki.Strings.WString (1 .. Len);\n      when N_LINK | N_IMAGE | N_QUOTE | N_LINK_REF =>\n         Link_Attr  : Wiki.Attributes.Attribute_List;\n         Title      : Wiki.Strings.WString (1 .. Len);\n      when N_TAG_START | N_TABLE | N_ROW | N_COLUMN =>\n         Tag_Start  : Html_Tag;\n         Attributes : Wiki.Attributes.Attribute_List;\n         Children   : Node_List_Access;\n      when N_PREFORMAT =>\n         Language     : Wiki.Strings.UString;\n         Preformatted : Wiki.Strings.WString (1 .. Len);\n      when N_TOC_ENTRY =>\n         Header    : Wiki.Strings.WString (1 .. Len);\n         Toc_Level : Natural := 0;\n      when N_TOC =>\n         Entries    : Node_List_Access;\n      when others =>\n         null;\n   end case;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Node_List_Access",
       qualified_name: "Wiki.Nodes.Node_List_Access",
       signature: "wiki.nodes.node_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_List_Access is access all Node_List;",
       }   ,
       {
       name: "Node_Type_Access",
       qualified_name: "Wiki.Nodes.Node_Type_Access",
       signature: "wiki.nodes.node_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Type_Access is access all Node_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Simple_Node_Kind",
       qualified_name: "Wiki.Nodes.Simple_Node_Kind",
       signature: "wiki.nodes.simple_node_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Simple_Node_Kind is Node_Kind range N_NONE .. N_NEWLINE;",
       }   ,
   ]
,}
---

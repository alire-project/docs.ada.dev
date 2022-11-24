---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Render.Links",
qualified_name: "Wiki.Render.Links",
signature: "wiki.render.links",
enclosing: "wiki.render",
is_private: false,
documentation: "",
documentation_snippet: "",
interface_types:    [
       {
       name: "Link_Renderer",
       qualified_name: "Wiki.Render.Links.Link_Renderer",
       signature: "wiki.render.links.link_renderer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Link_Renderer is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Default_Link_Renderer",
       qualified_name: "Wiki.Render.Links.Default_Link_Renderer",
       signature: "wiki.render.links.default_link_renderer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_Link_Renderer is new Link_Renderer with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Link_Renderer_Access",
       qualified_name: "Wiki.Render.Links.Link_Renderer_Access",
       signature: "wiki.render.links.link_renderer_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Link_Renderer_Access is access all Link_Renderer'Class;",
       }   ,
   ]
,}
---

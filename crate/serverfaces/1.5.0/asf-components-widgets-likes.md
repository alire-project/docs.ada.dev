---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Components.Widgets.Likes",
qualified_name: "ASF.Components.Widgets.Likes",
signature: "asf.components.widgets.likes",
enclosing: "asf.components.widgets",
is_private: false,
documentation: "------------------------------\nUILike\n------------------------------\nThe <b>UILike</b> component displays a social like button to recommend a page.",
documentation_snippet: "",
interface_types:    [
       {
       name: "Like_Generator",
       qualified_name: "ASF.Components.Widgets.Likes.Like_Generator",
       signature: "asf.components.widgets.likes.like_generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Like_Generator is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Facebook_Like_Generator",
       qualified_name: "ASF.Components.Widgets.Likes.Facebook_Like_Generator",
       signature: "asf.components.widgets.likes.facebook_like_generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Facebook_Like_Generator is new Like_Generator with null record;",
       }   ,
       {
       name: "Twitter_Like_Generator",
       qualified_name: "ASF.Components.Widgets.Likes.Twitter_Like_Generator",
       signature: "asf.components.widgets.likes.twitter_like_generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Twitter_Like_Generator is new Like_Generator with null record;",
       }   ,
       {
       name: "UILike",
       qualified_name: "ASF.Components.Widgets.Likes.UILike",
       signature: "asf.components.widgets.likes.uilike",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UILike is new ASF.Components.Html.UIHtmlComponent with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Like_Generator_Access",
       qualified_name: "ASF.Components.Widgets.Likes.Like_Generator_Access",
       signature: "asf.components.widgets.likes.like_generator_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Like_Generator_Access is access all Like_Generator'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "MAX_LIKE_GENERATOR",
       qualified_name: "ASF.Components.Widgets.Likes.MAX_LIKE_GENERATOR",
       signature: "asf.components.widgets.likes.max_like_generator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_LIKE_GENERATOR : constant Positive := 5;",
       }   ,
   ]
,}
---

---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.RenderWindow",
qualified_name: "Sf.Graphics.RenderWindow",
signature: "sf.graphics.renderwindow",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Construct a new render window\n/\n/ @param mode     Video mode to use\n/ @param title    Title of the window\n/ @param style    Window style\n/ @param settings Creation settings\n/\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
packages:    [
       {
       name: "Mouse",
       qualified_name: "Sf.Graphics.RenderWindow.Mouse",
       signature: "sf.graphics.renderwindow.mouse",
       enclosing: "sf.graphics.renderwindow",
       is_private: false,
       documentation: "//////////////////////////////////////////////////////////\n/ @brief Get the current position of the mouse relative to a render-window\n/\n/ This function returns the current position of the mouse\n/ cursor relative to the given render-window, or desktop if NULL is passed.\n/\n/ @param relativeTo Reference window\n/\n/ @return Position of the mouse cursor, relative to the given render window\n/\n//////////////////////////////////////////////////////////",
       documentation_snippet: "",
       }   ,
       {
       name: "Touch",
       qualified_name: "Sf.Graphics.RenderWindow.Touch",
       signature: "sf.graphics.renderwindow.touch",
       enclosing: "sf.graphics.renderwindow",
       is_private: false,
       documentation: "//////////////////////////////////////////////////////////\n/ @brief Get the current position of a touch in window coordinates\n/\n/ This function returns the current touch position\n/ relative to the given render window, or desktop if NULL is passed.\n/\n/ @param finger Finger index\n/ @param relativeTo Reference window\n/\n/ @return Current position of @a finger, or undefined if it's not down\n/\n//////////////////////////////////////////////////////////",
       documentation_snippet: "",
       }   ,
   ]
,}
---

---
crate: progress_indicators
layout: gnatdoc
gnatdoc: {
name: "Progress_Indicators.Spinners",
qualified_name: "Progress_Indicators.Spinners",
signature: "progress_indicators.spinners",
enclosing: "progress_indicators",
is_private: false,
documentation: "It's always fun to have a fun spinning indicator while waiting for\nterminal work to complete.  This is just a simple reusable version useful\nfor tasks monitoring work to indicate that the process isn't dead.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Spinner",
       qualified_name: "Progress_Indicators.Spinners.Spinner",
       signature: "progress_indicators.spinners.spinner",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Spinner is private;",
       }   ,
       {
       name: "Spinner_Style",
       qualified_name: "Progress_Indicators.Spinners.Spinner_Style",
       signature: "progress_indicators.spinners.spinner_style",
       enclosing: "",
       is_private: false,
       documentation: "What happens when you get the value of the spinner?\n\nEmpty returns an empty string, useful for disabling spinners when not\nrunning interactively.\n\nIn_Place inserts the appropriate ANSI escape sequence after the moving\nbar to overwrite in-place when called with `Put` in sequence.\n\nNormal just returns the next moving bar.\n\n@enum Empty\n@enum In_Place\n@enum Normal",
       documentation_snippet: "type Spinner_Style is (Empty, In_Place, Normal);",
       }   ,
   ]
,}
---

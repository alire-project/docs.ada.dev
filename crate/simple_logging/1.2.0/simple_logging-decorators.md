---
crate: simple_logging
layout: gnatdoc
gnatdoc: {
name: "Simple_Logging.Decorators",
qualified_name: "Simple_Logging.Decorators",
signature: "simple_logging.decorators",
enclosing: "simple_logging",
is_private: false,
documentation: "------------\n Defaults --\n------------\n  These functions are used by default for log decoration.\n  They take the log message and modify it somehow.",
documentation_snippet: "",
variables:    [
       {
       name: "Entity_Width",
       qualified_name: "Simple_Logging.Decorators.Entity_Width",
       signature: "simple_logging.decorators.entity_width",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Entity_Width   : Positive range 2 .. Positive'Last := 24;",
       }   ,
       {
       name: "Level_Decorator",
       qualified_name: "Simple_Logging.Decorators.Level_Decorator",
       signature: "simple_logging.decorators.level_decorator",
       enclosing: "",
       is_private: false,
       documentation: "Use simple text prefixes for normal levels, markers for verbose levels.",
       documentation_snippet: "Level_Decorator : access function (Level : Levels;\n                                   Message : String) return String :=\n  Default_Level_Decorator'Access;",
       }   ,
       {
       name: "Location_Decorator",
       qualified_name: "Simple_Logging.Decorators.Location_Decorator",
       signature: "simple_logging.decorators.location_decorator",
       enclosing: "",
       is_private: false,
       documentation: "No entity/location information by default.\nSee Simple_Location_Decorator above for a \"[entity] (location) Msg\" option.",
       documentation_snippet: "Location_Decorator : access function (Entity,\n                                      Location,\n                                      Message : String) return String :=\n  No_Location_Decorator'Access;",
       }   ,
       {
       name: "Location_Width",
       qualified_name: "Simple_Logging.Decorators.Location_Width",
       signature: "simple_logging.decorators.location_width",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Location_Width : Positive range 2 .. Positive'Last := 24;",
       }   ,
   ]
,}
---

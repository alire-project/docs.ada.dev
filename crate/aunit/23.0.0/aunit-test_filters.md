---
crate: aunit
layout: gnatdoc
gnatdoc: {
name: "AUnit.Test_Filters",
qualified_name: "AUnit.Test_Filters",
signature: "aunit.test_filters",
enclosing: "aunit",
is_private: false,
documentation: "An instance of a test filter.\nThis can be created from command line arguments, for instance, so that\nusers can decide to run specific tests only, as opposed to the whole\ntest suite.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Name_Filter",
       qualified_name: "AUnit.Test_Filters.Name_Filter",
       signature: "aunit.test_filters.name_filter",
       enclosing: "",
       is_private: false,
       documentation: "A filter based on the name of the test and/or routine.",
       documentation_snippet: "type Name_Filter is new Test_Filter with private;",
       }   ,
       {
       name: "Test_Filter",
       qualified_name: "AUnit.Test_Filters.Test_Filter",
       signature: "aunit.test_filters.test_filter",
       enclosing: "",
       is_private: false,
       documentation: "Whether we should run the given test. If this function returns False,\nthe test is not run.",
       documentation_snippet: "type Test_Filter is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Test_Filter_Access",
       qualified_name: "AUnit.Test_Filters.Test_Filter_Access",
       signature: "aunit.test_filters.test_filter_access",
       enclosing: "",
       is_private: false,
       documentation: "Whether we should run the given test. If this function returns False,\nthe test is not run.",
       documentation_snippet: "type Test_Filter_Access is access all Test_Filter'Class;",
       }   ,
   ]
,}
---

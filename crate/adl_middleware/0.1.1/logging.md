---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Logging",
qualified_name: "Logging",
signature: "logging",
enclosing: "",
is_private: false,
documentation: "This package is based on two features implemented in different packages:\n    - Logging_With_Categories\n    - Logging_With_Priorities\n\nYou can directly use one of those pacakge if you are not interested by the\nother feature.\n\n@formal Categories\n  Logging categories\n  Typicaly an enum type, example:\n     type My_Log_Categories is (Debug, Warning, Error);\n@formal Priorities\n  Logging priority type\n@formal Default_Category\n  Category used when the category is not specified as parameter\n@formal Default_Priority\n  Priority value used at initialization\n@formal Categories_Enabled_By_Default\n  If this value is true, all logging categories are enabled at\n  initialization. Otherwise, they are all disabled.\n@formal Prefix_Enabled_By_Default\n  If this value is true, prefix is enabled for all categories at\n  initialization. Otherwise, it is diabled for all.\n@formal Maximum_Message_Length\n  Maximum number of Characters in a message. Messages longer than this\n  limit will be rejected.\n@formal Maximum_Number_Of_Messages\n  Maximum number of messages in the queue. When the queue is filled the\n  lower priority will be discared.",
documentation_snippet: "",
}
---

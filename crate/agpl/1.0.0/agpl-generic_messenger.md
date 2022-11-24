---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Generic_Messenger",
qualified_name: "Agpl.Generic_Messenger",
signature: "agpl.generic_messenger",
enclosing: "agpl",
is_private: false,
documentation: "Since there's no selectable signals for registration, it should not be used\nfor heavy traffic, I suppose.\n\n@formal Signal_Kind\n@formal Message_Data",
documentation_snippet: "",
record_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Generic_Messenger.Object",
       signature: "agpl.generic_messenger.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is abstract tagged null record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Manager",
       qualified_name: "Agpl.Generic_Messenger.Manager",
       signature: "agpl.generic_messenger.manager",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Manager is tagged private;",
       }   ,
   ]
,}
---

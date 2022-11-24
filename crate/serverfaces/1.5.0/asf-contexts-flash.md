---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Contexts.Flash",
qualified_name: "ASF.Contexts.Flash",
signature: "asf.contexts.flash",
enclosing: "asf.contexts",
is_private: false,
documentation: "------------------------------\nFlash context\n------------------------------\nThe <b>Flash_Context</b> gives access to the flash instance and its management.\nThere are two flash instances: the 'previous' and the 'next' one.\n o attributes are read from the 'previous' instance,\n o attributes are written by default to the 'next' instance,",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Flash_Context",
       qualified_name: "ASF.Contexts.Flash.Flash_Context",
       signature: "asf.contexts.flash.flash_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flash_Context is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Flash_Context_Access",
       qualified_name: "ASF.Contexts.Flash.Flash_Context_Access",
       signature: "asf.contexts.flash.flash_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flash_Context_Access is access all Flash_Context'Class;",
       }   ,
   ]
,}
---

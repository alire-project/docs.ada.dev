---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Soft_Drawing_Bitmap",
qualified_name: "Soft_Drawing_Bitmap",
signature: "soft_drawing_bitmap",
enclosing: "",
is_private: false,
documentation: "This package provides a software implementation of the HAL.Bitmap drawing\nprimitives.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Soft_Drawing_Bitmap_Buffer",
       qualified_name: "Soft_Drawing_Bitmap.Soft_Drawing_Bitmap_Buffer",
       signature: "soft_drawing_bitmap.soft_drawing_bitmap_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Soft_Drawing_Bitmap_Buffer is abstract new Parent with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Soft_Drawing_Bitmap_Buffer",
       qualified_name: "Soft_Drawing_Bitmap.Any_Soft_Drawing_Bitmap_Buffer",
       signature: "soft_drawing_bitmap.any_soft_drawing_bitmap_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Soft_Drawing_Bitmap_Buffer is\n  access all Soft_Drawing_Bitmap_Buffer'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "Soft_Drawing_Bitmap.Parent",
       signature: "soft_drawing_bitmap.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Bitmap_Buffer;",
       }   ,
   ]
,}
---

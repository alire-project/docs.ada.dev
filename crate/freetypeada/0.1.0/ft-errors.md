---
crate: freetypeada
layout: gnatdoc
gnatdoc: {
name: "FT.Errors",
qualified_name: "FT.Errors",
signature: "ft.errors",
enclosing: "ft",
is_private: false,
documentation: "part of FreeTypeAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Error_Code",
       qualified_name: "FT.Errors.Error_Code",
       signature: "ft.errors.error_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Error_Code is\n  (Ok, Cannot_Open_Resource, Unknown_File_Format, Invalid_File_Format,\n   Invalid_Version, Lower_Module_Version, Invalid_Argument,\n   Unimplemented_Feature, Invalid_Table, Invalid_Offset, Array_Too_Large,\n   Missing_Module, Missing_Property, Invalid_Glyph_Index,\n   Invalid_Character_Code, Invalid_Glyph_Format, Cannot_Render_Glyph,\n   Invalid_Outline, Invalid_Composite, Too_Many_Hints, Invalid_Pixel_Size,\n   Invalid_Handle, Invalid_Library_Handle, Invalid_Driver_Handle,\n   Invalid_Face_Handle, Invalid_Size_Handle, Invalid_Slot_Handle,\n   Invalid_CharMap_Handle, Invalid_Cache_Handle, Invalid_Stream_Handle,\n   Too_Many_Drivers, Too_Many_Extensions, Out_Of_Memory, Unlisted_Object,\n   Cannot_Open_Stream, Invalid_Stream_Seek, Invalid_Stream_Skip,\n   Invalid_Stream_Read, Invalid_Stream_Operation, Invalid_Frame_Operation,\n   Nested_Frame_Access, Invalid_Frame_Read, Raster_Uninitialized,\n   Raster_Corrupted, Raster_Overflow, Raster_Negative_Height,\n   Too_Many_Caches, Invalid_Opcode, Too_Few_Arguments, Stack_Overflow,\n   Code_Overflow, Bad_Argument, Divide_By_Zero, Invalid_Reference,\n   Debug_OpCode, ENDF_In_Exec_Stream, Nested_DEFS, Invalid_CodeRange,\n   Execution_Too_Long, Too_Many_Function_Defs, Too_Many_Instruction_Defs,\n   Table_Missing, Horiz_Header_Missing, Locations_Missing,\n   Name_Table_Missing, CMap_Table_Missing, Hmtx_Table_Missing,\n   Post_Table_Missing, Invalid_Horiz_Metrics, Invalid_CharMap_Format,\n   Invalid_PPem, Invalid_Vert_Metrics, Could_Not_Find_Context,\n   Invalid_Post_Table_Format, Invalid_Post_Table, DEF_In_Glyf_Bytecode,\n   Missing_Bitmap, Syntax_Error, Stack_Underflow, Ignore,\n   No_Unicode_Glyph_Name, Glyph_Too_Big, Missing_Startfont_Field,\n   Missing_Font_Field, Missing_Size_Field, Missing_Fontboundingbox_Field,\n   Missing_Chars_Field, Missing_Startchar_Field, Missing_Encoding_Field,\n   Missing_Bbx_Field, Bbx_Too_Big, Corrupted_Font_Header,\n   Corrupted_Font_Glyphs);",
       }   ,
   ]
,subtypes:    [
       {
       name: "BDF_Errors",
       qualified_name: "FT.Errors.BDF_Errors",
       signature: "ft.errors.bdf_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BDF_Errors is Error_Code range\n  Missing_Startfont_Field .. Corrupted_Font_Glyphs;",
       }   ,
       {
       name: "Cache_Errors",
       qualified_name: "FT.Errors.Cache_Errors",
       signature: "ft.errors.cache_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Cache_Errors is Error_Code range Too_Many_Caches .. Too_Many_Caches;",
       }   ,
       {
       name: "CFF_CID_And_Type_1_Errors",
       qualified_name: "FT.Errors.CFF_CID_And_Type_1_Errors",
       signature: "ft.errors.cff_cid_and_type_1_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFF_CID_And_Type_1_Errors is Error_Code range\n  Syntax_Error .. Glyph_Too_Big;",
       }   ,
       {
       name: "Driver_Errors",
       qualified_name: "FT.Errors.Driver_Errors",
       signature: "ft.errors.driver_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Driver_Errors is Error_Code range\n  Too_Many_Drivers .. Too_Many_Extensions;",
       }   ,
       {
       name: "Generic_Errors",
       qualified_name: "FT.Errors.Generic_Errors",
       signature: "ft.errors.generic_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Generic_Errors is Error_Code range Ok .. Missing_Property;",
       }   ,
       {
       name: "Glyph_Character_Errors",
       qualified_name: "FT.Errors.Glyph_Character_Errors",
       signature: "ft.errors.glyph_character_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Glyph_Character_Errors is Error_Code range\n  Invalid_Glyph_Index .. Invalid_Pixel_Size;",
       }   ,
       {
       name: "Handle_Errors",
       qualified_name: "FT.Errors.Handle_Errors",
       signature: "ft.errors.handle_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Handle_Errors is Error_Code range\n  Invalid_Handle .. Invalid_Stream_Handle;",
       }   ,
       {
       name: "Memory_Errors",
       qualified_name: "FT.Errors.Memory_Errors",
       signature: "ft.errors.memory_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Memory_Errors is Error_Code range Out_Of_Memory .. Unlisted_Object;",
       }   ,
       {
       name: "Raster_Errors",
       qualified_name: "FT.Errors.Raster_Errors",
       signature: "ft.errors.raster_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Raster_Errors is Error_Code range\n  Raster_Uninitialized .. Raster_Negative_Height;",
       }   ,
       {
       name: "Stream_Errors",
       qualified_name: "FT.Errors.Stream_Errors",
       signature: "ft.errors.stream_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Stream_Errors is Error_Code range\n  Cannot_Open_Stream .. Invalid_Frame_Read;",
       }   ,
       {
       name: "TrueType_And_SFNT_Errors",
       qualified_name: "FT.Errors.TrueType_And_SFNT_Errors",
       signature: "ft.errors.truetype_and_sfnt_errors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TrueType_And_SFNT_Errors is Error_Code range\n  Invalid_Opcode .. Missing_Bitmap;",
       }   ,
   ]
,}
---

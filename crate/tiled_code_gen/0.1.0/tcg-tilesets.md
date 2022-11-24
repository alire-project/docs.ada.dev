---
crate: tiled_code_gen
layout: gnatdoc
gnatdoc: {
name: "TCG.Tilesets",
qualified_name: "TCG.Tilesets",
signature: "tcg.tilesets",
enclosing: "tcg",
is_private: false,
documentation: "We can load multiple maps, each map can load multiple tile sets and\npotetially the same tile sets will be loaded by different maps.\n\nTo simplify the generated data, we build a unique master tile set that\ncontains all the tiles from all the tile sets of all the maps. The tiles\nfrom the master tile set are indentifiyed with the Master_Tile_Id type.\n\nDuring loading of the maps we have to be able to get the Master_Tile_Id\nof a tile from a specific tile set. For this the function Convert will\nreturn the Master_Tile_Id from the Tileset_Id and the Local_Tile_Id.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Local_Tile_Id",
       qualified_name: "TCG.Tilesets.Local_Tile_Id",
       signature: "tcg.tilesets.local_tile_id",
       enclosing: "",
       is_private: false,
       documentation: "Id of a tile within a given tile set",
       documentation_snippet: "type Local_Tile_Id is new Natural;",
       }   ,
       {
       name: "Map_Tile_Id",
       qualified_name: "TCG.Tilesets.Map_Tile_Id",
       signature: "tcg.tilesets.map_tile_id",
       enclosing: "",
       is_private: false,
       documentation: "Id of a tile within a the layers of a map",
       documentation_snippet: "type Map_Tile_Id is new Natural;",
       }   ,
       {
       name: "Master_Tile_Id",
       qualified_name: "TCG.Tilesets.Master_Tile_Id",
       signature: "tcg.tilesets.master_tile_id",
       enclosing: "",
       is_private: false,
       documentation: "Id of a tile in the unified master tile set",
       documentation_snippet: "type Master_Tile_Id is new Natural;",
       }   ,
       {
       name: "Tileset_Id",
       qualified_name: "TCG.Tilesets.Tileset_Id",
       signature: "tcg.tilesets.tileset_id",
       enclosing: "",
       is_private: false,
       documentation: "Id of one of the loaded tile sets",
       documentation_snippet: "type Tileset_Id is private;",
       }   ,
   ]
,constants:    [
       {
       name: "Invalid_Tileset",
       qualified_name: "TCG.Tilesets.Invalid_Tileset",
       signature: "tcg.tilesets.invalid_tileset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Tileset : constant Tileset_Id;",
       }   ,
       {
       name: "No_Tile",
       qualified_name: "TCG.Tilesets.No_Tile",
       signature: "tcg.tilesets.no_tile",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Tile : constant Master_Tile_Id := 0;",
       }   ,
   ]
,}
---

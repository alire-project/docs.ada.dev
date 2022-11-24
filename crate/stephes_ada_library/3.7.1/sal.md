---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL",
qualified_name: "SAL",
signature: "sal",
enclosing: "",
is_private: false,
documentation: "Abstract:\n\nRoot package for Stephe's Ada Library packages.\n\nSee sal.html for more information.\n\nSee http://stephe-leake.org/ada/sal.html for the\nlatest version.\n\nContact Stephe at stephen_leake@stephe-leake.org.\n\nCopyright (C) 1997 - 2004, 2008, 2009, 2015, 2017, 2018, 2020, 2021 Free Software Foundation, Inc.\n\nSAL is free software; you can redistribute it and/or modify it\nunder terms of the GNU General Public License as published by the\nFree Software Foundation; either version 3, or (at your option) any\nlater version. SAL is distributed in the hope that it will be\nuseful, but WITHOUT ANY WARRANTY; without even the implied warranty\nof MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details. You should have received a\ncopy of the GNU General Public License distributed with SAL; see\nfile COPYING. If not, write to the Free Software Foundation, 59\nTemple Place - Suite 330, Boston, MA 02111-1307, USA.\n\nAs a special exception, if other files instantiate generics from\nSAL, or you link SAL object files with other files to produce\nan executable, that does not by itself cause the resulting\nexecutable to be covered by the GNU General Public License. This\nexception does not however invalidate any other reasons why the\nexecutable file might be covered by the GNU Public License.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Base_Peek_Type",
       qualified_name: "SAL.Base_Peek_Type",
       signature: "sal.base_peek_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Base_Peek_Type is new Ada.Containers.Count_Type range 0 .. Ada.Containers.Count_Type'Last;",
       }   ,
       {
       name: "Compare_Result",
       qualified_name: "SAL.Compare_Result",
       signature: "sal.compare_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Compare_Result is (Less, Equal, Greater);",
       }   ,
       {
       name: "Direction_Type",
       qualified_name: "SAL.Direction_Type",
       signature: "sal.direction_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Direction_Type is (Forward, Backward);",
       }   ,
       {
       name: "Duplicate_Action_Type",
       qualified_name: "SAL.Duplicate_Action_Type",
       signature: "sal.duplicate_action_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Duplicate_Action_Type is (Allow, Ignore, Error);",
       }   ,
       {
       name: "Overflow_Action_Type",
       qualified_name: "SAL.Overflow_Action_Type",
       signature: "sal.overflow_action_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Overflow_Action_Type is (Overwrite, Error);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Ignore_Error_Type",
       qualified_name: "SAL.Ignore_Error_Type",
       signature: "sal.ignore_error_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Ignore_Error_Type is Duplicate_Action_Type range Ignore .. Error;",
       }   ,
       {
       name: "Peek_Type",
       qualified_name: "SAL.Peek_Type",
       signature: "sal.peek_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Peek_Type is Base_Peek_Type range 1 .. Base_Peek_Type'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Invalid_Peek_Index",
       qualified_name: "SAL.Invalid_Peek_Index",
       signature: "sal.invalid_peek_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Peek_Index : constant Base_Peek_Type := 0;",
       }   ,
   ]
,}
---

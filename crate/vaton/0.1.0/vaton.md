---
crate: vaton
layout: gnatdoc
gnatdoc: {
name: "Vaton",
qualified_name: "Vaton",
signature: "vaton",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Digit",
       qualified_name: "Vaton.Digit",
       signature: "vaton.digit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Digit is range 0 .. 9;",
       }   ,
       {
       name: "Number_Kind",
       qualified_name: "Vaton.Number_Kind",
       signature: "vaton.number_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Number_Kind is (NaN, Float, Integer, Long_Float, Long_Long_Float, Long_Integer, Long_Long_Integer, Big_Real, Big_Integer);",
       }   ,
   ]
,record_types:    [
       {
       name: "Number",
       qualified_name: "Vaton.Number",
       signature: "vaton.number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Number (Kind : Number_Kind := NaN) is record\n   case Kind is\n      when NaN =>\n         null;\n      when Float =>\n         Float : Standard.Float := 0.0;\n      when Integer =>\n         Integer : Standard.Integer := 0;\n      when Long_Float =>\n         Long_Float : Standard.Long_Float := 0.0;\n      when Long_Integer =>\n         Long_Integer : Standard.Long_Integer := 0;\n      when Long_Long_Float =>\n         Long_Long_Float : Standard.Long_Long_Float := 0.0;\n      when Long_Long_Integer =>\n         Long_Long_Integer : Standard.Long_Long_Integer := 0;\n      when Big_Real =>\n         Big_Real : Big_Numbers.Big_Reals.Valid_Big_Real := 0.0;\n      when Big_Integer =>\n         Big_Integer : Big_Numbers.Big_Integers.Valid_Big_Integer := 0;\n   end case;\nend record;",
       }   ,
       {
       name: "Number_Pieces",
       qualified_name: "Vaton.Number_Pieces",
       signature: "vaton.number_pieces",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Number_Pieces is record\n   Whole                : Digit_Array.Unbound_Array;\n   Fraction             : Digit_Array.Unbound_Array;\n   Exponent             : Digit_Array.Unbound_Array;\n   Whole_Is_Negative    : Boolean := False;\n   Exponent_Is_Negative : Boolean := False;\n   Has_Exponent         : Boolean := False;\n   Has_Fraction         : Boolean := False;\n   Next_Must_Be_Digit   : Boolean := False;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "BASE_10",
       qualified_name: "Vaton.BASE_10",
       signature: "vaton.base_10",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "BASE_10                    : constant Standard.Integer := 10;",
       }   ,
       {
       name: "BASE_10_LENGTH_TO_BIT_SIZE",
       qualified_name: "Vaton.BASE_10_LENGTH_TO_BIT_SIZE",
       signature: "vaton.base_10_length_to_bit_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "BASE_10_LENGTH_TO_BIT_SIZE : constant Standard.Integer := 4;",
       }   ,
       {
       name: "BIG_NUMBER_DIGIT_LIMIT",
       qualified_name: "Vaton.BIG_NUMBER_DIGIT_LIMIT",
       signature: "vaton.big_number_digit_limit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "BIG_NUMBER_DIGIT_LIMIT : constant Standard.Integer := 1_900;",
       }   ,
       {
       name: "MAX_FLOAT_EXPONENT",
       qualified_name: "Vaton.MAX_FLOAT_EXPONENT",
       signature: "vaton.max_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Float'Machine_Emax);",
       }   ,
       {
       name: "MAX_LONG_FLOAT_EXPONENT",
       qualified_name: "Vaton.MAX_LONG_FLOAT_EXPONENT",
       signature: "vaton.max_long_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_LONG_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Long_Float'Machine_Emax);",
       }   ,
       {
       name: "MAX_LONG_LONG_FLOAT_EXPONENT",
       qualified_name: "Vaton.MAX_LONG_LONG_FLOAT_EXPONENT",
       signature: "vaton.max_long_long_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_LONG_LONG_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Long_Long_Float'Machine_Emax);",
       }   ,
       {
       name: "MIN_FLOAT_EXPONENT",
       qualified_name: "Vaton.MIN_FLOAT_EXPONENT",
       signature: "vaton.min_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MIN_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Float'Machine_Emin);",
       }   ,
       {
       name: "MIN_LONG_FLOAT_EXPONENT",
       qualified_name: "Vaton.MIN_LONG_FLOAT_EXPONENT",
       signature: "vaton.min_long_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MIN_LONG_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Long_Float'Machine_Emin);",
       }   ,
       {
       name: "MIN_LONG_LONG_FLOAT_EXPONENT",
       qualified_name: "Vaton.MIN_LONG_LONG_FLOAT_EXPONENT",
       signature: "vaton.min_long_long_float_exponent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MIN_LONG_LONG_FLOAT_EXPONENT : constant Standard.Integer := Standard.Integer (0.3 * Standard.Long_Long_Float'Machine_Emin);",
       }   ,
   ]
,}
---

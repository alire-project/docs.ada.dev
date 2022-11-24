---
crate: excel_writer
layout: gnatdoc
gnatdoc: {
name: "IEEE_754.Generic_Double_Precision",
qualified_name: "IEEE_754.Generic_Double_Precision",
signature: "ieee_754.generic_double_precision",
enclosing: "ieee_754",
is_private: false,
documentation: "\n Float_64 -- 64-bit double-precision IEEE 754 float. The memory layout\n             is big endian, i.e. the byte containing the number's sign\n and  the  most  significant  bits  of the exponent is the first array\n element.  The  byte  containing  the  least  significant  bits of the\n mantissa is the last array element.\n\n\n@formal Number",
documentation_snippet: "",
array_types:    [
       {
       name: "Float_64",
       qualified_name: "IEEE_754.Generic_Double_Precision.Float_64",
       signature: "ieee_754.generic_double_precision.float_64",
       enclosing: "",
       is_private: false,
       documentation: "\n From_IEEE -- Conversion from 32-bit single precision IEEE 754 float\n\n    Value - The argument\n\n Returns :\n\n    The corresponding floating-point number\n\n Exceptions :\n\n    Not_A_Number_Error      - Not a number\n    Positive_Overflow_Error - Positive infinity or too big positive\n    Negative_Overflow_Error - Negative infinity or too big negative\n",
       documentation_snippet: "type Float_64 is array (1 .. 8) of Byte;",
       }   ,
   ]
,constants:    [
       {
       name: "Negative_Infinity",
       qualified_name: "IEEE_754.Generic_Double_Precision.Negative_Infinity",
       signature: "ieee_754.generic_double_precision.negative_infinity",
       enclosing: "",
       is_private: false,
       documentation: "\n From_IEEE -- Conversion from 32-bit single precision IEEE 754 float\n\n    Value - The argument\n\n Returns :\n\n    The corresponding floating-point number\n\n Exceptions :\n\n    Not_A_Number_Error      - Not a number\n    Positive_Overflow_Error - Positive infinity or too big positive\n    Negative_Overflow_Error - Negative infinity or too big negative\n",
       documentation_snippet: "Negative_Infinity : constant Float_64;",
       }   ,
       {
       name: "Negative_Zero",
       qualified_name: "IEEE_754.Generic_Double_Precision.Negative_Zero",
       signature: "ieee_754.generic_double_precision.negative_zero",
       enclosing: "",
       is_private: false,
       documentation: "\n From_IEEE -- Conversion from 32-bit single precision IEEE 754 float\n\n    Value - The argument\n\n Returns :\n\n    The corresponding floating-point number\n\n Exceptions :\n\n    Not_A_Number_Error      - Not a number\n    Positive_Overflow_Error - Positive infinity or too big positive\n    Negative_Overflow_Error - Negative infinity or too big negative\n",
       documentation_snippet: "Negative_Zero     : constant Float_64;",
       }   ,
       {
       name: "Positive_Infinity",
       qualified_name: "IEEE_754.Generic_Double_Precision.Positive_Infinity",
       signature: "ieee_754.generic_double_precision.positive_infinity",
       enclosing: "",
       is_private: false,
       documentation: "\n From_IEEE -- Conversion from 32-bit single precision IEEE 754 float\n\n    Value - The argument\n\n Returns :\n\n    The corresponding floating-point number\n\n Exceptions :\n\n    Not_A_Number_Error      - Not a number\n    Positive_Overflow_Error - Positive infinity or too big positive\n    Negative_Overflow_Error - Negative infinity or too big negative\n",
       documentation_snippet: "Positive_Infinity : constant Float_64;",
       }   ,
       {
       name: "Positive_Zero",
       qualified_name: "IEEE_754.Generic_Double_Precision.Positive_Zero",
       signature: "ieee_754.generic_double_precision.positive_zero",
       enclosing: "",
       is_private: false,
       documentation: "\n From_IEEE -- Conversion from 32-bit single precision IEEE 754 float\n\n    Value - The argument\n\n Returns :\n\n    The corresponding floating-point number\n\n Exceptions :\n\n    Not_A_Number_Error      - Not a number\n    Positive_Overflow_Error - Positive infinity or too big positive\n    Negative_Overflow_Error - Negative infinity or too big negative\n",
       documentation_snippet: "Positive_Zero     : constant Float_64;",
       }   ,
   ]
,}
---

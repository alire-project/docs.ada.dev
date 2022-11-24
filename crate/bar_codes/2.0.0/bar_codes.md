---
crate: bar_codes
layout: gnatdoc
gnatdoc: {
name: "Bar_Codes",
qualified_name: "Bar_Codes",
signature: "bar_codes",
enclosing: "",
is_private: false,
documentation: "  (*) All Trademarks mentioned are properties of their respective owners.\n-----------------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Kind_Of_Code",
       qualified_name: "Bar_Codes.Kind_Of_Code",
       signature: "bar_codes.kind_of_code",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Code_128\n  \n    QR Code is a popular 2D bar code.\n    Standard: ISO/IEC 18004:2015.\n  \n@enum Code_QR_Low\n  Level L (Low)       7% of codewords can be restored.\n@enum Code_QR_Medium\n  Level M (Medium)   15% of codewords can be restored.\n@enum Code_QR_Quartile\n  Level Q (Quartile) 25% of codewords can be restored.\n@enum Code_QR_High\n  Level H (High)     30% of codewords can be restored.",
       documentation_snippet: "type Kind_Of_Code is (\n  Code_128,\n  Code_QR_Low,\n  Code_QR_Medium,\n  Code_QR_Quartile,\n  Code_QR_High\n);",
       }   ,
   ]
,record_types:    [
       {
       name: "Box",
       qualified_name: "Bar_Codes.Box",
       signature: "bar_codes.box",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Box is record left, bottom, width, height : Real; end record;",
       }   ,
       {
       name: "Module_Box",
       qualified_name: "Bar_Codes.Module_Box",
       signature: "bar_codes.module_box",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Module_Box is record left, bottom, width, height : Natural; end record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Bar_Code",
       qualified_name: "Bar_Codes.Bar_Code",
       signature: "bar_codes.bar_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bar_Code is abstract tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Code_1D",
       qualified_name: "Bar_Codes.Code_1D",
       signature: "bar_codes.code_1d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Code_1D is Kind_Of_Code range Code_128 .. Code_128;",
       }   ,
       {
       name: "Code_2D",
       qualified_name: "Bar_Codes.Code_2D",
       signature: "bar_codes.code_2d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Code_2D is Code_QR;",
       }   ,
       {
       name: "Code_2D_Square",
       qualified_name: "Bar_Codes.Code_2D_Square",
       signature: "bar_codes.code_2d_square",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Code_2D_Square is Code_QR;",
       }   ,
       {
       name: "Code_QR",
       qualified_name: "Bar_Codes.Code_QR",
       signature: "bar_codes.code_qr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Code_QR is Kind_Of_Code range Code_QR_Low  .. Code_QR_High;",
       }   ,
   ]
,constants:    [
       {
       name: "reference",
       qualified_name: "Bar_Codes.reference",
       signature: "bar_codes.reference",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL ^",
       documentation_snippet: "reference : constant String := \"05-Jul-2018\";",
       }   ,
       {
       name: "title",
       qualified_name: "Bar_Codes.title",
       signature: "bar_codes.title",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL ^",
       documentation_snippet: "title     : constant String := \"Ada Bar Codes\";",
       }   ,
       {
       name: "version",
       qualified_name: "Bar_Codes.version",
       signature: "bar_codes.version",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL ^",
       documentation_snippet: "version   : constant String := \"002\";",
       }   ,
       {
       name: "web",
       qualified_name: "Bar_Codes.web",
       signature: "bar_codes.web",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at that URL ^",
       documentation_snippet: "web       : constant String := \"http://ada-bar-codes.sf.net/\";",
       }   ,
   ]
,}
---

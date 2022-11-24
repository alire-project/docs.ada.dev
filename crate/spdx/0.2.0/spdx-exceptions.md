---
crate: spdx
layout: gnatdoc
gnatdoc: {
name: "SPDX.Exceptions",
qualified_name: "SPDX.Exceptions",
signature: "spdx.exceptions",
enclosing: "spdx",
is_private: false,
documentation: "Genrated code",
documentation_snippet: "",
simple_types:    [
       {
       name: "Id",
       qualified_name: "SPDX.Exceptions.Id",
       signature: "spdx.exceptions.id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Id is (\n            GCC_exception_2_0,\n            openvpn_openssl_exception,\n            GPL_3_0_linking_exception,\n            Fawkes_Runtime_exception,\n            u_boot_exception_2_0,\n            PS_or_PDF_font_exception_20170817,\n            gnu_javamail_exception,\n            LGPL_3_0_linking_exception,\n            DigiRule_FOSS_exception,\n            LLVM_exception,\n            Linux_syscall_note,\n            GPL_3_0_linking_source_exception,\n            Qwt_exception_1_0,\n            Id_389_exception,\n            mif_exception,\n            eCos_exception_2_0,\n            CLISP_exception_2_0,\n            Bison_exception_2_2,\n            Libtool_exception,\n            LZMA_exception,\n            OpenJDK_assembly_exception_1_0,\n            Font_exception_2_0,\n            OCaml_LGPL_linking_exception,\n            GCC_exception_3_1,\n            Bootloader_exception,\n            SHL_2_0,\n            Classpath_exception_2_0,\n            Swift_exception,\n            Autoconf_exception_2_0,\n            FLTK_exception,\n            freertos_exception_2_0,\n            Universal_FOSS_exception_1_0,\n            WxWindows_exception_3_1,\n            OCCT_exception_1_0,\n            Autoconf_exception_3_0,\n            i2p_gpl_java_exception,\n            GPL_CC_1_0,\n            Qt_LGPL_exception_1_1,\n            SHL_2_1,\n            Qt_GPL_exception_1_0);",
       }   ,
   ]
,access_types:    [
       {
       name: "String_Access",
       qualified_name: "SPDX.Exceptions.String_Access",
       signature: "spdx.exceptions.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is not null access constant String;",
       }   ,
   ]
,constants:    [
       {
       name: "Img_Ptr",
       qualified_name: "SPDX.Exceptions.Img_Ptr",
       signature: "spdx.exceptions.img_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Img_Ptr : constant array (Id) of String_Access :=\n  (\n   GCC_exception_2_0 => new String'(\"GCC-exception-2.0\"),\n   openvpn_openssl_exception => new String'(\"openvpn-openssl-exception\"),\n   GPL_3_0_linking_exception => new String'(\"GPL-3.0-linking-exception\"),\n   Fawkes_Runtime_exception => new String'(\"Fawkes-Runtime-exception\"),\n   u_boot_exception_2_0 => new String'(\"u-boot-exception-2.0\"),\n   PS_or_PDF_font_exception_20170817 => new String'(\"PS-or-PDF-font-exception-20170817\"),\n   gnu_javamail_exception => new String'(\"gnu-javamail-exception\"),\n   LGPL_3_0_linking_exception => new String'(\"LGPL-3.0-linking-exception\"),\n   DigiRule_FOSS_exception => new String'(\"DigiRule-FOSS-exception\"),\n   LLVM_exception => new String'(\"LLVM-exception\"),\n   Linux_syscall_note => new String'(\"Linux-syscall-note\"),\n   GPL_3_0_linking_source_exception => new String'(\"GPL-3.0-linking-source-exception\"),\n   Qwt_exception_1_0 => new String'(\"Qwt-exception-1.0\"),\n   Id_389_exception => new String'(\"389-exception\"),\n   mif_exception => new String'(\"mif-exception\"),\n   eCos_exception_2_0 => new String'(\"eCos-exception-2.0\"),\n   CLISP_exception_2_0 => new String'(\"CLISP-exception-2.0\"),\n   Bison_exception_2_2 => new String'(\"Bison-exception-2.2\"),\n   Libtool_exception => new String'(\"Libtool-exception\"),\n   LZMA_exception => new String'(\"LZMA-exception\"),\n   OpenJDK_assembly_exception_1_0 => new String'(\"OpenJDK-assembly-exception-1.0\"),\n   Font_exception_2_0 => new String'(\"Font-exception-2.0\"),\n   OCaml_LGPL_linking_exception => new String'(\"OCaml-LGPL-linking-exception\"),\n   GCC_exception_3_1 => new String'(\"GCC-exception-3.1\"),\n   Bootloader_exception => new String'(\"Bootloader-exception\"),\n   SHL_2_0 => new String'(\"SHL-2.0\"),\n   Classpath_exception_2_0 => new String'(\"Classpath-exception-2.0\"),\n   Swift_exception => new String'(\"Swift-exception\"),\n   Autoconf_exception_2_0 => new String'(\"Autoconf-exception-2.0\"),\n   FLTK_exception => new String'(\"FLTK-exception\"),\n   freertos_exception_2_0 => new String'(\"freertos-exception-2.0\"),\n   Universal_FOSS_exception_1_0 => new String'(\"Universal-FOSS-exception-1.0\"),\n   WxWindows_exception_3_1 => new String'(\"WxWindows-exception-3.1\"),\n   OCCT_exception_1_0 => new String'(\"OCCT-exception-1.0\"),\n   Autoconf_exception_3_0 => new String'(\"Autoconf-exception-3.0\"),\n   i2p_gpl_java_exception => new String'(\"i2p-gpl-java-exception\"),\n   GPL_CC_1_0 => new String'(\"GPL-CC-1.0\"),\n   Qt_LGPL_exception_1_1 => new String'(\"Qt-LGPL-exception-1.1\"),\n   SHL_2_1 => new String'(\"SHL-2.1\"),\n   Qt_GPL_exception_1_0 => new String'(\"Qt-GPL-exception-1.0\"));",
       }   ,
       {
       name: "Name_Ptr",
       qualified_name: "SPDX.Exceptions.Name_Ptr",
       signature: "spdx.exceptions.name_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Name_Ptr : constant array (Id) of String_Access :=\n  (\n   GCC_exception_2_0 => new String'(\"GCC Runtime Library exception 2.0\"),\n   openvpn_openssl_exception => new String'(\"OpenVPN OpenSSL Exception\"),\n   GPL_3_0_linking_exception => new String'(\"GPL-3.0 Linking Exception\"),\n   Fawkes_Runtime_exception => new String'(\"Fawkes Runtime Exception\"),\n   u_boot_exception_2_0 => new String'(\"U-Boot exception 2.0\"),\n   PS_or_PDF_font_exception_20170817 => new String'(\"PS/PDF font exception (2017-08-17)\"),\n   gnu_javamail_exception => new String'(\"GNU JavaMail exception\"),\n   LGPL_3_0_linking_exception => new String'(\"LGPL-3.0 Linking Exception\"),\n   DigiRule_FOSS_exception => new String'(\"DigiRule FOSS License Exception\"),\n   LLVM_exception => new String'(\"LLVM Exception\"),\n   Linux_syscall_note => new String'(\"Linux Syscall Note\"),\n   GPL_3_0_linking_source_exception => new String'(\"GPL-3.0 Linking Exception (with Corresponding Source)\"),\n   Qwt_exception_1_0 => new String'(\"Qwt exception 1.0\"),\n   Id_389_exception => new String'(\"389 Directory Server Exception\"),\n   mif_exception => new String'(\"Macros and Inline Functions Exception\"),\n   eCos_exception_2_0 => new String'(\"eCos exception 2.0\"),\n   CLISP_exception_2_0 => new String'(\"CLISP exception 2.0\"),\n   Bison_exception_2_2 => new String'(\"Bison exception 2.2\"),\n   Libtool_exception => new String'(\"Libtool Exception\"),\n   LZMA_exception => new String'(\"LZMA exception\"),\n   OpenJDK_assembly_exception_1_0 => new String'(\"OpenJDK Assembly exception 1.0\"),\n   Font_exception_2_0 => new String'(\"Font exception 2.0\"),\n   OCaml_LGPL_linking_exception => new String'(\"OCaml LGPL Linking Exception\"),\n   GCC_exception_3_1 => new String'(\"GCC Runtime Library exception 3.1\"),\n   Bootloader_exception => new String'(\"Bootloader Distribution Exception\"),\n   SHL_2_0 => new String'(\"Solderpad Hardware License v2.0\"),\n   Classpath_exception_2_0 => new String'(\"Classpath exception 2.0\"),\n   Swift_exception => new String'(\"Swift Exception\"),\n   Autoconf_exception_2_0 => new String'(\"Autoconf exception 2.0\"),\n   FLTK_exception => new String'(\"FLTK exception\"),\n   freertos_exception_2_0 => new String'(\"FreeRTOS Exception 2.0\"),\n   Universal_FOSS_exception_1_0 => new String'(\"Universal FOSS Exception, Version 1.0\"),\n   WxWindows_exception_3_1 => new String'(\"WxWindows Library Exception 3.1\"),\n   OCCT_exception_1_0 => new String'(\"Open CASCADE Exception 1.0\"),\n   Autoconf_exception_3_0 => new String'(\"Autoconf exception 3.0\"),\n   i2p_gpl_java_exception => new String'(\"i2p GPL+Java Exception\"),\n   GPL_CC_1_0 => new String'(\"GPL Cooperation Commitment 1.0\"),\n   Qt_LGPL_exception_1_1 => new String'(\"Qt LGPL exception 1.1\"),\n   SHL_2_1 => new String'(\"Solderpad Hardware License v2.1\"),\n   Qt_GPL_exception_1_0 => new String'(\"Qt GPL exception 1.0\"));",
       }   ,
       {
       name: "Version",
       qualified_name: "SPDX.Exceptions.Version",
       signature: "spdx.exceptions.version",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Version : constant String :=\"3.10-14-g0fb8a59\";",
       }   ,
   ]
,}
---

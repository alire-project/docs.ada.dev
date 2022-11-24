---
layout: gnatdoc_error
crate: utilada_unit
version: 2.5.0
---
```
<GenericPackageInstantiation ["Ahven.AStrings"] ahven-astrings.ads:19:1-20:74>
<GenericPackageInstantiation ["Ahven.Long_AStrings"] ahven-long_astrings.ads:19:1-20:79>
<ExceptionDecl ["Invalid_Parameter"] ahven-parameters.ads:21:4-21:34>
<ExceptionDecl ["Invalid_Cursor"] ahven-slist.ads:27:4-27:31>
<ExceptionDecl ["List_Full"] ahven-slist.ads:29:4-29:26>
<GenericSubpDecl ["For_Each"] ahven-slist.ads:59:4-61:39>
<ExceptionDecl ["Temporary_File_Error"] ahven-temporary_output.ads:20:4-20:37>
<ExceptionDecl ["Assertion_Error"] ahven.ads:23:4-23:32>
<ExceptionDecl ["Test_Skipped_Error"] ahven.ads:26:4-26:35>
<GenericSubpDecl ["Assert_Equal"] ahven.ads:33:4-38:47>
<GenericSubpDecl ["Assert_Equals_T"] util-assertions.ads:26:4-33:78>
<GenericSubpDecl ["Harness"] util-tests.ads:165:4-169:41>
<ExceptionDecl ["Assertion_Error"] util-xunit.ads:32:4-32:62>
<IncompleteTypeDecl ["Test_Object"] util-xunit.ads:42:4-42:21>
<GenericSubpDecl ["Harness"] util-xunit.ads:105:4-110:44>

raised CONSTRAINT_ERROR : GNATdoc.Entities.Entity_Information_Maps.Constant_Reference: key not in map
ERROR: Command ["gnatdoc4", "-P", ".alire/unit/utilada_unit.gpr", "--output-dir", "/home/chouteau/src/github/alire/docs.ada.dev/crate/utilada_unit/2.5.0", "--front-matter", "crate: utilada_unit", "--no-subprojects"] exited with code 1

```

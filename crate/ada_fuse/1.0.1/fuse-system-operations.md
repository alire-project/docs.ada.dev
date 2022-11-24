---
crate: ada_fuse
layout: gnatdoc
gnatdoc: {
name: "Operations",
qualified_name: "Fuse.System.Operations",
signature: "fuse.system.operations",
enclosing: "fuse.system",
is_private: false,
documentation: "Operations\n\n@formal GetAttr_C_Type\n@formal ReadLink_C_Type\n@formal MkNod_C_Type\n@formal MkDir_C_Type\n@formal Unlink_C_Type\n@formal RmDir_C_Type\n@formal SymLink_C_Type\n@formal Rename_C_Type\n@formal Link_C_Type\n@formal ChMod_C_Type\n@formal ChOwn_C_Type\n@formal Truncate_C_Type\n@formal UTime_C_Type\n@formal Open_C_Type\n@formal Read_C_Type\n@formal Write_C_Type\n@formal StatFS_C_Type\n@formal Flush_C_Type\n@formal Release_C_Type\n@formal FSync_C_Type\n@formal SetXAttr_C_Type\n@formal GetXAttr_C_Type\n@formal ListXAttr_C_Type\n@formal RemoveXAttr_C_Type\n@formal OpenDir_C_Type\n@formal ReadDir_C_Type\n@formal ReleaseDir_C_Type\n@formal FSyncDir_C_Type\n@formal Init_C_Type\n@formal Destroy_C_Type\n@formal Access_C_Type\n@formal Create_C_Type\n@formal FTruncate_C_Type\n@formal FGetAttr_C_Type\n  type Lock_C_Type is private;\n  type UTimeNS_C_Type is private;\n  type BMap_C_Type is private;\n  type IOCtl_C_Type is private;\n  type Poll_C_Type is private;",
documentation_snippet: "",
record_types:    [
       {
       name: "Operations_C_Record",
       qualified_name: "Fuse.System.Operations.Operations_C_Record",
       signature: "fuse.system.operations.operations_c_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operations_C_Record is\n   record\n      GetAttr_C     : GetAttr_C_Type;\n      Readlink_C    : Readlink_C_Type;\n      Mknod_C       : Mknod_C_Type;\n      Mkdir_C       : Mkdir_C_Type;\n      Unlink_C      : Unlink_C_Type;\n      RmDir_C       : RmDir_C_Type;\n      Symlink_C     : Symlink_C_Type;\n      Rename_C      : Rename_C_Type;\n      Link_C        : Link_C_Type;\n      Chmod_C       : Chmod_C_Type;\n      Chown_C       : Chown_C_Type;\n      Truncate_C    : Truncate_C_Type;\n      Utime_C       : Utime_C_Type;\n      Open_C        : Open_C_Type;\n      Read_C        : Read_C_Type;\n      Write_C       : Write_C_Type;\n      Statfs_C      : Statfs_C_Type;\n      Flush_C       : Flush_C_Type;\n      Release_C     : Release_C_Type;\n      Fsync_C       : Fsync_C_Type;\n      Setxattr_C    : Setxattr_C_Type;\n      Getxattr_C    : Getxattr_C_Type;\n      Listxattr_C   : Listxattr_C_Type;\n      Removexattr_C : Removexattr_C_Type;\n      OpenDir_C     : OpenDir_C_Type;\n      ReadDir_C     : ReadDir_C_Type;\n      ReleaseDir_C  : ReleaseDir_C_Type;\n      FSyncDir_C    : FSyncDir_C_Type;\n      Init_C        : Init_C_Type;\n      Destroy_C     : Destroy_C_Type;\n      Access_C      : Access_C_Type;\n      Create_C      : Create_C_Type;\n      FTruncate_C   : FTruncate_C_Type;\n      FGetAttr_C    : FGetAttr_C_Type;\n      Flag_Nullpath_Ok : Boolean;\n   end record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Operations_C_Access",
       qualified_name: "Fuse.System.Operations.Operations_C_Access",
       signature: "fuse.system.operations.operations_c_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operations_C_Access is access all Operations_C_Record;",
       }   ,
   ]
,}
---

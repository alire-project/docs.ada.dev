---
crate: keystoreada
layout: gnatdoc
gnatdoc: {
name: "Keystore.Passwords.GPG",
qualified_name: "Keystore.Passwords.GPG",
signature: "keystore.passwords.gpg",
enclosing: "keystore.passwords",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Context_Type",
       qualified_name: "Keystore.Passwords.GPG.Context_Type",
       signature: "keystore.passwords.gpg.context_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context_Type is limited new Ada.Finalization.Limited_Controlled\n  and Slot_Provider and Keys.Key_Provider with private;",
       }   ,
   ]
,constants:    [
       {
       name: "DECRYPT_COMMAND",
       qualified_name: "Keystore.Passwords.GPG.DECRYPT_COMMAND",
       signature: "keystore.passwords.gpg.decrypt_command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DECRYPT_COMMAND : constant String := \"gpg --decrypt --batch --yes --quiet\";",
       }   ,
       {
       name: "ENCRYPT_COMMAND",
       qualified_name: "Keystore.Passwords.GPG.ENCRYPT_COMMAND",
       signature: "keystore.passwords.gpg.encrypt_command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ENCRYPT_COMMAND : constant String := \"gpg --encrypt --batch --yes -r $USER\";",
       }   ,
       {
       name: "LIST_COMMAND",
       qualified_name: "Keystore.Passwords.GPG.LIST_COMMAND",
       signature: "keystore.passwords.gpg.list_command",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "LIST_COMMAND    : constant String := \"gpg --list-secret-keys --with-colons --with-fingerprint\";",
       }   ,
       {
       name: "MAX_ENCRYPT_SIZE",
       qualified_name: "Keystore.Passwords.GPG.MAX_ENCRYPT_SIZE",
       signature: "keystore.passwords.gpg.max_encrypt_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_ENCRYPT_SIZE : constant := 1024;",
       }   ,
   ]
,}
---

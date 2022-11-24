---
layout: crate
crate: "sparknacl"
authors: ["Rod Chapman"]
maintainers: ["Rod Chapman <rod@proteancode.com>"]
licenses: ["BSD-3-Clause"]
websites: ["https://github.com/rod-chapman/SPARKNaCl"]
tags: ["spark",
"cryptography",
"security",
"nacl",
"curve25519",
"ed25519",
"tweetnacl"]
version: "3.0.0"
short_description: "Verified SPARK 2014 re-implementation of TweetNaCl cryptographic library"
dependencies: [{crate: "gnat", version: ">=11.2.1"}]
configuration_variables: []
configuration_values: []

---
SPARK 2014 re-implementation of TweetNaCl cryptographic library, with fully automated proofs of type safety and some correctness properties


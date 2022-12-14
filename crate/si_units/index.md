---
layout: crate
crate: "si_units"
authors: ["Vinzent \"Jellix\" Saranen"]
maintainers: ["vinzent@heisenbug.eu"]
licenses: ["WTFPL"]
websites: ["https://github.heisenbug.eu/si_units"]
tags: ["utilities",
"formatting"]
version: "0.2.0"
short_description: "Pretty print physical values in properly scaled metric (SI) units."
dependencies: []
configuration_variables: []
configuration_values: []

---
Provides generic conversion (`Image`) functions that convert values into human
readable strings with appropriate SI prefixes. This is especially convenient
when you have to deal with printing values from a potentially large interval,
and you need to represent such values as something an average human will
easily be able to read. Then you can use `SI_Units` to take care of the
conversion into an appropriate string representation for you.

Converting values into a string is supported with all SI prefixes which are a
power of 1000 (yocto .. Yotta), additionally there is a generic that can deal
with binary prefixes (i.e. prefixes that denote powers of 1024).

Scaling (i.e. conversion between different prefixes, like from kilo(meter) to
centi(meter)) between all defined SI prefixes is also supported, similar for
binary prefixes.

See the project's [website](https://github.heisenbug.eu/si_units) for more
details.

Version 0.2.0 is source code identical to the previous 0.1.3 release, but adds
full support for Alire integration. In the process, the provided `gnat` project
files have been streamlined, so if you upgrade to this version from a previous
release, you will need to adjust your own project files accordingly.



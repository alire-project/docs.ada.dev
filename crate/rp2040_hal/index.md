---
layout: crate
crate: "rp2040_hal"
authors: ["Jeremy Grosser"]
maintainers: ["Jeremy Grosser <jeremy@synack.me>"]
licenses: ["BSD-3-Clause"]
websites: ["https://pico-doc.synack.me/"]
tags: ["embedded",
"nostd",
"rp2040",
"raspberrypi",
"drivers"]
version: "2.0.0"
short_description: "Drivers and HAL for the RP2040 micro-controller family"
dependencies: [{crate: "atomic", version: "~0.4"},
{crate: "cortex_m", version: "~0.5"},
{crate: "gnat_arm_elf", version: "^12"},
{crate: "hal", version: "~0.3"},
{crate: "usb_embedded", version: "~0.3"}]
configuration_variables: [{name: 'Flash_Chip', type: 'Enum (w25qxx, generic_qspi, generic_03)', default: "w25qxx"},
{name: 'Interrupts', type: 'Enum (hal, bb_runtimes)', default: "hal"},
{name: 'Use_Startup', type: 'Boolean', default: "TRUE"}]
configuration_values: [{crate: 'atomic', settings: [{name: 'Backend', value: "armv6m"}]},
{crate: 'cortex_m', settings: [{name: 'core', value: "m0p"}]}]

---



---
crate: spawn
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Spawn",
    qualified_name: "Spawn",
    signature: "spawn",
    enclosing: "",
    is_private: false,
    documentation: "\nCopyright (C) 2018-2019, AdaCore\n\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Spawn.Environments",
    qualified_name: "Spawn.Environments",
    signature: "spawn.environments",
    enclosing: "spawn",
    is_private: false,
    documentation: "Notes about names of variables: its case sensitivity is platform dependent.\nOn case insensitive platforms original casing is returned by Keys function.",
    documentation_snippet: "",
    },
    {
    name: "Spawn.Environments.Internal",
    qualified_name: "Spawn.Environments.Internal",
    signature: "spawn.environments.internal",
    enclosing: "spawn.environments",
    is_private: false,
    documentation: "\nCopyright (C) 2018-2019, AdaCore\n\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Spawn.Posix",
    qualified_name: "Spawn.Posix",
    signature: "spawn.posix",
    enclosing: "spawn",
    is_private: false,
    documentation: "\nCopyright (C) 2018-2022, AdaCore\n\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Spawn.Processes",
    qualified_name: "Spawn.Processes",
    signature: "spawn.processes",
    enclosing: "spawn",
    is_private: false,
    documentation: "Asynchronous process control API with listener pattern",
    documentation_snippet: "",
    },
    {
    name: "Spawn.String_Vectors",
    qualified_name: "Spawn.String_Vectors",
    signature: "spawn.string_vectors",
    enclosing: "spawn",
    is_private: false,
    documentation: "\nCopyright (C) 2018-2019, AdaCore\n\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
]
, subprograms: [
    {
    name: "Spawn.Processes.Monitor_Loop",
    qualified_name: "Spawn.Processes.Monitor_Loop",
    signature: "spawn(standard.integer).processes(standard.integer).monitor_loop(standard.integer)",
    enclosing: "",
    is_private: false,
    documentation: "Drive process control engine, deliver events, watch child processes, etc.\n\nTimeout to run in milliseconds. Don't wait if zero. Wait forever if < 0.\nIf there are some events then procedure will return before timeout\nexpires.\n\nNote: This procedure is NOT thread-safe! In multi-tasking environment\ncreate a dedicated task to drive the engine.\n\nIn single task application you should call this to drive process engine.\n\nIn Glib enabled application the engine is integrated it the Glib event\nloop and this procedure shouldn't be used.\n\n@param Timeout",
    documentation_snippet: "procedure Spawn.Processes.Monitor_Loop (Timeout : Integer)",
    },
]
}
---

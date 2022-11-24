---
crate: spawn
layout: gnatdoc
gnatdoc: {
name: "Spawn.Processes.Monitor_Loop",
qualified_name: "Spawn.Processes.Monitor_Loop",
signature: "spawn(standard.integer).processes(standard.integer).monitor_loop(standard.integer)",
enclosing: "",
is_private: false,
documentation: "Drive process control engine, deliver events, watch child processes, etc.\n\nTimeout to run in milliseconds. Don't wait if zero. Wait forever if < 0.\nIf there are some events then procedure will return before timeout\nexpires.\n\nNote: This procedure is NOT thread-safe! In multi-tasking environment\ncreate a dedicated task to drive the engine.\n\nIn single task application you should call this to drive process engine.\n\nIn Glib enabled application the engine is integrated it the Glib event\nloop and this procedure shouldn't be used.\n\n@param Timeout",
documentation_snippet: "procedure Spawn.Processes.Monitor_Loop (Timeout : Integer)",
}
---

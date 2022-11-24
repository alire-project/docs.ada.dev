---
crate: spawn
layout: gnatdoc
gnatdoc: {
name: "Spawn.Processes",
qualified_name: "Spawn.Processes",
signature: "spawn.processes",
enclosing: "spawn",
is_private: false,
documentation: "Asynchronous process control API with listener pattern",
documentation_snippet: "",
simple_types:    [
       {
       name: "Process_Error",
       qualified_name: "Spawn.Processes.Process_Error",
       signature: "spawn.processes.process_error",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process_Error is (Failed_To_Start);",
       }   ,
       {
       name: "Process_Exit_Code",
       qualified_name: "Spawn.Processes.Process_Exit_Code",
       signature: "spawn.processes.process_exit_code",
       enclosing: "",
       is_private: false,
       documentation: "Exit status reported by the child process on normal exit.\nFor crash the meaning depends on the OS.",
       documentation_snippet: "type Process_Exit_Code is new Interfaces.Unsigned_32;",
       }   ,
       {
       name: "Process_Exit_Status",
       qualified_name: "Spawn.Processes.Process_Exit_Status",
       signature: "spawn.processes.process_exit_status",
       enclosing: "",
       is_private: false,
       documentation: "Process exit status\n@value Normal   The normal process termination case\n@value Crash    The abnormal process termination case\n\n@enum Normal\n@enum Crash",
       documentation_snippet: "type Process_Exit_Status is (Normal, Crash);",
       }   ,
       {
       name: "Process_Status",
       qualified_name: "Spawn.Processes.Process_Status",
       signature: "spawn.processes.process_status",
       enclosing: "",
       is_private: false,
       documentation: "Current process status.\n\n@value Not_Running  The process has not been started yet or has been\nexited/crashed already. Call Start to run it.\n\n@value Starting     The process is launching, but it isn't run yet.\n\n@value Running      The process is running.\n\n@enum Not_Running\n@enum Starting\n@enum Running",
       documentation_snippet: "type Process_Status is\n (Not_Running,\n  Starting,\n  Running);",
       }   ,
   ]
,interface_types:    [
       {
       name: "Process_Listener",
       qualified_name: "Spawn.Processes.Process_Listener",
       signature: "spawn.processes.process_listener",
       enclosing: "",
       is_private: false,
       documentation: "A process status event listener.",
       documentation_snippet: "type Process_Listener is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Process",
       qualified_name: "Spawn.Processes.Process",
       signature: "spawn.processes.process",
       enclosing: "",
       is_private: false,
       documentation: "The Process represents a running, exited, crashed or not-yet-running\nprocess.\n\nThe just created process has Not_Running status.\nIn this status Program, Arguments, Environment, Working_Directory and\nListener could be configured on the process. The Start call changes\nthe process status to Starting. Since then no configuration allowed.\nIf the OS is able to run corresponding program then the status becomes\nRunning and Started, Standard_Input_Available events are triggered on\nthe listener. Otherwise status becomes Not_Running and Error_Occurred\nevent is signaled.\nA running process keeps Running state till it crashes or exit normally,\nthen state becomes Not_Running and Finished event is triggered.\n\nNote: Make sure to keep Process object alive while it has Running\nstate. The suggested pattern is to keep it in the listener object.\nFinalization of the Process object in Running state result in wait\nfor termination of the child process or undefined behavior.\n\nThe running process has standard output and standard error streams to\nread from and standard input stream to write. Corresponding events\nnotify the listener when such calls are available.",
       documentation_snippet: "type Process is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Process_Listener_Access",
       qualified_name: "Spawn.Processes.Process_Listener_Access",
       signature: "spawn.processes.process_listener_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Process_Listener_Access is access all Process_Listener'Class;",
       }   ,
   ]
,}
---

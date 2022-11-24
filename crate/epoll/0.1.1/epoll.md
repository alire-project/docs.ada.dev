---
crate: epoll
layout: gnatdoc
gnatdoc: {
name: "Epoll",
qualified_name: "Epoll",
signature: "epoll",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Epoll_Descriptor",
       qualified_name: "Epoll.Epoll_Descriptor",
       signature: "epoll.epoll_descriptor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Epoll_Descriptor is private;",
       }   ,
       {
       name: "Epoll_Operation",
       qualified_name: "Epoll.Epoll_Operation",
       signature: "epoll.epoll_operation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Epoll_Operation is (Add, Delete, Modify)\n   with Size => 32;",
       }   ,
   ]
,array_types:    [
       {
       name: "Epoll_Events",
       qualified_name: "Epoll.Epoll_Events",
       signature: "epoll.epoll_events",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Epoll_Events is array (Integer range <>) of Epoll_Event\n   with Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Epoll_Event",
       qualified_name: "Epoll.Epoll_Event",
       signature: "epoll.epoll_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Epoll_Event is record\n   Flags : Epoll_Flags := (others => False);\n   Data  : Unsigned_64 := -1;\nend record\n   with Pack,\n        Convention => C_Pass_By_Copy;",
       }   ,
       {
       name: "Epoll_Flags",
       qualified_name: "Epoll.Epoll_Flags",
       signature: "epoll.epoll_flags",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Readable\n  EPOLLIN\n@field Writable\n  EPOLLOUT\n@field Peer_Shutdown\n  EPOLLRDHUP\n@field Out_Of_Band\n  EPOLLPRI\n@field Error\n  EPOLLERR\n@field Hang_Up\n  EPOLLHUP\n@field Edge_Triggered\n  EPOLLET\n@field One_Shot\n  EPOLLONESHOT\n@field Wake_Up\n  EPOLLWAKEUP\n@field Exclusive\n  EPOLLEXCLUSIVE",
       documentation_snippet: "type Epoll_Flags is record\n   Readable       : Boolean;\n   Writable       : Boolean;\n   Peer_Shutdown  : Boolean;\n   Out_Of_Band    : Boolean;\n   Error          : Boolean;\n   Hang_Up        : Boolean;\n   Edge_Triggered : Boolean;\n   One_Shot       : Boolean;\n   Wake_Up        : Boolean;\n   Exclusive      : Boolean;\nend record\n   with Size => 32;",
       }   ,
   ]
,}
---

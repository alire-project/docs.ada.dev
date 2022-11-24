---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.I2C",
qualified_name: "RP.I2C",
signature: "rp.i2c",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "I2C_Role",
       qualified_name: "RP.I2C.I2C_Role",
       signature: "rp.i2c.i2c_role",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Role is (Controller, Target);",
       }   ,
       {
       name: "I2C_Status",
       qualified_name: "RP.I2C.I2C_Status",
       signature: "rp.i2c.i2c_status",
       enclosing: "",
       is_private: false,
       documentation: "If a procedure sets Status to Error, the record returned by function\nState will provide more information useful for debugging.\n\n@enum Ok\n@enum Timeout\n@enum Error",
       documentation_snippet: "type I2C_Status is\n   (Ok, Timeout, Error);",
       }   ,
       {
       name: "Nanoseconds",
       qualified_name: "RP.I2C.Nanoseconds",
       signature: "rp.i2c.nanoseconds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Nanoseconds is new Natural;",
       }   ,
   ]
,record_types:    [
       {
       name: "I2C_Abort_Source",
       qualified_name: "RP.I2C.I2C_Abort_Source",
       signature: "rp.i2c.i2c_abort_source",
       enclosing: "",
       is_private: false,
       documentation: "\n@field No_Ack_Addr_7b\n  7 bit address unacknowledged\n@field No_Ack_Addr_10b_1\n  10 bit address unacknowledged (first byte)\n@field No_Ack_Addr_10b_2\n  10 bit address unacknowledged (second byte)\n@field No_Ack_Transmit\n  Upon controller transmit, the address was acknowledged, but a data byte was not.\n@field No_Ack_General_Call\n  No target acknowledged a general call\n@field Invalid_General_Call\n  General call command with read bit set\n@field Invalid_Ack_High_Speed\n  High speed mode was selected, but an ack was received before the end of the transfer.\n@field Invalid_Ack_Start\n  A start byte was acknowledged, but only data should be acknowledged.\n@field No_Restart_High_Speed\n  High speed mode was selected but restart is not enabled\n@field No_Restart_Start\n  Attempting to send a start byte but restart is not enabled\n@field No_Restart_10b_Read\n  10 bit read attempted but restart is not enabled\n@field Not_Controller_Mode\n  A controller operation was attempted while in target mode\n@field Arbitration_Lost\n  Something pulled SDA low before being addressed by the controller\n@field Target_Transmit_Abort\n  A target read command was issued while there was still data in the\n  transmit FIFO, transmit aborted.\n@field Target_Arbitration_Lost\n  Something pulled SDA to the wrong state while transmitting in target mode\n@field Invalid_Target_Read\n  The read bit was set in the CMD register during a target transmit\n@field Transfer_Aborted\n  User aborted a transfer in controller mode\n@field Transmit_Flush_Count",
       documentation_snippet: "type I2C_Abort_Source is record\n   No_Ack_Addr_7b          : Boolean := False;\n   No_Ack_Addr_10b_1       : Boolean := False;\n   No_Ack_Addr_10b_2       : Boolean := False;\n   No_Ack_Transmit         : Boolean := False;\n   No_Ack_General_Call     : Boolean := False;\n   Invalid_General_Call    : Boolean := False;\n   Invalid_Ack_High_Speed  : Boolean := False;\n   Invalid_Ack_Start       : Boolean := False;\n   No_Restart_High_Speed   : Boolean := False;\n   No_Restart_Start        : Boolean := False;\n   No_Restart_10b_Read     : Boolean := False;\n   Not_Controller_Mode     : Boolean := False;\n   Arbitration_Lost        : Boolean := False;\n   Target_Transmit_Abort   : Boolean := False;\n   Target_Arbitration_Lost : Boolean := False;\n   Invalid_Target_Read     : Boolean := False;\n   Transfer_Aborted        : Boolean := False;\n   Transmit_Flush_Count    : HAL.UInt9 := 0;\nend record\n   with Size => 32;",
       }   ,
       {
       name: "I2C_Config",
       qualified_name: "RP.I2C.I2C_Config",
       signature: "rp.i2c.i2c_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Config is record\n   Role   : I2C_Role := Controller;\n   Timing : I2C_Timing := Standard_Mode;\nend record;",
       }   ,
       {
       name: "I2C_State",
       qualified_name: "RP.I2C.I2C_State",
       signature: "rp.i2c.i2c_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_State is record\n   Abort_Source   : I2C_Abort_Source;\n   Last_Command   : RP2040_SVD.I2C.IC_DATA_CMD_Register;\n   RX_Remaining   : Natural;\n   TX_Remaining   : Natural;\n   TX_Empty       : Boolean;\n   RX_Empty       : Boolean;\n   Repeated_Start : Boolean;\n   Is_Error       : Boolean;\nend record;",
       }   ,
       {
       name: "I2C_Timing",
       qualified_name: "RP.I2C.I2C_Timing",
       signature: "rp.i2c.i2c_timing",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Timing is record\n   High, Low, Hold, Spike : Nanoseconds;\n   Rise, Fall : Nanoseconds := 0;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "I2C_Port",
       qualified_name: "RP.I2C.I2C_Port",
       signature: "rp.i2c.i2c_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Port\n   (Num    : I2C_Number;\n    Periph : not null access RP2040_SVD.I2C.I2C_Peripheral)\nis tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "I2C_Number",
       qualified_name: "RP.I2C.I2C_Number",
       signature: "rp.i2c.i2c_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype I2C_Number is Natural range 0 .. 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Fast_Mode",
       qualified_name: "RP.I2C.Fast_Mode",
       signature: "rp.i2c.fast_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fast_Mode      : constant I2C_Timing :=\n   (High   => 1_160,\n    Low    => 1_330,\n    Hold   => 800,\n    Spike  => 50,\n    others => <>);",
       }   ,
       {
       name: "Fast_Mode_Plus",
       qualified_name: "RP.I2C.Fast_Mode_Plus",
       signature: "rp.i2c.fast_mode_plus",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Fast_Mode_Plus : constant I2C_Timing :=\n   (High   => 400,\n    Low    => 600,\n    Hold   => 200,\n    Spike  => 50,\n    others => <>);",
       }   ,
       {
       name: "Standard_Mode",
       qualified_name: "RP.I2C.Standard_Mode",
       signature: "rp.i2c.standard_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Standard_Mode  : constant I2C_Timing :=\n   (High   => 5_200,\n    Low    => 4_700,\n    Hold   => 3_450,\n    others => <>);",
       }   ,
   ]
,}
---

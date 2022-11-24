---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "Bosch_BNO055",
qualified_name: "Bosch_BNO055",
signature: "bosch_bno055",
enclosing: "",
is_private: false,
documentation: "Give the supplied package for I2C-based communication (BNO055_I2C_IO),\nand a procedure for delaying a given number of milliseconds, one could\ninstantiate the package as follows (for example):\n\n    with BNO055_I2C_IO;  use BNO055_I2C_IO;\n    with HAL.I2C;        use HAL.I2C;\n\n    with Bosch_BNO055;\n    with Delay_Milliseconds;\n\n    package BNO055_I2C is new Bosch_BNO055\n      (IO_Port            => IO_Port,\n       Any_IO_Port        => Any_IO_Port,\n       Sensor_Data_Buffer => I2C_Data);\n\nIn the above we are specifying the generic actual types from the\nBNO055_I2C_IO package and the HAL.I2C package, in that order, and taking\nthe defaults for the generic formal I/O subprograms made visible via the\nuse-clause for the BNO055_I2C_IO package. Note that a USART-based\ninstantiation could look very similar; given similar naming only the\nfirst two lines would change.\n\nSimilarly, the with-clause on procedure Delay_Milliseconds makes a\nprocedure matching the formal subprogram's profile directly visible\n(and only one), so the default can be taken there as well.\n\n@formal IO_Port\n@formal Any_IO_Port\n@formal Read\n  Get the Value at the address specified in Register via This port.\n@formal Write\n  Write the Value to the address specified in Register via This port.\n@formal Sensor_Data_Buffer\n@formal Read_Buffer\n  Get the multiple Values at the address specified in Register via This\n  port.\n@formal Delay_Milliseconds\n  Issue a relative delay for Count milliseconds. This formal subprogram\n  removes the dependency on Ada.Real_Time so that this driver can be used\n  with runtimes that do not have that language-defined facility.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Acceleration_Units",
       qualified_name: "Bosch_BNO055.Acceleration_Units",
       signature: "bosch_bno055.acceleration_units",
       enclosing: "",
       is_private: false,
       documentation: "linear and gravity vector\n\n@enum Meters_Second_Squared\n@enum Milligravity",
       documentation_snippet: "type Acceleration_Units is (Meters_Second_Squared, Milligravity);",
       }   ,
       {
       name: "Angular_Rate_Units",
       qualified_name: "Bosch_BNO055.Angular_Rate_Units",
       signature: "bosch_bno055.angular_rate_units",
       enclosing: "",
       is_private: false,
       documentation: "for gyro\n\n@enum Degrees_Second\n@enum Radians_Second",
       documentation_snippet: "type Angular_Rate_Units is (Degrees_Second, Radians_Second);",
       }   ,
       {
       name: "Axis",
       qualified_name: "Bosch_BNO055.Axis",
       signature: "bosch_bno055.axis",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis is (X, Y, Z);",
       }   ,
       {
       name: "Axis_Remapping_Selections",
       qualified_name: "Bosch_BNO055.Axis_Remapping_Selections",
       signature: "bosch_bno055.axis_remapping_selections",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis_Remapping_Selections is (Remap_To_X, Remap_To_Y, Remap_To_Z)\n  with Size => 2;",
       }   ,
       {
       name: "Axis_Sign_Selections",
       qualified_name: "Bosch_BNO055.Axis_Sign_Selections",
       signature: "bosch_bno055.axis_sign_selections",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis_Sign_Selections is (Remap_To_Positive, Remap_To_Negative)\n  with Size => 2;",
       }   ,
       {
       name: "Euler_Angle_Units",
       qualified_name: "Bosch_BNO055.Euler_Angle_Units",
       signature: "bosch_bno055.euler_angle_units",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Euler_Angle_Units is (Degrees, Radians);",
       }   ,
       {
       name: "Operating_Modes",
       qualified_name: "Bosch_BNO055.Operating_Modes",
       signature: "bosch_bno055.operating_modes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Operating_Modes is\n  (Operating_Mode_Config,\n   Operating_Mode_Acc_Only,\n   Operating_Mode_Mag_Only,\n   Operating_Mode_Gyro_Only,\n   Operating_Mode_Acc_Mag,\n   Operating_Mode_Acc_Gyro,\n   Operating_Mode_Mag_Gyro,\n   Operating_Mode_AMG,\n   Operating_Mode_IMU,\n   Operating_Mode_Compass,\n   Operating_Mode_M4G,\n   Operating_Mode_NDOF_FMC_Off,\n   Operating_Mode_NDOF);",
       }   ,
       {
       name: "Pitch_Rotation_Conventions",
       qualified_name: "Bosch_BNO055.Pitch_Rotation_Conventions",
       signature: "bosch_bno055.pitch_rotation_conventions",
       enclosing: "",
       is_private: false,
       documentation: "See the Datasheet, Table 3-12, in section 3.6.2 \"Data output format\"\nin which \"Android\" and \"Windows\" are used for these possible values.\nNobody seems to know why they are used so we give them different names.\nClockwise_Increasing corresponds to \"Windows\" and Clockwise_Decreasing\ncorresponds to \"Android\" in that table. Clockwise_Increasing is the\ndefault on power-up.\n\nThe effect is only applied to Pitch angle values, as follows:\n  Clockwise_Increasing => -180 to +180 degrees\n  Clockwise_Decreasing => +180 to -180 degrees\n\n@enum Clockwise_Increasing\n@enum Clockwise_Decreasing",
       documentation_snippet: "type Pitch_Rotation_Conventions is (Clockwise_Increasing, Clockwise_Decreasing);",
       }   ,
       {
       name: "Power_Modes",
       qualified_name: "Bosch_BNO055.Power_Modes",
       signature: "bosch_bno055.power_modes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Power_Modes is\n  (Power_Mode_Normal,\n   Power_Mode_Lowpower,\n   Power_Mode_Suspend);",
       }   ,
       {
       name: "Sensor_Data_Kinds",
       qualified_name: "Bosch_BNO055.Sensor_Data_Kinds",
       signature: "bosch_bno055.sensor_data_kinds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sensor_Data_Kinds is\n  (Accelerometer_Data,\n   Magnetometer_Data,\n   Gyroscope_Data,\n   Euler_Orientation,\n   Linear_Acceleration_Data,\n   Gravity_Data);",
       }   ,
       {
       name: "Sensor_Id",
       qualified_name: "Bosch_BNO055.Sensor_Id",
       signature: "bosch_bno055.sensor_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sensor_Id is (Accelerometer, Gyroscope, Magnetometer);",
       }   ,
       {
       name: "System_Error_Values",
       qualified_name: "Bosch_BNO055.System_Error_Values",
       signature: "bosch_bno055.system_error_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type System_Error_Values is\n  (No_Error,\n   Peripheral_Initialization_Error,\n   System_Initialization_Error,\n   Self_Test_Result_Failed,\n   Register_Map_Value_Range_Error,\n   Register_Map_Address_Range_Error,\n   Register_Map_Write_Error,\n   BNO_Low_Power_Mode_Not_Available,\n   Accelerometer_Power_Mode_Not_Available,\n   Fusion_Algorithm_Configuration_Error,\n   Sensor_Configuration_Error)\n  with Size => 8;",
       }   ,
       {
       name: "System_Status_Values",
       qualified_name: "Bosch_BNO055.System_Status_Values",
       signature: "bosch_bno055.system_status_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type System_Status_Values is\n  (Idle,\n   System_Error,\n   Initializing_Peripherals,\n   System_Initalization,\n   Executing_Self_Test,\n   Sensor_Fusion_Algorithm_Running,\n   System_Running_Without_Fusion_Algorithms)\n  with Size => 8;",
       }   ,
       {
       name: "Temperature_Units",
       qualified_name: "Bosch_BNO055.Temperature_Units",
       signature: "bosch_bno055.temperature_units",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Temperature_Units is (Celsius, Fahrenheit);",
       }   ,
   ]
,array_types:    [
       {
       name: "Axes_Remapping",
       qualified_name: "Bosch_BNO055.Axes_Remapping",
       signature: "bosch_bno055.axes_remapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axes_Remapping is array (Axis) of Axis_Remapping_Selections;",
       }   ,
       {
       name: "Axes_Sign_Remapping",
       qualified_name: "Bosch_BNO055.Axes_Sign_Remapping",
       signature: "bosch_bno055.axes_sign_remapping",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axes_Sign_Remapping is array (Axis) of Axis_Sign_Selections;",
       }   ,
       {
       name: "Quaternion",
       qualified_name: "Bosch_BNO055.Quaternion",
       signature: "bosch_bno055.quaternion",
       enclosing: "",
       is_private: false,
       documentation: "W value is in the first indexed value\nX value is in the second indexed value\nY value is in the third indexed value\nZ value is in the fourth indexed value\n\nWe define this type here, rather than using the full Quaternions package\nand type, because this facility does not manipulate quaternions itself,\nit just provides the data. In addition, we use a numeric type for the\nindex so that this type will support direct conversion to the full\nQuaternion type without requiring UC or a user-defined function. An\nenumeration type for the index would not allow direct type conversion.",
       documentation_snippet: "type Quaternion is array (1 .. 4) of Float;",
       }   ,
       {
       name: "Sensor_Data",
       qualified_name: "Bosch_BNO055.Sensor_Data",
       signature: "bosch_bno055.sensor_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sensor_Data is array (Axis) of Float;",
       }   ,
       {
       name: "Sensors_Selection",
       qualified_name: "Bosch_BNO055.Sensors_Selection",
       signature: "bosch_bno055.sensors_selection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sensors_Selection is array (Positive range <>) of Sensor_Id;",
       }   ,
   ]
,record_types:    [
       {
       name: "Calibration_States",
       qualified_name: "Bosch_BNO055.Calibration_States",
       signature: "bosch_bno055.calibration_states",
       enclosing: "",
       is_private: false,
       documentation: "NB: The \"platform\" component (\"system\" in the Datasheet) can indicate\nthat the platform is (fully) calibrated, but that does not mean that\nall sensors are individually fully calibrated. We define function\nCalibration_Complete for determining the state based on the three\n(or fewer, if so selected) sensors.\n\n@field Platform\n@field Gyroscope\n@field Accelerometer\n@field Magnetometer",
       documentation_snippet: "type Calibration_States is record\n   Platform      : Calibration_Level;\n   Gyroscope     : Calibration_Level;\n   Accelerometer : Calibration_Level;\n   Magnetometer  : Calibration_Level;\nend record;",
       }   ,
       {
       name: "Revision_Information",
       qualified_name: "Bosch_BNO055.Revision_Information",
       signature: "bosch_bno055.revision_information",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Revision_Information is record\n   Accelerometer : UInt8;\n   Magnetometer  : UInt8;\n   Gyroscope     : UInt8;\n   Software      : UInt16;\n   Bootloader    : UInt8;\nend record;",
       }   ,
       {
       name: "Self_Test_Results",
       qualified_name: "Bosch_BNO055.Self_Test_Results",
       signature: "bosch_bno055.self_test_results",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Self_Test_Results is record\n   Accelerometer_Passed : Boolean;\n   Magnetometer_Passed  : Boolean;\n   Gyroscope_Passed     : Boolean;\n   MCU_Passed           : Boolean;\nend record\n  with Size => 8, Alignment => 1, Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "Sensor_Offset_Values",
       qualified_name: "Bosch_BNO055.Sensor_Offset_Values",
       signature: "bosch_bno055.sensor_offset_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sensor_Offset_Values is record\n   Accel_Offset_X : Integer_16;\n   Accel_Offset_Y : Integer_16;\n   Accel_Offset_Z : Integer_16;\n   Gyro_Offset_X  : Integer_16;\n   Gyro_Offset_Y  : Integer_16;\n   Gyro_Offset_Z  : Integer_16;\n   Mag_Offset_X   : Integer_16;\n   Mag_Offset_Y   : Integer_16;\n   Mag_Offset_Z   : Integer_16;\n   Accel_Radius   : Integer_16;\n   Mag_Radius     : Integer_16;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "BNO055_9DOF_IMU",
       qualified_name: "Bosch_BNO055.BNO055_9DOF_IMU",
       signature: "bosch_bno055.bno055_9dof_imu",
       enclosing: "",
       is_private: false,
       documentation: "The BNO055 is a System in Package (SiP) integrating a triaxial 14-bit\naccelerometer, a triaxial 16-bit gyroscope, a triaxial geomagnetic\nsensor and a 32-bit Cortex M0+ microcontroller running Bosch Sensortec\nsensor fusion software providing fused orientation data. The designated\nIO_Port is used to communicate with the sensor, and will be a concrete\ninstance of either an I2C port or a USART port.",
       documentation_snippet: "type BNO055_9DOF_IMU (Port : not null Any_IO_Port) is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Calibration_Level",
       qualified_name: "Bosch_BNO055.Calibration_Level",
       signature: "bosch_bno055.calibration_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Calibration_Level    is UInt8 range 0 .. 3;",
       }   ,
       {
       name: "Fully_Calibrated",
       qualified_name: "Bosch_BNO055.Fully_Calibrated",
       signature: "bosch_bno055.fully_calibrated",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Fully_Calibrated     is Calibration_Level range 3 .. 3;",
       }   ,
       {
       name: "Partially_Calibrated",
       qualified_name: "Bosch_BNO055.Partially_Calibrated",
       signature: "bosch_bno055.partially_calibrated",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Partially_Calibrated is Calibration_Level range 1 .. 2;",
       }   ,
       {
       name: "Temperature_Source",
       qualified_name: "Bosch_BNO055.Temperature_Source",
       signature: "bosch_bno055.temperature_source",
       enclosing: "",
       is_private: false,
       documentation: "The magnetometer's temperature is not available, per section 3.6.5.8\nof the Datasheet.",
       documentation_snippet: "subtype Temperature_Source is Sensor_Id\n  with Static_Predicate => Temperature_Source in Accelerometer | Gyroscope;",
       }   ,
       {
       name: "Uncalibrated",
       qualified_name: "Bosch_BNO055.Uncalibrated",
       signature: "bosch_bno055.uncalibrated",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Uncalibrated         is Calibration_Level range 0 .. 0;",
       }   ,
   ]
,constants:    [
       {
       name: "All_Sensors",
       qualified_name: "Bosch_BNO055.All_Sensors",
       signature: "bosch_bno055.all_sensors",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "All_Sensors : constant Sensors_Selection := (Accelerometer, Magnetometer, Gyroscope);",
       }   ,
       {
       name: "All_Tests_Passed",
       qualified_name: "Bosch_BNO055.All_Tests_Passed",
       signature: "bosch_bno055.all_tests_passed",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "All_Tests_Passed : constant Self_Test_Results := (others => True);",
       }   ,
       {
       name: "BNO055_Alternate_Address",
       qualified_name: "Bosch_BNO055.BNO055_Alternate_Address",
       signature: "bosch_bno055.bno055_alternate_address",
       enclosing: "",
       is_private: false,
       documentation: "shift left one bit since we're using 7-bit addresses.",
       documentation_snippet: "BNO055_Alternate_Address : constant I2C_Address := 16#29# * 2;",
       }   ,
       {
       name: "BNO055_Min_Sample_Interval",
       qualified_name: "Bosch_BNO055.BNO055_Min_Sample_Interval",
       signature: "bosch_bno055.bno055_min_sample_interval",
       enclosing: "",
       is_private: false,
       documentation: "According to the Datasheet, when using the internal oscillator the max\ndata rate is 100Hz for the data-fusion configurations. The AdaFruit\nbreakout has an external crystal available so this rate could be higher.\nSee Datasheet Table 0-2 in section 1.2, and especially Table 3-14 in\nsection 3.6.3. Rates for the Compass and M4G configurations are lower.\nThe procedure Configure has a parameter named Use_External_Crystal to\ncontrol that option.",
       documentation_snippet: "BNO055_Min_Sample_Interval : constant := 10;",
       }   ,
       {
       name: "BNO055_Primary_Address",
       qualified_name: "Bosch_BNO055.BNO055_Primary_Address",
       signature: "bosch_bno055.bno055_primary_address",
       enclosing: "",
       is_private: false,
       documentation: "shift left one bit since we're using 7-bit addresses.",
       documentation_snippet: "BNO055_Primary_Address   : constant I2C_Address := 16#28# * 2;",
       }   ,
       {
       name: "I_Am_BNO055",
       qualified_name: "Bosch_BNO055.I_Am_BNO055",
       signature: "bosch_bno055.i_am_bno055",
       enclosing: "",
       is_private: false,
       documentation: "The value expected to be returned from Device_Id",
       documentation_snippet: "I_Am_BNO055 : constant := 16#A0#;",
       }   ,
   ]
,}
---
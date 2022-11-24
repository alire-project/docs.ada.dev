---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PIO.Audio_I2S",
qualified_name: "RP.PIO.Audio_I2S",
signature: "rp.pio.audio_i2s",
enclosing: "rp.pio",
is_private: false,
documentation: "There is only one LRCLK signal, so any more than two channels will need\nsome external multiplexing logic.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "I2S_Device",
       qualified_name: "RP.PIO.Audio_I2S.I2S_Device",
       signature: "rp.pio.audio_i2s.i2s_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2S_Device\n   (Data        : not null access RP.GPIO.GPIO_Point;\n    BCLK        : not null access RP.GPIO.GPIO_Point;\n    LRCLK       : not null access RP.GPIO.GPIO_Point;\n    PIO         : not null access RP.PIO.PIO_Device'Class;\n    SM          : RP.PIO.PIO_SM;\n    Channels    : Channel_Count;\n    DMA_Channel : RP.DMA.DMA_Channel_Id;\n    Buffer_Size : Positive)\nis limited new HAL.Audio.Audio_Stream with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Channel_Count",
       qualified_name: "RP.PIO.Audio_I2S.Channel_Count",
       signature: "rp.pio.audio_i2s.channel_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Channel_Count is Positive range 1 .. 2;",
       }   ,
   ]
,}
---

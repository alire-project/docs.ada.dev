---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "ST7735R.RAM_Framebuffer",
qualified_name: "ST7735R.RAM_Framebuffer",
signature: "st7735r.ram_framebuffer",
enclosing: "st7735r",
is_private: false,
documentation: "This a buffered driver for the ST7735R LCD. Pixels are stored in RAM\nwhich means more memory consumption but also fast operations.\n\nPlease use ST7735R for a low memory foot print implementation.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "ST7735R_RAM_Framebuffer_Screen",
       qualified_name: "ST7735R.RAM_Framebuffer.ST7735R_RAM_Framebuffer_Screen",
       signature: "st7735r.ram_framebuffer.st7735r_ram_framebuffer_screen",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ST7735R_RAM_Framebuffer_Screen\n  (Port : not null Any_SPI_Port;\n   CS   : not null Any_GPIO_Point;\n   RS   : not null Any_GPIO_Point;\n   RST  : not null Any_GPIO_Point;\n   Time : not null HAL.Time.Any_Delays)\nis limited new Parent with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "ST7735R.RAM_Framebuffer.Parent",
       signature: "st7735r.ram_framebuffer.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is ST7735R_Screen;",
       }   ,
   ]
,}
---

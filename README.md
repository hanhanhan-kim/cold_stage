# How to make an insect cooling stage

**_N.B._ This project is a work-in-progress!**

I outline the steps for making a DIY insect cooling stage. Cold temperatures immobilize insects so they can be used for common downstream preparations in neurobiology experiments. Cooling stages provide a useful alternative to carbon dioxide-based methods, which result in physiological and behavioural side-effects on the insect. In addition, a cheap and easy to assemble cooling stage may prove useful for those who wish to do some preliminary experimentation from home, during the ongoing COVID-19 crisis. 

Peter Weir's [excellent blog post](https://ptweir.github.io/flyBridge/) inspired this project, but I decided I didn't want to spend money on a fancy temperature controller like [TE Tech's TC-48-20](https://tetech.com/product/tc-48-20/). Below, I detail my amateur efforts on making a closed-loop temperature controller for an insect cooling stage. I thank [Will Dickson](https://github.com/willdickson) for hardware recommendations and for general troubleshooting and control systems advice—in particular for suggesting a proportional control scheme with a feedforward term. 

## Materials

In addition to the usual hobby electronics tools and consumables—jumper wires, breadboard, multimeter, etc.—I use the following parts:

- [Teensy 3.2 microcontroller](https://www.pjrc.com/store/teensy32.html) 
- [VNH5019 DC motor driver](https://www.pololu.com/product/1451)   
- [Waterproof DS18B20 temperature sensor](https://www.amazon.com/gp/product/B01LY53CED/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1) and a 4.7 kOhm resistor
- [Air-cooled Peltier module](https://www.adafruit.com/product/1335) [(recommended in Peter's blog)](https://ptweir.github.io/flyBridge/)
- [12 V power supply rated for at least 6 A](https://www.amazon.com/gp/product/B07M981HSV/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

## Circuit

Connect the DC motor driver to the Teensy as specified in the below schematic from Pololu:

![VNH5019 hookup example from Pololu](docs/VNH5019_hookup.jpg)

One of the many reasons the Teensy is great is because it has tons of digital and PWM pins—way more than the Arduino Nano, which despite having a similar form factor, is limited in its pin selections. 





 




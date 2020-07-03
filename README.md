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

Connect the DC motor driver to the Teensy as specified in the below schematic from Pololu. Note that the GNDs for the motor and logic powers are common:

![VNH5019 hookup example from Pololu](docs/VNH5019_hookup.jpg)

Then connect the DS18B20 temperature sensor. Place the 4.7 kOhm resistor in parallel with the sensor's signal and VCC lines. Connect the sensor's signal wire to any digital pin on the Teensy, its GND to the common GND, and its VCC to the common logic VCC. See [this blog post](https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806) for more details. 

Our circuit wiring might look something like this:

![VNH5019 hookup example from Pololu](docs/full_circuit_hookup.jpg)

Don't fret if your wiring doesn't look exactly like the photo above. So long as the digital wires go to the digital pins, GND goes to GND, VCC goes to VCC, and PWM goes to PWM, you should be set. 

## Firmware

If you want to get your cooling stage going right away, simply upload this sketch to your Teensy and call it a day! Simply edit the line specifying the setpoint temperature (C), `const float setpointC = 17;`, to whatever you fancy—probably something like `4`. If you're interested in a little bit of the troubleshooting and validation I went through to arrive at the recommended firmware, continuing reading this section. 

<!-- One of the many reasons the Teensy is great is because it has tons of digital and PWM pins—way more than the Arduino Nano, which despite having a similar form factor, provides less generous pin options.  -->





 




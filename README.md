# How to make an insect cooling stage

---

_N.B._ This project is currently a work-in-progress!

---

I outline the steps for making a DIY insect cooling stage. Cooling stages are necessary for immobilizing insects so they can be used for downstream preparations common in neurobiology experiments. These stages provide a useful alternative to carbon dioxide-based methods, which result in physiological and behavioural side-effects on the insect. In addition, a cheap and easy to assemble cooling stage may prove useful for those who wish to do some preliminary experimentation from home, during the ongoing COVID-19 crisis. 

Peter Weir's [excellent blog post](https://ptweir.github.io/flyBridge/) inspired this project, but I decided I didn't want to spend money on a fancy temperature controller like [TE Tech's TC-48-20](https://tetech.com/product/tc-48-20/). Below, I detail my amateur efforts on making a closed-loop temperature controller for an insect cooling stage. I use a Teensy 3.2 microcontroller, a DC motor driver, a waterproof DS18B20 temperature sensor, and the air-cooled Peltier module [recommended by Peter's blog](https://ptweir.github.io/flyBridge/). I thank [Will Dickson](https://github.com/willdickson) for hardware recommendations and for suggesting a proportional control scheme with a feedforward term, instead of a bang-bang or PID control system. 

 




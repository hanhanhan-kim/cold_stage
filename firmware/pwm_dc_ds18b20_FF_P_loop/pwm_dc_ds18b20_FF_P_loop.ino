#include <OneWire.h>
#include <DallasTemperature.h>

// Define DC motor pins:
#define enableInputA 3
#define enableInputB 7
#define PWMoutput 5

// Define DS18B20 signal pin:
#define oneWireBus 9

// Define initial Peltier PWM value and desired setpoint in oC:
int PWMValue = 255;
const float setpointC = 17;
const float gainP = 2;


// Set up a oneWire instance to communicate with any OneWire devices
// and not just Maxim / Dallas temperature ICs:
OneWire oneWire(oneWireBus); 

// Pass our oneWire reference to Dallas Temperature:
DallasTemperature sensors(&oneWire);

void setup() {
  
  // Set InputA, InputB, and PWM pins as OUTPUTs:
  pinMode(enableInputA, OUTPUT);
  pinMode(enableInputB, OUTPUT);
  pinMode(PWMoutput, OUTPUT);

  // Set PWM freequency to 20 kHz: 
  analogWriteFrequency(PWMoutput, 20000);
  // Set PWM bit res to 8-bits:
  analogWriteResolution(8);
  // Set PWM duty cycle here between 0 and 255 (2**8):
  analogWrite(PWMoutput, PWMValue);
  
  Serial.begin(115200);

  // Delete if not debugging:
  Serial.println("DallasTemperature IC control library demo");

  // Start up the library:
  sensors.begin();
  
}

void loop() {

  // Set polarity across the Peltier leads:
  digitalWrite(enableInputA, LOW);
  digitalWrite(enableInputB, HIGH);

  // Delete if not debugging:
  Serial.print(" Requesting temperatures ...");

  // This fxn issues a global temperature request to ALL devices
  // on the bus:
  sensors.requestTemperatures();
  // Delete if not debugging:
  Serial.println(" Done!");

  // Get the temp from the first (0th) IC on the bus:
  Serial.print(sensors.getTempCByIndex(0));

  // Compute ff with P control:
  float ff = feedforward(setpointC);
  float error = setpointC - sensors.getTempCByIndex(0);
  float PWMValue = ff - gainP * error;

  // Set PWM pin to our new PWM value:
  analogWrite(PWMoutput, PWMValue);
  
  // Delete if not debugging:
  delay(1000);
  
}

// My feedforward function for initializing the PWM value:
float feedforward(float setpointC){
  float pwmValue;
  pwmValue = -10.44 * setpointC + 243.16;
  return pwmValue;
}

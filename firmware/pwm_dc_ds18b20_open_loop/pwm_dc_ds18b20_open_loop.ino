#include <OneWire.h>
#include <DallasTemperature.h>

// Define DC motor pins:
#define enableInputA 3
#define enableInputB 7
#define pwmPin 5

// Define DS18B20 signal pin:
#define oneWireBus 9

// Set up a oneWire instance to communicate with any OneWire devices
// and not just Maxim / Dallas temperature ICs:
OneWire oneWire(oneWireBus); 

// Pass our oneWire reference to Dallas Temperature:
DallasTemperature sensors(&oneWire);

void setup() {
  
  // Set InputA, InputB, and PWM pins as OUTPUTs:
  pinMode(enableInputA, OUTPUT);
  pinMode(enableInputB, OUTPUT);
  pinMode(pwmPin, OUTPUT);

  // Set PWM freequency to 20 kHz: 
  analogWriteFrequency(pwmPin, 20000);
  // Set PWM bit res to 8-bits:
  analogWriteResolution(8);
  // Set PWM duty cycle here between 0 and 255 (2**8):
  analogWrite(pwmPin, 255);
  
  Serial.begin(115200);

  // Start up the library:
  sensors.begin();
  
}

void loop() {

  // Set polarity across the Peltier leads:
  digitalWrite(enableInputA, LOW);
  digitalWrite(enableInputB, HIGH);

  // This fxn issues a global temperature request to ALL devices
  // on the bus:
  sensors.requestTemperatures();

  // Get the temp from the first (0th) IC on the bus:
  Serial.print(sensors.getTempCByIndex(0));

  // Delete if not debugging:
  delay(1000);
  
}

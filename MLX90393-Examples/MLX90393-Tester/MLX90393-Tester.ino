/*
  MLX90393 Magnetometer Example Code
  By: Nathan Seidle
  SparkFun Electronics
  Date: February 6th, 2017
  License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

  Wait for user to press button. Turn on LED if board responded correctly.

  Hardware Connections (Breakoutboard to Arduino):
  3.3V = 3.3V
  GND = GND
  SDA = A4
  SCL = A5

  Serial.print it out at 9600 baud to serial monitor.
*/

#include <Wire.h>
#include <MLX90393.h> //From https://github.com/tedyapo/arduino-MLX90393 by Theodore Yapo

MLX90393 mlx;
MLX90393::txyz data; //Create a structure, called data, of four floats (t, x, y, and z)

#define LED 7
#define BUTTON 8

void setup()
{
  Serial.begin(9600);
  Serial.println("MLX90393 Test");

  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
  pinMode(BUTTON, INPUT_PULLUP);
}

void loop()
{
  Serial.println("Waiting for user to press button");
  while (digitalRead(BUTTON) == HIGH) delay(1); // Wait for button to be pressed

  digitalWrite(LED, LOW); //Indicate start of test

  mlx.begin(); //Assumes I2C jumpers are GND. No DRDY pin used.

  byte response = mlx.readData(data); //Read the values from the sensor
  if (response == 0x00)
  {
    Serial.print("Sensor GOOD");
    Serial.print(" magX[");
    Serial.print(data.x);
    Serial.print("] magY[");
    Serial.print(data.y);
    Serial.print("] magZ[");
    Serial.print(data.z);
    Serial.print("] temperature(C)[");
    Serial.print(data.t);
    Serial.print("]");

    digitalWrite(LED, HIGH);
  }
  else
  {
    Serial.print("FAIL!");

    Serial.print(" Start response: 0x");
    if (response < 0x10) Serial.print("0"); //Pretty output
    Serial.println(response, HEX);

    digitalWrite(LED, LOW);
  }

  Serial.println();

  while (digitalRead(BUTTON) == LOW) delay(1); //Wait for user to stop pressing button
}

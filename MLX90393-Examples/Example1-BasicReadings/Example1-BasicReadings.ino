/*
  MLX90393 Magnetometer Example Code
  By: Nathan Seidle
  SparkFun Electronics
  Date: February 6th, 2017
  License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

  Read the mag fields on three XYZ axis

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

char user_input;

void setup()
{
  Serial.begin(9600);
  //sensor1: A0 = 0, A1 = 0; sensor2: A0 = 0, A1 = 1
  mlx.begin(); //Assumes I2C jumpers are GND. No DRDY pin used.
}

void loop()
{
  while (Serial.available()) {
    user_input = Serial.read(); //Read user input and trigger appropriate function
    if (user_input == '1')
    {
      delay(100);
      mlx.changeaddr(0,0);
      delay(1);
      Serial.flush();
      delay(1000);
    }
    else if (user_input == '2')
    {
      delay(100);
      mlx.changeaddr(0,1);
      delay(1);
      Serial.flush();
      delay(1000);
    }
    else
    {
      Serial.println("Invalid option entered.");
    }
  }

  mlx.readData(data); //Read the values from the sensor
  Serial.print(data.z);
  Serial.print("\n");

  //  Serial.println();

  delay(1);
}

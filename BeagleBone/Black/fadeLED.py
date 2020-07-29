#!/usr/bin/python3
#//////////////////////////////////////
# 	fadeLED.py
#   Fades the LED wired to P1_36 using the PWM.
# 	Wiring:	P1_36 connects to the plus lead of an LED.  The negative lead of the
# 			LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
# 			to 3.3V (P1_14).
#//////////////////////////////////////
import Adafruit_BBIO.PWM as PWM
import time
LED = 'P1_36'
step = 10       # Step size
min =  0        # dimmest value
max =  100      # brightest value
brightness = min # Current brightness;
 
PWM.start(LED, brightness)

while True:
    PWM.set_duty_cycle(LED, brightness)
    brightness += step
    if(brightness >= max or brightness <= min):
        step = -1 * step
    time.sleep(0.04)

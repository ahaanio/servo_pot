from machine import PWM, Pin, ADC
import time

servo = PWM(Pin(17))
servo.freq(50)
pot = ADC(Pin(28))

def servo_control(degree):
    if degree > 180:
        degree = 180
    if degree < 0:
        degree = 0
        
    maxDuty = 9000
    minDuty = 1000
    
    newDuty = minDuty + (maxDuty - minDuty) * (degree/180)
    servo.duty_u16(int(newDuty))
    
while True:
    value = pot.read_u16()
    degree = value*180/65500
    servo_control(degree)
    time.sleep(0.05)


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) #This will use BCM pin numbering

LED_PIN = 24 #this will set pin 18 as our output
GPIO.setup(LED_PIN, GPIO.OUT)

startup_timer=10

while startup_timer>0:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
    startup_timer-=1

GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(60)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()

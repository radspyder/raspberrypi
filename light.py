import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #This will use BCM pin numbering

LED_PIN = 24 #this will set pin 18 as our output
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)
print("LED ON!")
time.sleep(5)
GPIO.output(LED_PIN, GPIO.LOW)
print("LED OFF!")
time.sleep(1)

GPIO.cleanup()

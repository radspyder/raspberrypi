from gpiozero import Button
from signal import pause

# Connect button to GPIO 24 and GND
button = Button(24)
state="off"

def button_pressed():
    global state
    if state=="off":
        print("starting program")
        state="on"
    elif state=="on":
        print("stopping program")
        state="off"

def button_released():
    print("Button was released!")

# Assign functions to events
button.when_pressed = button_pressed

pause() # Keeps the program running

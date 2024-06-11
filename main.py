# Program simulating a door lock system with arduino esp32 with micropython
# By Tim Nilsson and Calle Larsen

import machine
import time
from servo import Servo

# Define hardware pins for buttons
button_one = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
button_two = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)
button_three = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
button_four = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
button_five = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

# Setup servo trough servo library
motor = Servo(pin=10)

# Define hardware pins for led diods
led_red = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
led_yellow = machine.Pin(12, machine.Pin.OUT)

# Initiate starting values
led_red.value(1)
led_green.value(0)
led_yellow.value(0)

current_button_value = 0
prev_button_value = 0

prev_debounce_time = 0

correct_code = [1, 1, 1, 1]
pressed_buttons = []
motor.move(0)

is_green_light_on = False
time_opened = time.ticks_ms()

is_in_reset_mode = False
is_reset_permitted = False


# Function to check which button, if any, has been pressed
def get_new_button_value():
    new_button_value = 0

    if button_one.value() == 0:
        new_button_value = 1
    
    if button_two.value() == 0:
        new_button_value = 2
    
    if button_three.value() == 0:
        new_button_value = 3
    
    if button_four.value() == 0:
        new_button_value = 4

    if button_five.value() == 0:
        new_button_value = 5

    return new_button_value


# Function to simulate opening of the door
def open_door():
    print("Opening door")
    pressed_buttons.clear()
    led_red.value(0)
    led_green.value(1)
    motor.move(180)


# Function to simulate closing of the door
def close_door():
    print("Closing door")
    motor.move(0)
    led_green.value(0)
    led_red.value(1)


# Function to push a given value into the list
def add_to_pressed_buttons(new_value):
    # If list is full, remove first value and push new value at the end of the list
    if len(pressed_buttons) == 4:
        pressed_buttons.pop(0)
        pressed_buttons.append(new_value)
        print(pressed_buttons)
    else:
        pressed_buttons.append(new_value)
        print(pressed_buttons)


while True:

    # If door is open, close door if five seconds have passed
    if is_green_light_on == True and time.ticks_ms() - time_opened > 5000:
        close_door()
        is_green_light_on = False
  
    new_button_value = get_new_button_value()

    # Update recorded time if button value differs from previous button value
    if new_button_value != prev_button_value:
        prev_debounce_time = time.ticks_ms()

    # React only if long enough time has passed since two different button values
    if time.ticks_ms() - prev_debounce_time > 20 and new_button_value != current_button_value and is_green_light_on == False:
      
        current_button_value = new_button_value

        # Sets device in reset mode if fifth button is pressed
        if new_button_value == 5 and is_in_reset_mode == False:
            print("Enter current code: ")
            is_in_reset_mode = True
            pressed_buttons.clear()
            led_yellow.value(1)

        # Update list of pressed button depending on which button is pressed
        if new_button_value == 1:
            add_to_pressed_buttons(1)

        if new_button_value == 2:
            add_to_pressed_buttons(2)

        if new_button_value == 3:
            add_to_pressed_buttons(3)

        if new_button_value == 4:
            add_to_pressed_buttons(4)

        # Change code if in reset mode and four new numbers has been entered
        if is_in_reset_mode == True and is_reset_permitted == True and len(pressed_buttons) == 4:
            correct_code = pressed_buttons.copy()
            pressed_buttons.clear()
            is_in_reset_mode = False
            led_yellow.value(0)
            led_red.value(1)
            led_green.value(0)
            print("Code reset")
            is_reset_permitted = False
        # When user has entered correct code after pressing fifth button
        elif is_in_reset_mode == True and pressed_buttons == correct_code:
            print("Enter new code: ")
            pressed_buttons.clear()
            is_reset_permitted = True
            led_red.value(0)
            led_green.value(1)
        elif pressed_buttons == correct_code:
            open_door()
            is_green_light_on = True
            time_opened = time.ticks_ms()
    
    prev_button_value = new_button_value

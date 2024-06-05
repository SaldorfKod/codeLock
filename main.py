import machine
import time
from servo import Servo

button_one = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
button_two = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
button_three = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
button_four = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)
motor = Servo(pin=9)

led_red = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)

led_red.value(1)
led_green.value(0)

current_button_value = 0
prev_button_value = 0

prev_debounce_time = 0

correct_code = [1, 1, 1, 1]
pressed_buttons = []
motor.move(0)

is_green_light_on = False
time_opened = time.ticks_ms()

def open_door():
  print("Opening door")
  pressed_buttons.clear()
  led_red.value(0)
  led_green.value(1)
  motor.move(180)

def close_door():
  print("closing door")
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

    if is_green_light_on == True:
      if time.ticks_ms() - time_opened > 5000:
        close_door()
        is_green_light_on = False
  
    new_button_value = 0

    if button_one.value() == 0:
        new_button_value = 1
    
    if button_two.value() == 0:
        new_button_value = 2
    
    if button_three.value() == 0:
        new_button_value = 3
    
    if button_four.value() == 0:
        new_button_value = 4
    
    if new_button_value != prev_button_value:
        prev_debounce_time = time.ticks_ms()
    
    if time.ticks_ms() - prev_debounce_time > 20 and new_button_value != current_button_value:
        current_button_value = new_button_value

        if new_button_value == 1:
            print("Button one is pressed")
            add_to_pressed_buttons(1)

        if new_button_value == 2:
            print("Button two is pressed")
            add_to_pressed_buttons(2)

        if new_button_value == 3:
            print("Button three is pressed")
            add_to_pressed_buttons(3)

        if new_button_value == 4:
            print("Button four is pressed")
            add_to_pressed_buttons(4)

        if pressed_buttons == correct_code:
          open_door()
          is_green_light_on = True
          time_opened = time.ticks_ms()
    
    prev_button_value = new_button_value
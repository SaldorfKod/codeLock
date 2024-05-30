import machine
import time


button_one_sensor = machine.Pin(47, machine.Pin.IN, machine.Pin.PULL_UP)
red_sensor = machine.Pin(05, machine.Pin.OUT)
green_sensor = machine.Pin(07, machine.Pin.OUT)

correct_code = [1, 1, 1, 1]
pressed_buttons = []

# Function to push a given value into the list
def add_to_pressed_buttons(new_value):
  # If list is full, remove first value and push new value at the end of the list
  if len(pressed_buttons) == 4:
    pressed_buttons.pop(0)
    pressed_buttons.append(new_value)
  else:
    pressed_buttons.append(new_value)

# Turn red light on
red_sensor.value(1)
while True:

  current_button_value = button_one_sensor.value()
  if current_button_value == 0:
    add_to_pressed_buttons(1)
    print("Your list is now:")
    print(pressed_buttons)
    
    if len(pressed_buttons) == 4 and pressed_buttons == correct_code:
      red_sensor.value(0)
      green_sensor.value(1)
      time.sleep(3)
      green_sensor.value(0)
      red_sensor.value(1)
  time.sleep(0.3)

# while True:

  # new_value = 0

  # if button_one_sensor is pressed:
    # set new_value to one
  # if button_two_sensor is pressed:
    # set new_value to two

  # if list has four elements
    # remove first element in list
    # add new_value to list
    # if pressed_buttons list is identical to correct_code list
      # turn red light off
      # turn green light on
      # wait five seconds
      # turn green light off
      # turn red light on
  # else
    # add new_value to list


# Tests that led lights up when button is pressed
# while True:
#   first = button_one_sensor.value()
#   print(first)
#   if first == 0:
#     red_sensor.value(1)
#     green_sensor.value(1)
#   else:
#     red_sensor.value(0)
#     green_sensor.value(0)
#   time.sleep(1)
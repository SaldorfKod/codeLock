import machine
import time


button_one_sensor = machine.Pin(47, machine.Pin.IN, machine.Pin.PULL_UP)
red_sensor = machine.Pin(05, machine.Pin.OUT)
green_sensor = machine.Pin(06, machine.Pin.OUT)

correct_code = [1, 1, 1, 1]
pressed_buttons = []

# Turn red light on

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
while True:
  first = button_one_sensor.value()
  print(first)
  if first == 0:
    red_sensor.value(1)
    green_sensor.value(1)
  else:
    red_sensor.value(0)
    green_sensor.value(0)
  time.sleep(1)
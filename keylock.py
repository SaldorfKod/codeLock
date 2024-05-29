import machine
import time


button_sensor = machine.Pin(47, machine.Pin.IN, machine.Pin.PULL_UP)
red_sensor = machine.Pin(05, machine.Pin.OUT)
yellow_sensor = machine.Pin(06, machine.Pin.OUT)
print('Hello, MicroPython!')

while True:
  first = button_sensor.value()
  print(first)
  if first == 0:
    red_sensor.value(1)
    yellow_sensor.value(1)
  else:
    red_sensor.value(0)
    yellow_sensor.value(0)
  time.sleep(1)
# Write your code here :-)
from microbit import *
name = "Mia"
while True:
    if button_a.is_pressed():
        display.scroll("Hello ")
        display.scroll(name)
        sleep(1000)
    if button_b.is_pressed():
        display.scroll('Hello', delay=500, wait=True, loop=False, monospace=False)
        display.scroll(name, delay=500, wait=True, loop=False, monospace=False)
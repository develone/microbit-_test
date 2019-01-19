from microbit import *

compass.calibrate()

tardiscompass = 0

while True:
    if button_b.is_pressed():
        tardiscompass = compass.heading()
        if tardiscompass >= 210:
            display.scroll("Lower")
        elif tardiscompass <= 190:
            display.scroll("Higher")
    if button_a.is_pressed():
        tardiscompass = compass.heading()
    if 190 < tardiscompass < 210:
        display.scroll("TARDIS")
    else:
        display.scroll("?")
        
            
import hal.hal_input_switch as switch
import hal.hal_led as led
import time
switch.init()
led.init()

while(1 == 1):
    if switch.read_slide_switch() == 1:
        led.set_output(1,1)
        time.sleep(0.1)
        led.set_output(1, 0)
        time.sleep(0.1)
        
    else:
        count = 0
        while count <= 50:
            led.set_output(1,1)
            time.sleep(0.05)
            led.set_output(1, 0)
            time.sleep(0.05)
            count += 1
        led.set_output(1,0)
        quit()
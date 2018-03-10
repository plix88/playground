from time import sleep
import signal, sys, MPR121, switchLight1.py

try:
    sensor = MPR121.begin()
except Exception as e:
    print e
    sys.exit(1)

# this is the touch threshold - setting it low makes it more like a proximity trigger default value is 40 for touch
touch_threshold = 40

# this is the release threshold - must ALWAYS be smaller than the touch threshold default value is 20 for touch
release_threshold = 20

# set the thresholds
sensor.set_touch_threshold(touch_threshold)
sensor.set_release_threshold(release_threshold)


# handle ctrl+c gracefully
def signal_handler(signal, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

switchState = 'false'

while True:
    if sensor.touch_status_changed():
        sensor.update_touch_data()
        for i in range(12):
            if sensor.is_new_touch(i):
                if switchState == 'false':
                    switchState = 'true'
                    switchLight1.switch(switchState)

                if switchState == 'true':
                    switchState = 'false'
                    switchLight1.switch(switchState)
                    
                print "electrode {0} was just touched".format(i)
            elif sensor.is_new_release(i):
                print "electrode {0} was just released".format(i)

    sleep(0.01)

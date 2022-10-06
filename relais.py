import time
import gpiozero

RELAY_PIN = 19

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

relay.on()
time.sleep(5)
relay.off()


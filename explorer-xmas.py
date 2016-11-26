import explorerhat as eh
from time import sleep

try:
    while True:
        print("Lights on")
        eh.output.one.on()
        sleep(5)
        print("Lights off")
        eh.output.one.off()
        sleep(1)
        print("Lights blink")
        eh.output.one.blink(0.5,0.5)
        sleep(5)
        print("Lights pulse")
        eh.output.one.pulse(1,1,0.5,0.5)
        sleep(5)
except KeyboardInterrupt:
	print("Exit")
	eh.output.one.off()

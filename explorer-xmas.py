import explorerhat as eh
from time import sleep

try:
    while True:
        eh.output.one.on()
        sleep(5)
        eh.output.one.off()
        sleep(1)
        eh.output.one.blink(0.5,0.5)
        sleep(5)
        eh.output.one.pulse(1,1,0.5,0.5)
except KeyboardInterrupt:
	print("Exit")
	eh.output.one.off()

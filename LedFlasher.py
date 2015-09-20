# Simple led flasher for pyopy-mini
led = pyb.LED(1)
while True:
	led.on()
	pyb.delay(500)
	led.off()
	pyb.delay(500)
  

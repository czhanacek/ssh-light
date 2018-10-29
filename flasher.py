import RPi.GPIO as GPIO
import time
class EmitsLight():
    self.status = 0
    def off(): raise NotImplementedError

    def on(): raise NotImplementedError

    def status(): raise NotImplementedError

class Flashable():
    def flash(): raise NotImplementedError
    

class LED_Light(EmitsLight, Flashable):
    def __init__(self, status=0, pin=2):
        self.status = status
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)


    def status(self):
        return self.status

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.status = 0

    
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.status = 1

    def flash(self):
        self.on()
        time.sleep(0.5)
        self.off()
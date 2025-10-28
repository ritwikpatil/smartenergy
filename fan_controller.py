
import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

class FanController:
    def __init__(self, pin, off_delay=10):
        self.pin = pin
        self.off_delay = off_delay
        self.fan_on = False
        self.last_seen = 0
        if GPIO:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        if not self.fan_on:
            print("🌀 Fan ON")
            if GPIO: GPIO.output(self.pin, GPIO.HIGH)
            self.fan_on = True

    def turn_off(self):
        if self.fan_on and time.time() - self.last_seen > self.off_delay:
            print("💤 Fan OFF (No activity)")
            if GPIO: GPIO.output(self.pin, GPIO.LOW)
            self.fan_on = False

    def update_last_seen(self):
        self.last_seen = time.time()


import random

class TemperatureSensor:
    def __init__(self, threshold=28):
        self.threshold = threshold

    def read_temp(self):
        # Simulated temperature read
        temp = 25 + random.random() * 10
        print(f"🌡️ Temperature: {temp:.2f}°C")
        return temp

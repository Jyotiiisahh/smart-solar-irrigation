class Pump:
    def __init__(self):
        self.status = "OFF"
        
    def turn_on(self):
        self.status = "ON"
        
    def turn_off(self):
        self.status = "OFF"
class SolarPanel:
    def __init__(self, efficiency):
        self.efficiency = efficiency
        
    def generate_power(self, sunlight):
        return sunlight*self.efficiency
class TemperatureConverter:
    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def to_fahrenheit(self):
        if self.unit == 'C':
            return (self.temperature * 9/5) + 32
        elif self.unit == 'K':
            return (self.temperature - 273.15) * 9/5 + 32
        else:
            return self.temperature

    def to_celsius(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        elif self.unit == 'K':
            return self.temperature - 273.15
        else:
            return self.temperature

    def to_kelvin(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9 + 273.15
        elif self.unit == 'C':
            return self.temperature + 273.15
        else:
            return self.temperature

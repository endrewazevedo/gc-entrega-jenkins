import pytest
from main import TemperatureConverter

# use pytest.mark.parametrize to test multiple cases
@pytest.mark.parametrize("temp, unit, expected", [
    (0, 'C', 32), # Celsius to Fahrenheit
    (0, 'K', -459.66999999999996), # Kelvin to Fahrenheit
    (32, 'F', 32), # Fahrenheit to Fahrenheit
])
def test_to_fahrenheit(temp, unit, expected):
    # use plain assert instead of self.assertEqual
    tc = TemperatureConverter(temp, unit)
    assert tc.to_fahrenheit() == expected

@pytest.mark.parametrize("temp, unit, expected", [
    (32, 'F', 0), # Fahrenheit to Celsius
    (0, 'K', -273.15), # Kelvin to Celsius
    (0, 'C', 0), # Celsius to Celsius
])
def test_to_celsius(temp, unit, expected):
    tc = TemperatureConverter(temp, unit)
    assert tc.to_celsius() == expected

@pytest.mark.parametrize("temp, unit, expected", [
    (32, 'F', 273.15), # Fahrenheit to Kelvin
    (0, 'C', 273.15), # Celsius to Kelvin
    (0, 'K', 0), # Kelvin to Kelvin
])
def test_to_kelvin(temp, unit, expected):
    tc = TemperatureConverter(temp, unit)
    assert tc.to_kelvin() == expected

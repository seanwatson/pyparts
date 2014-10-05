class PartBin(object):

  def __init__(self, platform):
    self._platform = platform

  def get_rgb_led(self, red_pin, green_pin, blue_pin)
    from parts.led import rgb_led
    red = platform.get_pwm_output(red_pin)
    green = platform.get_pwm_output(green_pin)
    blue = platform.get_pwm_output(blue_pin)
    return rgb_led.RGBLed(red, green, blue) 

  def get_max31855(self, port, device):
    from parts.sensor.temperature import max31855
    spi = self._platform.get_hardware_spi_bus(port, device)
    return max31855.MAX31855(spi)

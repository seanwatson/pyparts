from component.led import rgb_led


class Components(object):

  def __init__(self, platform):
    self._platform = platform

  def get_rgb_led(self, red_pin, green_pin, blue_pin)
    red = platform.get_pwm_output(red_pin)
    green = platform.get_pwm_output(green_pin)
    blue = platform.get_pwm_output(blue_pin)
    return rgb_led.RGBLed(red, green, blue) 

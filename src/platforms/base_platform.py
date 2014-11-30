class BasePlatform(object):
  """An abstract class for creating platforms.

  BasePlatform is what all platforms are created from. Platforms are expected
  to override the methods of BasePlatform to provide different kinds of
  peripheral devices like GPIO pins, PWM pins, and communication busses.
  Platforms should only implement the methods for peripheral types supported
  by the platform.
  """

  def get_digital_input(self, pin):
    raise NotImplementedError

  def get_digital_output(self, pin):
    raise NotImplementedError

  def get_pwm_output(self, pin):
    raise NotImplementedError

  def get_hardware_spi_bus(self, port, device):
    raise NotImplementedError

  def get_software_spi_bus(self, sclk_pin, mosi_pin, miso_pin, ss_pin):
    raise NotImplementedError

  def get_i2c_bus(self):
    raise NotImplementedError

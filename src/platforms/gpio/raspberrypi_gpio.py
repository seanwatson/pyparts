import RPi.GPIO as rpi_gpio

from platforms.gpio import base_gpio


class RaspberryPiGPIO(base_gpio.BaseGPIO):
  """Raspberry Pi implementation of a GPIO peripheral."""

  def __init__(self, pin, mode):
    """Creates a GPIO pin for a Raspberry Pi.

    Args:
      pin: Integer. The pin number to create the GPIO on.
      mode: INPUT or OUTPUT. The pin mode to put the GPIO in.
    """
    super(RaspberryPiGPIO, self).__init__(pin, mode)
    
    if self._mode == base_gpio.INPUT:
      pin_type = rpi_gpio.IN
    else:
      pin_type = rpi_gpio.OUT

    rpi_gpio.setup(self._pin, pin_type)
    
  def _write(self, value):
    """Writes a value to the pin.

    Args:
      value: HIGH or LOW. The value to write to the pin.
    """
    rpi_gpio.output(self.pin, value)

  def _read(self):
    """Reads the current value from the pin.

    Returns:
      The GPIO pin's current value as HIGH or LOW.
    """
    return rpi_gpio.input(self.pin)


def RaspberryPiDigitalInput(RaspberryPiGPIO):
  """Raspberry Pi implementation of a DigitalInput."""

  def __init__(self, pin):
    super(RaspberryPiDigitalInput, self).__init__(pin, base_gpio.INPUT)


def RaspberryPiDigitalOutput(RaspberryPiGPIO):
  """Raspberry Pi implementation of a DigitalOutput."""

  def __init__(self, pin):
    super(RaspberryPiDigitalInput, self).__init__(pin, base_gpio.OUTPUT)

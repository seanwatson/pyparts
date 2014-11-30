import RPi.GPIO as rpi_gpio

from pyparts.platforms.gpio import base_gpio


class RaspberryPiGPIO(base_gpio.BaseGPIO):
  """Raspberry Pi implementation of a GPIO peripheral."""

  PUD_UP = rpi_gpio.PUD_UP
  PUD_DOWN = rpi_gpio.PUD_DOWN

  def __init__(self, pin, mode, pull_up_down=rpi_gpio.PUD_UP):
    """Creates a GPIO pin for a Raspberry Pi.

    Args:
      pin: Integer. The pin number to create the GPIO on.
      mode: INPUT or OUTPUT. The pin mode to put the GPIO in.
    """
    super(RaspberryPiGPIO, self).__init__(pin, mode, pull_up_down)
    
    if self._mode == base_gpio.INPUT:
      pin_type = rpi_gpio.IN
    else:
      pin_type = rpi_gpio.OUT

    rpi_gpio.setup(self._pin, pin_type, pull_up_down=pull_up_down)
    
  def _write(self, value):
    """Writes a value to the pin.

    Args:
      value: HIGH or LOW. The value to write to the pin.
    """
    rpi_gpio.output(self._pin, value)

  def _read(self):
    """Reads the current value from the pin.

    Returns:
      The GPIO pin's current value as HIGH or LOW.
    """
    return rpi_gpio.input(self._pin)


class RaspberryPiDigitalInput(base_gpio.BaseDigitalInput, RaspberryPiGPIO):
  """Raspberry Pi implementation of a DigitalInput."""

  INTERRUPT_FALLING = rpi_gpio.FALLING
  INTERRUPT_RISING = rpi_gpio.RISING
  INTERRUPT_BOTH = rpi_gpio.BOTH

  def __init__(self, pin):
    super(RaspberryPiDigitalInput, self).__init__(pin, base_gpio.INPUT)

  def add_interrupt(self, type, callback=None, debounce_time_ms=0):
    rpi_gpio.add_event_detect(self._pin, type, callback, debounce_time_ms)

  def wait_for_edge(self, type):
    rpi_gpio.wait_for_edge(self._pin, type)

  def remove_interrupt(self):
    rpi_gpio.remove_event_detection(self._pin)


class RaspberryPiDigitalOutput(RaspberryPiGPIO):
  """Raspberry Pi implementation of a DigitalOutput."""

  def __init__(self, pin):
    super(RaspberryPiDigitalOutput, self).__init__(pin, base_gpio.OUTPUT)

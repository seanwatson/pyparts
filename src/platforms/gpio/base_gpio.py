# Pin modes
OUTPUT = 0
INPUT = 1
BIDIRECTIONAL = 2

# Pin values
HIGH = True
LOW = False


class GPIOError(Exception):
  """Error type for exceptions while writing to GPIO pins."""
  pass


class BaseGPIO(object):
  """A class for creating GPIO type peripherals.

  BaseGPIO implements basic GPIO functionality such as reading pin values
  and setting pins high or low. Platforms are expected to subclass BaseGPIO
  and provide platform specific implementations of _write and _read. Platforms
  will likely also have to override the constructor to do platform specific
  initialization tasks like setting the pin to INPUT or OUTPUT.
  
  Attributes:
    _pin: The GPIO pin being used. For example a pin number.
    _mode: The mode the pin is in. For example INPUT or OUTPUT.
  """

  def __init__(self, pin, mode):
    """Creates a GPIO pin.

    Args:
      pin: The pin to create the GPIO on.
      mode: The type of pin mode to use.
    """
    self._pin = pin
    self._mode = mode

  def _write(self, value):
    """Writes a value to the pin.

    This method should be implemented by the platform.

    Args:
      value: The value to write to the pin.
    """
    raise NotImplementedError

  def _read(self):
    """Reads the current value of a pin.

    This method should be implemented by the platform.

    Returns:
      The GPIO pin's current value as HIGH or LOW.
    """
    raise NotImplementedError

  def get_pin_number(self):
    """Gets the pin number of the GPIO.

    Returns:
      The GPIO's pin number.
    """
    return self._pin

  def get_mode(self):
    """Gets the mode the GPIO pin is in.

    Returns:
      The mode being used by the GPIO pin.
    """
    return self._mode

  def set_high(self):
    """Writes a value of HIGH to the GPIO pin.

    Raises:
      GPIOError: Trying to write to a pin in INPUT mode will throw an
        exception.
    """
    if self._mode == INPUT:
      raise GPIOError('Failed to write pin %d high. Pin %d is an input.'
                      % (self._pin, self._pin))
    self._write(HIGH)

  def is_high(self):
    """Checks if the GPIO pin has a value of HIGH.

    Returns:
      True if the pin is in a HIGH state, False otherwise.
    """
    return self._read() == HIGH

  def set_low(self):
    """Writes a value of LOW to the GPIO pin.

    Raises:
      GPIOError: Trying to write to a pin in INPUT mode will throw an
        exception.
    """
    if self._mode == INPUT:
      raise GPIOError('Failed to write pin %d low. Pin %d is an input.'
                      % (self._pin, self._pin))
    self._write(LOW)

  def is_low(self):
    """Checks if the GPIO pin has a value of LOW.

    Returns:
      True if the GPIO pin is in a LOW state, False otherwise.
    return self._read() == LOW

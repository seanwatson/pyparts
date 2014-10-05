OUTPUT = 0
INPUT = 1
BIDIRECTIONAL = 2

HIGH = True
LOW = False


class GPIOError(Exception):
  pass


class BaseGPIO(object):

  def __init__(self, pin, mode):
    self._pin = pin
    self._mode = mode

  def _write(self, value):
    raise NotImplementedError

  def _read(self):
    raise NotImplementedError

  def get_pin_number(self):
    return self._pin

  def get_mode(self):
    return self._mode

  def set_high(self):
    if self._mode == INPUT:
      raise GPIOError('Failed to write pin %d high. Pin %d is an input.'
                      % (self._pin, self._pin))
    self._write(HIGH)

  def is_high(self):
    return self._read() == HIGH

  def set_low(self):
    if self._mode == INPUT:
      raise GPIOError('Failed to write pin %d low. Pin %d is an input.'
                      % (self._pin, self._pin))
    self._write(LOW)

  def is_low(self):
    return self._read() == LOW

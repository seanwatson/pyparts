MSB_FIRST = 0
LSB_FIRST = 1


class BaseSPIBus(object):

  def __init__(self):
    self._is_open = False
    self._clock_frequency = 0.0
    self._mode = 0
    self._bit_order = MSB_FIRST

  def _open(self):
    raise NotImplementedError

  def _close(self):
    raise NotImplementedError

  def _set_clock_frequency(self, frequency_hz):
    raise NotImplementedError

  def _set_mode(self, mode)
    raise NotImplementedError

  def _set_bit_order(self, order):
    raise NotImplementedError

  def open(self):
    self.open()
    self._is_open = True

  def close(self):
    self._close()
    self._is_open = False

  def is_open(self):
    return self._is_open

  def set_clock_frequency(self, frequency_hz):
    if frequency_hz < 0:
      raise ValueError('Frequency must be greater than 0. Got %g'
                       % (frequency_hz))
    self._set_clock_frequency(frequency_hz)
    self._clock_frequency = frequency_hz

  def get_clock_frequency(self):
    return self._clock_frequency

  def set_mode(self, mode):
    if mode < 0 or mode > 3:
      raise ValueError('Mode must be between 0 and 3. Got %d' % mode)
    self._set_mode(mode)
    self._mode = mode

  def get_mode(self, mode):
    return self._mode

  def set_bit_order(self, order):
    if order not in (MSB_FIRST, LSB_FIRST):
      raise ValueError('Bit order must be MSB_FIRST or LSB_FIRST')
    self._set_bit_order(order)
    self._bit_order = order

  def write(self, data):
    raise NotImplementedError

  def read(self, length):
    raise NotImplementedError


class BaseHardwareSPIBus(BaseSPIBus):

  def __init__(self, port, device):
    super(BaseHardwareSPIBus, self).__init__()
    self._port = port
    self._device = device

  def get_port(self):
    return self._port

  def get_device(self):
    return self._device

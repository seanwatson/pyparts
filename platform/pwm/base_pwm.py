class BasePWM(object):

  def __init__(self, output_pin):
    self._enabled = False
    self._output_pin = output_pin
    self._duty_cycle = 0.0
    self._frequency_hz = 0.0

  def _enable(self):
    raise NotImplementedError

  def _disable(self):
    raise NotImplementedError

  def _set_duty_cycle(self, duty_cycle):
    raise NotImplementedError

  def _set_frequency(self, freqency_hz):
    raise NotImplementedError

  def enable(self):
    self._enable()
    self._enabled = True

  def disable(self):
    self._disable()
    self._enabled = False

  def is_enabled(self):
    return self._enabled

  def set_duty_cycle(self, duty_cycle):
    if duty_cycle < 0 or duty_cycle > 100:
      raise ValueError('Duty cycle must be between 0 and 100. Got: %d'
                       % duty_cycle)
    self._set_duty_cycle(duty_cycle)
    self._duty_cycle = duty_cycle

  def get_duty_cycle(self):
    return self._duty_cycle

  def set_frequency(self, frequency_hz):
    if frequency_hz < 0:
      raise ValueError('Frequency must be greater than 0. Got: %d'
                       % frequency_hz)
    self._set_frequency(frequency_hz)
    self._frequency_hz = frequency_hz

  def get_frequency(self):
    return self._frequency_hz

  def get_pin_number(self):
    return self._output_pin.get_pin_number()

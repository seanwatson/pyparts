import RPi.GPIO as gpio

from pyparts.platforms.pwm import base_pwm

class RaspberryPiPWMOutput(base_pwm.BasePWM):

  def __init__(self, output_pin, frequency_hz=2000):
    super(RaspberryPiPWMOutput, self).__init__(output_pin)
    self._pwm_pin = gpio.PWM(self._output_pin.get_pin_number(), frequency_hz)

  def _enable(self):
    self._pwm_pin.start(0)

  def _disable(self):
    self._pwm_pin.stop()

  def _set_duty_cycle(self, duty_cycle):
    self._pwm_pin.ChangeDutyCycle(duty_cycle)

  def _set_frequency(self, frequency_hz):
    self._pwm_pin.ChangeFrequency(frequency_hz)

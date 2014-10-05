import RPi.GPIO as gpio

from platforms.pwm import base_pwm

class RaspberryPiPWMOutput(base_pwm.BasePWM):

  def __init__(self, output_pin):
    super(RaspberryPiPWMOutput, self).__init__(output_pin)
    self._pwm_pin = gpio.PWM(self._output_pin.get_pin_number(), 0.0)

  def _enable(self):
    self._pwm_pin.start()

  def _disable(self):
    self._pwm_pin.stop()

  def _set_duty_cycle(self, duty_cycle):
    self._pwm_pin.ChangeDutyCycle(duty_cycle)

  def _set_frequency(self, frequency_hz):
    self._pwm_pin.ChangeFrequency(frequency_hz)

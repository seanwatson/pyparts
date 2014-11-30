import time

from pyparts.logic import pid_controller

class TemperatureController(object):

  MAX_ERROR_DEGREES_C = 10.0

  def __init__(self, temp_sensor, heater_pin, kp, ki, kd):
    self._temp_sensor = temp_sensor
    self._heater_pin = heater_pin
    self._pid_worker = pid_controller.PIDController.Worker(
        kp, ki, kd, self._pid_input_func, self._pid_output_func)

  def _pid_input_func(self):
    return self._time_sensor.get_temp_c()

  def _pid_output_func(self, val):
    # If the sensor is too hot, turn off the heater
    if val <= 0:
      self._heater_pin.set_duty_cycle(0)
      return
    if val > MAX_ERROR_DEGREES_C:
      self._heater_pin.set_duty_cycle(100)
      return
    self._heater_pin.set_duty_cycle(float(val) / self.MAX_ERROR_DEGREES_C * 100)
    time.sleep(0.1)

  def set_temp_c(self, temp):
    self._pid_worker.set_desired_value(temp)

  def get_temp_setting(self):
    return self._pid_worker.get_desired_value()

  def enable(self):
    self._pid_worker.start()

  def disable(self):
    self._pid_worker.stop()

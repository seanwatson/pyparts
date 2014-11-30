import time
import threading


class PIDController(object):

  def __init__(self, kp, ki, kd):
    self._kp = kp
    self._ki = ki
    self._kd = kd

    self._prev_error = 0
    self._cp = 0
    self._ci = 0
    self._cd = 0

    self._prev_time = time.time()

  def get_output(self, error):
    self._current_time = time.time()
    dt = self._current_time - self._prev_time
    de = error - self._prev_error

    self._cp = self._kp * error
    self._ci += error * dt
    self._cd = 0
    if dt > 0:
      self._cd = de / dt

    self._prev_time = self._current_time
    self._prev_error = error

    return self._cp  + (self._ki * self._ci) + (self._kd * self._cd)

  class Worker(threading.Thread):

    def __init__(self, kp, kd, ki, input_func, output_func):
      super(PIDController.Worker, self).__init__()
      self._controller = PIDController(kp, ki, kd)
      self._input_func = input_func
      self._output_func = output_func
      self._set_point = 0
      self._stop = False

    def set_desired_value(self, value):
      self._set_point = value

    def get_desired_value(self):
      return self._set_point

    def stop(self):
      self._stop = True

    def run(self):
      while not self._stop:
        current_val = self._input_func()
        error = self._set_point - current_val
        self._output_func(self._controller.get_output(error))

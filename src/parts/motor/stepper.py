import time

from pyparts.parts import base_part


class StepperMotor(base_part.BasePart):

  def __init__(self, coil_1_a, coil_1_b, coil_2_a, coil_2_b, enable):
    self._coil_1_a = coil_1_a
    self._coil_1_b = coil_1_b
    self._coil_2_a = coil_2_a
    self._coil_2_b = coil_2_b
    self._enable = enable

  def enable(self):
    self._enable.set_high()

  def disable(self):
    self._enable.set_low()

  def forward(self, delay, steps):  
    for i in range(0, steps):
      self._setStep(1, 0, 1, 0)
      time.sleep(delay)
      self._setStep(0, 1, 1, 0)
      time.sleep(delay)
      self._setStep(0, 1, 0, 1)
      time.sleep(delay)
      self._setStep(1, 0, 0, 1)
      time.sleep(delay)

  def backward(self, delay, steps):  
    for i in range(0, steps):
      self._setStep(1, 0, 0, 1)
      time.sleep(delay)
      self._setStep(0, 1, 0, 1)
      time.sleep(delay)
      self._setStep(0, 1, 1, 0)
      time.sleep(delay)
      self._setStep(1, 0, 1, 0)
      time.sleep(delay)

  def _setStep(self, w1, w2, w3, w4):
   if w1:
     self._coil_1_a.set_high()
   else:
     self._coil_1_a.set_low()
   if w2:
     self._coil_1_b.set_high()
   else:
     self._coil_1_b.set_low()
   if w3:
     self._coil_2_a.set_high()
   else:
     self._coil_2_a.set_low()
   if w4:
     self._coil_2_b.set_high()
   else:
     self._coil_2_b.set_low()

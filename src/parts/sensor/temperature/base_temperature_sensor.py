from pyparts.parts import base_part

class BaseTemperatureSensor(base_part.BasePart):

  def get_temp_c(self):
    raise NotImplementedError

  def get_temp_f(self):
    return self._to_f(self.get_temp_c())

  def _to_f(self, temp):
    return (temp * 9 / 5) + 32

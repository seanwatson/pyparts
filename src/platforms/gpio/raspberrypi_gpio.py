import RPi.GPIO as rpi_gpio

from platforms.gpio import base_gpio


class RaspberryPiGPIO(base_gpio.BaseGPIO):

  def __init__(self, pin, mode)
    super(RaspberryPiGPIO, self).__init__(pin, mode)
    
    if self._mode == base_gpio.INPUT:
      pin_type = rpi_gpio.IN
    else:
      pin_type = rpi_gpio.OUT

    rpi_gpio.setup(self._pin, pin_type)
    
  def _write(self, value):
    rpi_gpio.output(self.pin, value)

  def _read(self):
    return rpi_gpio.input(self.pin)


def RaspberryPiDigitalInput(RaspberryPiGPIO):

  def __init__(self, pin):
    super(RaspberryPiDigitalInput, self).__init__(pin, base_gpio.INPUT)


def RaspberryPiDigitalOutput(RaspberryPiGPIO):

  def __init__(self, pin):
    super(RaspberryPiDigitalInput, self).__init__(pin, base_gpio.OUTPUT)

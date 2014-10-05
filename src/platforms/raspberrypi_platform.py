import RPi.GPIO as gpio

from platforms import base_platform
from platforms.gpio import raspberrypi_gpio as rpi_gpio
from platforms.pwm import raspberrypi_pwm as rpi_pwm
from platforms.spi import raspberrypi_spi as rpi_spi

BCM = gpio.BCM
BOARD = gpio.BOARD


class RaspberryPiPlatform(base_platform.BasePlatform):

  def __init__(self, pin_numbering=rpi_gpio.BCM):
    super(RaspberryPiPlatform, self).__init__()
    
    if pin_numbering not in (BCM, BOARD):
      raise ValueError('Pin numbering must be one of: BCM, BOARD. Got %s'
                       % str(pin_numbering))
    gpio.setmode(pin_numbering)
    self._pin_numbering = pin_numbering

  def get_pin_numbering(self):
    return self._pin_numbering

  def get_digital_input(self, pin):
    return rpi_gpio.RaspberryPiDigitalInput(pin)

  def get_digital_output(self, pin):
    return rpi_gpio.RaspberryPiDigitalOutput(pin)

  def get_pwm_output(self, pin):
    output = rpi_gpio.RaspberryPiDigitalOutput(pin)
    return rpi_pwm.RaspberryPiPWMOutput(output)

  def get_hardware_spi_bus(self, port, device):
    return rpi_spi.RaspberryPiHardwareSPIBus(port, device)

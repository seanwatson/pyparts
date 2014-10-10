import RPi.GPIO as gpio

from platforms import base_platform
from platforms.gpio import raspberrypi_gpio as rpi_gpio
from platforms.pwm import raspberrypi_pwm as rpi_pwm
from platforms.spi import raspberrypi_spi as rpi_spi


# Create local copies of the numbering schemes for conveinence.
BCM = gpio.BCM
BOARD = gpio.BOARD


class RaspberryPiPlatform(base_platform.BasePlatform):
  """Raspberry Pi implementation of a platform.

  RaspberryPiPlatform provides peripheral devices that can be used by parts to
  interact with the Raspberry Pi computer. Available peripherals:
    * DigitalInput
    * DigitalOutput
    * PWMOutput
    * HardwareSPIBus

  Attributes:
    _pin_numbering: BCM or BOARD. The current pin numbering scheme.
  """

  def __init__(self, pin_numbering=rpi_gpio.BCM):
    """Creates a Raspberry Pi platform.

    Args:
      pin_numbering: BCM or BOARD. Specifies the pin numbering scheme to use.
        (default=BCM)

    Raises:
      ValueError: The pin numbering scheme was not one of (BCM, BOARD).
    """
    super(RaspberryPiPlatform, self).__init__()
    
    if pin_numbering not in (BCM, BOARD):
      raise ValueError('Pin numbering must be one of: BCM, BOARD. Got %s'
                       % str(pin_numbering))
    gpio.setmode(pin_numbering)
    self._pin_numbering = pin_numbering

  def get_pin_numbering(self):
    """Gets the current pin numbering scheme.

    Returns:
      The current pin numbering scheme. One of BCM or BOARD.
    """
    return self._pin_numbering

  def get_digital_input(self, pin):
    """Creates a digital input pin on a Raspberry Pi.

    Args:
      pin: Integer. Pin number to create the pin on.

    Returns:
      A RaspberryPyDigitalInput object for the pin.
    """
    return rpi_gpio.RaspberryPiDigitalInput(pin)

  def get_digital_output(self, pin):
    """Creates a digital output pin on a Raspberry Pi.

    Args:
      pin: Integer. Pin number to create the pin on.

    Returns:
      A RaspberryPyDigitalOutput object for the pin.
    """
    return rpi_gpio.RaspberryPiDigitalOutput(pin)

  def get_pwm_output(self, pin):
    """Creates a PWM outut pin on a Raspberry Pi.

    Args:
      pin: Integer. Pin number to create the pin on.

    Returns:
      A RaspberryPyPWMOutput object for the pin.
    """
    output = rpi_gpio.RaspberryPiDigitalOutput(pin)
    return rpi_pwm.RaspberryPiPWMOutput(output)

  def get_hardware_spi_bus(self, port, device):
    """Creates a hardware based SPI bus on a Raspberry Pi.

    The Raspberry Pi has an available hardware SPI interface at /dev/spidevX.Y
    where X and Y are the port and device number respectively.

    Args:
      port: Integer. The SPI port number to use.
      device: Integer. The SPI device number to use.

    Returns:
      A RaspberryPiHardwareSPIBus object for the port/device.
    """
    return rpi_spi.RaspberryPiHardwareSPIBus(port, device)

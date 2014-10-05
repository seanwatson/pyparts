import spidev

from platforms.spi import base_spi


class RaspberryPiHardwareSPIBus(base_spi.BaseHardwareSPIBus):

  def __init__(self, port, device):
    super(RaspberryPiHardwareSPIBus, self).__init__(port, device)
    self._spi_device = spidev.SpiDev()

  def _open(self):
    self.open(self._port, self._device)

  def _close(self):
    self._spi_device.close()

  def _set_clock_frequency(self, frequency_hz):
    self._spi_device.max_speed_hz = frequency_hz

  def _set_mode(self, mode):
    self._spi_device.mode = mode

  def _set_bit_order(self, order):
    self._spi_device.lsbfirst = order == LSB_FIRST

  def write(self, data):
    self._spi_device.writebytes(data)

  def read(self, length):
    return bytearray(self._spi_device.readbytes(length))

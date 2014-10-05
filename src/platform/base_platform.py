class BasePlatform(object)

  def get_digital_input(self, pin):
    raise NotImplementedError

  def get_digital_output(self, pin):
    raise NotImplementedError

  def get_pwm_output(self, pin):
    raise NotImplementedError

  def get_hardware_spi_bus(self, port, device):
    raise NotImplementedError

  def get_software_spi_bus(self, sclk_pin, mosi_pin, miso_pin, ss_pin):
    raise NotImplementedError

  def get_i2c_bus(self):
    raise NotImplementedError

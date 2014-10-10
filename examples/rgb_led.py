import time

from pyparts.parts.led import rgb_led
from pyparts.platforms import raspberrypi_platform as rpi_platform

RED_PIN = 1
GREEN_PIN = 2
BLUE_PIN = 3

PIN_NAMING_SCHEME = rpi_platform.BCM
PWM_FREQUENCY_HZ = 2000


def main():
  platform = rpi_platform.RasberryPiPlatform(PIN_NAMING_SCHEME)

  red_pwm = platform.get_pwm_output(RED_PIN)
  green_pwm = platform.get_pwm_output(GREEN_PIN)
  blue_pwm = platform.get_pwm_output(BLUE_PIN)
  rgb = rgb_led.RGBLed(red_pwm, green_pwm, blue_pwm)

  rgb.set_frequency(PWM_FREQUENCY_HZ)
  print 'PWM Frequency:', rgb.get_frequency

  rgb.set_rgb(25, 50, 75)
  print '(Red, Green, Blue):', rgb.get_rgb()

  rgb.enable()
  print 'Led enabled:' rgb.is_enabled()

  time.sleep(5)

  rgb.set_red(40)
  rgb.set_green(20)
  rgb.set_blue(0)
  print 'Red:', rgb.get_red()
  print 'Greed:', rgb.get_green()
  print 'Blue:', rgb.get_blue()

  time.sleep(5)

  rgb.fade(0, 0, 100)

  time.sleep(5)

  rgb.disable()
  print 'Led enabled:' rgb.is_enabled()


if __name__ == '__main__':
  self.main()

import time

from pyparts.parts.led import rgb_led
from pyparts.platforms import raspberrypi_platform as rpi_platform

# Pin numbers
RED_PIN = 1
GREEN_PIN = 2
BLUE_PIN = 3

PIN_NAMING_SCHEME = rpi_platform.BCM
PWM_FREQUENCY_HZ = 2000


def main():
  platform = rpi_platform.RasberryPiPlatform(PIN_NAMING_SCHEME)

  # Create an RGB LED.
  red_pwm = platform.get_pwm_output(RED_PIN)
  green_pwm = platform.get_pwm_output(GREEN_PIN)
  blue_pwm = platform.get_pwm_output(BLUE_PIN)
  rgb = rgb_led.RGBLed(red_pwm, green_pwm, blue_pwm)

  # Set the PWM frequency for the LEDs.
  rgb.set_pwm_frequency_hz(PWM_FREQUENCY_HZ)
  print 'PWM Frequency:', rgb.pwm_frequency_hz

  # Set all 3 colors at once.
  rgb.set_rgb(25, 50, 75)
  print '(Red, Green, Blue):', rgb.rgb

  # Enable the LED.
  rgb.enable()
  print 'Led enabled:' rgb.is_enabled

  time.sleep(5)

  # Set each color individually.
  rgb.set_red(40)
  rgb.set_green(20)
  rgb.set_blue(0)
  print 'Red:', rgb.red
  print 'Greed:', rgb.green
  print 'Blue:', rgb.blue

  time.sleep(5)

  # Fade from one color to another.
  rgb.fade(0, 0, 100)

  time.sleep(5)

  # Disable the LED.
  rgb.disable()
  print 'Led enabled:' rgb.is_enabled


if __name__ == '__main__':
  self.main()

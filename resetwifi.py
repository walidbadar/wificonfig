import os, subprocess, time, datetime
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def reset_wifi(ev=None):
    wifiSetting = open("/etc/wpa_supplicant/wpa_supplicant-wlan0.conf", "w")
    replacement = 'country=EC\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\nnetwork={\nssid="Mina"\nmode=2\npsk="admin123"\n}'
    wifiSetting.write(replacement)
    wifiSetting.close()
    subprocess.Popen(['shutdown','-r','now'])

def loop():
    GPIO.add_event_detect(25, GPIO.FALLING, callback=reset_wifi, bouncetime=1000)
    while True:
        pass   # Don't do anything, sit forever

if __name__ == '__main__':
    setup()
    try:
        loop()
    except:
        GPIO.cleanup()

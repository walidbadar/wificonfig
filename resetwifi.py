import os, subprocess, time, datetime
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def reset_wifi(ev=None):
    wifiSetting = open("/etc/wpa_supplicant/wpa_supplicant-wlan0.conf", "w")
    replacement = 'country=EC\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\nnetwork={\nssid="Mina"\nmode=2\npsk="admin"\n}'
    wifiSetting.write(replacement)
    wifiSetting.close()

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


wifiSetting = open("wifibook-fr1-udp53.owifi", "r")
replacement = ""
for line in wifiSetting:
    line = line.strip()
    changes = line.replace("auth-user-pass", "auth-user-pass /etc/openwifi/password.txt")
    replacement = replacement + changes + "\n"
wifiSetting.close()
wifiSetting = open("wifibook-fr1-udp53.owifi", "w")
wifiSetting.write(replacement)
wifiSetting.close()
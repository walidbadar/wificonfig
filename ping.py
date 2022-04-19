import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(2,GPIO.OUT, initial = GPIO.LOW)

while True:
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            GPIO.output(2, GPIO.HIGH)
            # print('Connected to Internet!')

    except:
        GPIO.output(2, GPIO.LOW)
        # print('Not Connected to Internet.')

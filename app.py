#!/usr/bin/env python
import motor
import os
import time
from importlib import import_module

from flask import Flask, render_template, Response, request

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera


app = Flask(__name__)
app.secret_key = "vth"

LEFT, RIGHT, FORWARD, BACKWARD, STOP = "left", "right", "forward", "backward", "stop"
AVAILABLE_COMMANDS = {
    'Left': LEFT,
    'Forward': FORWARD,
    'Right': RIGHT,
    'Backward': BACKWARD,
    'Stop': STOP
}


@app.route('/', methods=['POST', 'GET'])
def index():
    """Home page"""
    return render_template('index.html', commands=AVAILABLE_COMMANDS)


def gen(camera):
    while True:
        """This function generates the frame for displaying the video. The 'yield' increments the iteration by the 
        next, therefore, the image overlaps. The frame variable is used later in the function video_feed() """
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """This function streams the images on the frame, with the next one overlapping and replacing the former. This is
    achieved by setting mimetype to 'multipart/x-mixed-replace'. The idea is that by replacing the image with another
    so quickly, it'd look like a video."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# GPIO Mode
GPIO.setmode(GPIO.BCM)
# Set GPIO Pins
LED_L = 2
LED_R = 4
# Set GPIO Pins
TRIG = 18
ECHO = 24
LED = 23
LED_S = 3
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# LED setup
GPIO.setwarnings(False)
GPIO.setup(LED_L, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED_S, GPIO.OUT)


def led():
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_l():
    GPIO.output(LED_L, GPIO.HIGH)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_r():
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_s():
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_S, GPIO.HIGH)


def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    print("Measuring...")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    stop = time.time()

    # Save StartTime
    while GPIO.input(ECHO) == 0:
        start = time.time()

    # Save StopTime
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    return (stop - start) / 0.000058  # cm


@app.route('/<cmd>')
def command(cmd=None):
    if cmd == STOP:
        print("Stop Pressed")
        led_s()
        measure()
        motor.stop()
    elif cmd == FORWARD:
        print("Up Pressed")
        led()
        measure()
        motor.forward()
    elif cmd == BACKWARD:
        print("Down Pressed")
        led()
        measure()
        motor.backward()
    elif cmd == LEFT:
        print("Left Pressed")
        led_l()
        measure()
        motor.left()
    else:
        print("Right Pressed")
        led_r()
        measure()
        motor.right()
    response = "Moving {}".format(cmd.capitalize())
    return response, 200, {'Content-Type': 'text/plain'}


def measure():
    try:
        while True:
            dist = distance()
            print("Distance: %.2f cm" % dist)
            if dist < 15:
                GPIO.output(LED, GPIO.HIGH)
            else:
                GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop measurement")


@app.route('/log_out')
def shutdown_server():
    """Send a request to shutdown werkzeug server and load the signing out page"""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return render_template("log_out.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True, threaded=True)

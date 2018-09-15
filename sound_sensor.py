import os # Miscellaneous operating system interface
import zmq # Asynchronous messaging framework
import time # Time access and conversions
from random import randint # Random numbers
import sys # System-specific parameters and functions
from matrix_io.proto.malos.v1 import driver_pb2 # MATRIX Protocol Buffer driver library
from matrix_io.proto.malos.v1 import io_pb2 # MATRIX Protocol Buffer sensor library
from multiprocessing import Process, Manager, Value # Allow for multiple processes at once
from zmq.eventloop import ioloop, zmqstream# Asynchronous events through ZMQ
from ledimage import ImageCreator

matrix_ip = '127.0.0.1' # Local device ip
everloop_port = 20021 # Driver Base port
led_count = 0 # Amount of LEDs on MATRIX device (35 leds for us)


def ledSpin(lit_led):
    # Create an empty Everloop image
    image = []
    
    if led_count == lit_led:
        lit_led = 1
    else:
        lit_led = lit_led + 1
        
    for led in range(0, lit_led):
        # Set individual LED value
        ledValue = io_pb2.LedValue()
        ledValue.blue = 0
        ledValue.red = 0
        ledValue.green = 0
        ledValue.white = 0
        image.append(ledValue)
        
    for led in range(lit_led, lit_led+1):
        # Set individual LED value
        ledValue = io_pb2.LedValue()
        ledValue.blue = 0
        ledValue.red = 100
        ledValue.green = 0
        ledValue.white = 0
        image.append(ledValue)
		
    for led in range(lit_led +1, led_count):
        # Set individual LED value
        ledValue = io_pb2.LedValue()
        ledValue.blue = 0
        ledValue.red = 0
        ledValue.green = 0
        ledValue.white = 0
        image.append(ledValue)
        
            #reset led counter    
        

    return [image, lit_led] 
    

def ping_socket():
    # Define zmq socket
    context = zmq.Context()
    # Create a Pusher socket
    ping_socket = context.socket(zmq.PUSH)
    # Connect to the socket
    ping_socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port+1))
    # Send one ping
    ping_socket.send_string('')

def everloop_error_callback(error):
    # Log error
    print('{0}'.format(error))

def update_socket():
    # Define zmq socket
    context = zmq.Context()
    # Create a Subscriber socket
    socket = context.socket(zmq.SUB)
    # Connect to the Data Update port
    socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port+3))
    # Connect Subscriber to Error port
    socket.setsockopt(zmq.SUBSCRIBE, b'')
    # Create the stream to listen to data from port
    stream = zmqstream.ZMQStream(socket)

    # Function to update LED count and close connection to the Data Update Port
    def updateLedCount(data):
        # Extract data and pass into led_count global variable
        global led_count
        led_count = io_pb2.LedValue().FromString(data[0]).green
        # Log LEDs
        print('{0} LEDs counted'.format(led_count))
        # If LED count obtained
        if led_count > 0:
            # Close Data Update Port connection
            ioloop.IOLoop.instance().stop()
            print('LED count obtained. Disconnecting from data publisher {0}'.format(everloop_port+3))
    # Call updateLedCount() once data is received
    stream.on_recv(updateLedCount)

    # Log and begin event loop for ZMQ connection to Data Update Port
    print('Connected to data publisher with port {0}'.format(everloop_port+3))
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    # Initiate asynchronous events
    ioloop.install()
    # Start Error Port connection
    # Process(target=register_error_callback, args=(everloop_error_callback, matrix_ip, everloop_port)).start()    
    # Ping the Keep-alive Port once
    ping_socket()
    # Start Data Update Port connection & close after response
    update_socket()
    # Send Base Port configuration
    try:
        context = zmq.Context()
        # Create a Pusher socket
        socket = context.socket(zmq.PUSH)
        # Connect Pusher to configuration socket
        socket.connect('tcp://{0}:{1}'.format(matrix_ip, everloop_port))
        driver_config_proto = driver_pb2.DriverConfig()

        img = ImageCreator()
        while True:
            # Create a new driver config
####################### led painting happens here ####################
            r = 0
            led_count = 35
            for i in range(led_count):
                r += int(200/35)
                img.set_led(i, r,0,0,0)
                
          
            leds = img.out
            
            image = []
           # For each device LED
            for led in leds:
               # Set individual LED value
               ledValue = io_pb2.LedValue()
               ledValue.blue = led[2]
               ledValue.red = led[0]
               ledValue.green = led[1]
               ledValue.white = led[3]
               image.append(ledValue)
           # Store the Everloop image in driver configuration

            driver_config_proto.image.led.extend(image)

            # Send driver configuration through ZMQ socket
            socket.send(driver_config_proto.SerializeToString())
            # Wait before restarting loop
            time.sleep(0.1)
# Avoid logging Everloop errors on user quiting
    except KeyboardInterrupt:
        print(' quit')

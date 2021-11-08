# main.py -- put your code here!

from network import LoRa
import time
import binascii
import socket
import pycom
import machine 
from machine import Pin
import utime
import ustruct

# initialise Ultrasonic Sensor pins
echo = Pin(Pin.exp_board.G7, mode=Pin.IN) # Lopy4 specific: Pin('P20', mode=Pin.IN)
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT) # Lopy4 specific Pin('P21', mode=Pin.IN)
trigger(0)

# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2

    return distance

# to reduce errors we take ten readings and use the median
def distance_median():

    # initialise the list
    distance_samples = []
    # take 10 samples and append them into the list
    for count in range(10):
        distance_samples.append(int(distance_measure()))
    # sort the list
    distance_samples = sorted(distance_samples)
    # take the center list row value (median average)
    distance_median = distance_samples[int(len(distance_samples)/2)]
    # apply the function to scale to volts

    print(distance_samples)

    return int(distance_median)

# Turn of the default blinking every 4 seconds
pycom.heartbeat(False)

#Local testing code
# count = 0
# # limit to 200 packets; just in case power is left on
# while count < 200:

#     # take distance measurment, turn the light blue when measuring
#     pycom.rgbled(0x00007d)
#     utime.sleep(1)
#     distance = distance_median()
#     pycom.rgbled(0x004600)

#     print("Distance ",count,":",distance)
#     count += 1


 # Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    pycom.rgbled(0xFF0000)
    lora.nvram_restore()
else:
    # create an OTAA authentication parameters
    app_eui = binascii.unhexlify('0000000000000000')
    app_key = binascii.unhexlify('DF6FC4A272140DDF43F0F77F9429EFEB') #('B54ED2937D0E35151F23FB0528A704DB')
    # Red while connecting to LORA
    pycom.rgbled(0xFF0000)
    
    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    print('Starting up')
# wait until the module has joined the network
for x in range(20):
    if not lora.has_joined():
        print('Not joined yet...attempt', (x+1))
        time.sleep(2.5)

if not lora.has_joined():
    print('Could not join network, will try again later')
    machine.deepsleep(5000);
else:
    print('Network joined!')
    pycom.rgbled(0x00FF00)
    # setup the socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
    s.setblocking(False)
    s.bind(1)
    count = 0
    # limit to 200 packets; just in case power is left on
    while count < 5:

        # take distance measurment, turn the light blue when measuring
        pycom.rgbled(0x00007d)
        utime.sleep(1)
        distance = distance_median()
        pycom.rgbled(0x004600)

        print("Distance:  ", distance)
        # encode the packet, so that it's in BYTES (TTN friendly)
        # could be extended like this struct.pack('f', distance) + struct.pack('c',"example text")
        # 'h' packs it into a short, 'f' packs it into a float, must be decoded in TTN
        packet = ustruct.pack('h', distance)

        # send the prepared packet via LoRa
        s.send(packet)

        # example of unpacking a payload - unpack returns a sequence of
        #immutable objects (a list) and in this case the first object is the only object
        print ("Unpacked value is:", ustruct.unpack('h',packet)[0])

        # check for a downlink payload, up to 64 bytes
        rx_pkt = s.recv(64)

        # check if a downlink was received
        if len(rx_pkt) > 0:
            print("Downlink data on port 200:", rx_pkt)
            pycom.rgbled(0xffa500)
            input("Downlink recieved, press Enter to continue")
            pycom.rgbled(0x004600)

        count += 1
        utime.sleep(10)

    lora.nvram_save()
    machine.deepsleep(10*1000)

# while True:
#     s.setblocking(True)
#     pycom.rgbled(0x445CFD)
#     # send some data
#     print(time.time())
#     t1 = time.time()
#     s.send(bytes([0x57, 0x75, 0x74]))
#     print('Sent in: ', time.time()-t1, ' seconds')
#     pycom.rgbled(0x000000)

#     # make the socket non-blocking
#     # (because if there's no data received it will block forever...)
#     s.setblocking(False)

#     # get any data received (if any...)
#     data = s.recv(64)
#     print('Downlink: ' + str(data))

#     if data == b'\x01':
#         pycom.rgbled(0x00FF00) #green
#         time.sleep(1)
#         pycom.rgbled(0x000000) #off
#         time.sleep(0.5)
#         pycom.rgbled(0x00FF00) #green
#         time.sleep(1)
#         pycom.rgbled(0x000000)
#     #time.sleep(30)
#     lora.nvram_save()
#     machine.deepsleep(10*1000)


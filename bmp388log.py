import time
import smbus2
import bmp388

bus = smbus2.SMBus(1)
address = 0x77

calibration_params = bmp388.load_calibration_params(bus, address)
layout = '{0:5d}:  {1},  {2:0.3f} deg C,  {3:0.2f} hPa,  {4:0.2f} %'
counter = 1

while True:
    data = bmp388.sample(bus, address, calibration_params)
    with open("sample.log","a+") as f:
        f.write(layout.format(counter, data.timestamp, data.temperature, data.pressure, data.humidity) + "\n")
    f.close()
    counter += 1
    time.sleep(5)

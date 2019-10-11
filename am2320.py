#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus2
import sensors.am2320

sensor = sensors.am2320.Am2320sensor(1)

if __name__ == '__main__':
    sensor.setup()

    for sensor_name, sensor_value in sensor.read().items():
        print(sensor_value)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus2
import sensors.lps25h

sensor = sensors.lps25h.Lps25hsensor(1)

if __name__ == '__main__':
  sensor.setup()
  print ( sensor.read() )

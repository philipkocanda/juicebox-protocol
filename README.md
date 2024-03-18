# Juicebox

## Tested devices

- Juicebox 32A 3-phase 2018 (v7, firmware: ?, hardware: ?)

## Usage

NOTE: The most up to date examples can be found in the test suite.

```py
from juicebox.hru_device import HruDevice

hru = HruDevice(HruDevice.ESP32_ADDR, HruDevice.HRU_ADDR)
msg = hru.set_supply_fan_rpm(0)

print(str(msg))
# => "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 04"

print(msg.bytes_list())
# => ['82', '80', 'A4', '10', '06', '13', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '2D', '00', '04']

print(msg.build().data)
# => [130, 128, 164, 16, 6, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 4]
```


## UDP packet format

`[Byte index] description`

```
[0]     destination address
[1]     reply address
[2..3]  message class
[4]     message type
[5]     payload length
[n]     payload
[n+1]   checksum
```

## Unit Tests

Run all unit tests:

```sh
bin/test
```
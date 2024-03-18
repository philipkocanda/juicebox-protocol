# Juicebox Protocol

## Tested devices

- Juicebox 32A 3-phase 2018 (v7)

## Usage

```python3
from juicebox.message import Message

m = Message()
m.offline_amperage = 20
m.instant_amperage = 16

print(m.build())
# CMD52324A20M16C006S001!5RE$

print(m.inspect())
# {'offline_amperage': 20, 'instant_amperage': 16, 'payload_str': 'CMD52324A20M16C006S001', 'checksum_str': '5RE', 'checksum_computed': '5RE'}
```

## Unit Tests

Run all unit tests:

```sh
bin/test
```
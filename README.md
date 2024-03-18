# Juicebox Protocol

Basic library for building and parsing Juicebox UDP messages. Shoutout to @FalconFour and @jesserockz who were instrumental in getting this to work and [whose code](https://gist.github.com/jesserockz/276441f58892b7b425910bf9144cba39) I've reused in this library. See [this issue](https://github.com/snicker/juicepassproxy/issues/39) for more.

## Tested devices

- Juicebox 32A 3-phase 2018 (v7)

## Usage

Building a message:

```python3
from juicebox.message import Message

m = Message()
m.offline_amperage = 20
m.instant_amperage = 16
m.command = 6 # TODO: still not sure what this does
m.message_counter = 1

print(m.build())
# CMD52324A20M16C006S001!5RE$

print(m.inspect())
# {'offline_amperage': 20, 'instant_amperage': 16, 'payload_str': 'CMD52324A20M16C006S001', 'checksum_str': '5RE', 'checksum_computed': '5RE'}
```

Parsing a message:

```python3
from juicebox.message import Message

m = Message().from_string('CMD41325A0040M040C006S638!5N5$')
print(m.inspect())
# {'offline_amperage': 0, 'instant_amperage': 0, 'payload_str': 'CMD41325A0040M040C006S638', 'checksum_str': '5N5', 'checksum_computed': '5N5'}
```

NOTE: Only the payload as a whole is parsed, the contents are not. This exists mostly for testing purposes.

## Unit Tests

Run all unit tests:

```sh
bin/test
```

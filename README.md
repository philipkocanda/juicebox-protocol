# Juicebox Protocol

Basic library for building and parsing Juicebox UDP messages. Shoutout to @FalconFour and @jesserockz who were instrumental in getting this to work and [whose code](https://gist.github.com/jesserockz/276441f58892b7b425910bf9144cba39) I've reused in this library. See [this issue](https://github.com/snicker/juicepassproxy/issues/39) for more.

## Features

- [x] Build command (CMD) messages

## TODO

- [ ] Figure out what the "command" field does (naming is mine, not sure if it's actually a command)
- [ ] Figure out what the counter is for.
- [ ] Integrate into Juicepassproxy (JPP) to get it to actually send a message to the Juicebox (HA > MQTT > JPP > Juicebox)
- [ ] Support parsing status messages
- [ ] Nice to have for consistency: Support parsing command messages

## Tested devices

- Juicebox 32A 3-phase 2018 (v7)

## Usage

Building a message:

```python3
from juicebox.message import Message

m = Message()
m.offline_amperage = 20
m.instant_amperage = 16
m.command = 6 # TODO: figure out what this does
m.counter = 1

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

## Command Message Format

Command messages sent to the Juicebox by the server on regular intervals:

```
CMD62210A20M18C006S006!31Y$
^^^^^^^^^^^^^^^^^^^^^^ ^^^
          |             |
       payload       checksum

CMD    # Prefix
6      # Day of week (6 = Saturday, 0 = Sunday).
2210   # Local time (22:10)
A20    # Offline Amperage
M18    # Instant Amperage
C006   # Command?
S006   # Message counter?
!      # Delimiter between payload and checksum
31Y    # Checksum (base35) calculated from payload
$      # Suffix
```

### Day of week and local time

Sets the internal clock based on the local time zone for offline time of use.

Source: [FalconFour](https://github.com/snicker/juicepassproxy/issues/39#issuecomment-2002312548)

### Offline Amperage (aka Wire Rating)

Stored in the microcontroller's EEPROM as "wire rating", and it takes effect immediately on startup.

Source: [FalconFour](https://github.com/snicker/juicepassproxy/issues/39#issuecomment-2002312548)

### Instant Amperage

When online, tells the box how many amps to allow. Anything below 6A disallows/disables charging, causing the Charge LED to flash when plugged in.

The "instant amperage" command is fleeting, it only matters while the box is online/receiving regular CMD reports from each of its runtime report packets.

Precedence of amperage limit is: Unit rating > Offline amperage > Runtime amperage. So if unit rating is 32, sending offline amperage 40 / runtime 40, the unit rating (baked into firmware code, non-modifiable) takes precedence and you get 32 amps. If unit rating=40, offline=32, runtime=16, you get 16 amps. Similarly, unit=40, offline=16, runtime=32, you ought to get 16 amps, but server architecture always prevented that from being sent, so the behavior may be undefined (if it's online, it should go 32, but if it goes offline / hasn't received a command in about 5 minutes, you may get 16).

Source: [FalconFour](https://github.com/snicker/juicepassproxy/issues/39#issuecomment-2002312548)

### Command (?)

Alternates between C242, C244, C008, C006. Purpose unclear.

### Message counter (?)

Increments by one for every message until 999 then it loops back to 001. Purpose unclear.

### TBD

> There is also a bit mask in there that determines "whether the user is looking at the app now", which increases the report interval from 10 seconds when charging (I believe) and 30 seconds when idle, to 3 seconds for both modes.

> if I'm recalling/reading correctly, the first part of the command (several numeric digits) is setting the clock, and the final one is sending time-of-use hours with a bit mask (weekday start, weekday end, weekend start, weekend end) - this is all inherited from wayyyy old protocol back in 2014 or so when this silly protocol was first devised.

Source: [FalconFour](https://github.com/snicker/juicepassproxy/issues/39#issuecomment-2002312548)

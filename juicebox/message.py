from juicebox.checksum import Checksum
from juicebox.exceptions import InvalidMessageFormat
import re
import datetime

class Message:
    def __init__(self) -> None:
        self.payload_str = None
        self.checksum_str = None

        # Offline Amperage
        # Stored in the microcontroller's EEPROM as "wire rating", and it takes effect immediately on startup.
        self.offline_amperage = 0

        # Instant Amperage
        # When online, tells the box how many amps to allow. Anything below 6A disallows/disables charging, causing the Charge LED to flash when plugged in.
        # The instant/runtime amp command is fleeting, it only matters while the box is online/receiving regular CMD reports from each of its runtime report packets.
        self.instant_amperage = 0

        self.command = 6 # Alternates between C242, C244, C008, C006. Meaning unclear.

        # increments by one for every message until 999 then it loops back to 1
        self.message_counter = 1

        self.time = datetime.datetime.today()

        pass


    def from_string(self, string: str) -> 'Message':
        msg = re.search(r'((?P<payload>.*)!(?P<checksum>[A-Z0-9]{3})(?:\$|:))', string)

        if msg is None:
            raise InvalidMessageFormat(f"Unable to parse message: '{string}'")

        self.payload_str = msg.group('payload')
        self.checksum_str = msg.group('checksum')
        return self


    def checksum(self) -> Checksum:
        return Checksum(self.payload_str)


    def checksum_computed(self) -> str:
        return self.checksum().base35()


    def build_payload(self) -> None:
        if self.payload_str:
            return

        weekday = self.time.strftime('%w') # 0 = Sunday, 6 = Saturday

        # Instant amperage may need to be represented using 4 digits (e.g. 0040)
        # on newer Juicebox versions.
        self.payload_str = f"CMD{weekday}{self.time.strftime('%H%M')}A{self.offline_amperage:02d}M{self.instant_amperage:02d}C{self.command:03d}S{self.message_counter:03d}"
        self.checksum_str = self.checksum_computed()


    def build(self) -> str:
        self.build_payload()
        return f"{(self.payload_str)}!{self.checksum_str}$"


    def inspect(self) -> dict:
        return {
            "offline_amperage": self.offline_amperage,
            "instant_amperage": self.instant_amperage,
            "payload_str": self.payload_str,
            "checksum_str": self.checksum_str,
            "checksum_computed": self.checksum_computed(),
        }


    def __str__(self):
        return self.build()

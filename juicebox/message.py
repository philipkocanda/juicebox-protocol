from juicebox.constants import Constants
from juicebox.checksum import Checksum
from juicebox.exceptions import InvalidMessageFormat
import re

class Message:
    def __init__(self) -> None:
        self.payload_str = ""
        self.checksum_str = ""
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


    def build(self) -> str:
        return f"{self.payload_str}!{self.checksum.base35()}$"


    def inspect(self) -> dict:
        return {
            "payload_str": self.payload_str,
            "checksum_str": self.checksum_str,
            "checksum_computed": self.checksum_computed(),
        }


    def __str__(self):
        return self.build()

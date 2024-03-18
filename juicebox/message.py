from juicebox.constants import Constants
from juicebox.checksum import Checksum
from juicebox.exceptions import InvalidMessageFormat
import re

class Message:
    def __init__(self) -> None:
        self.data = "" # rename to payload?
        self.checksum = ""
        pass


    def from_string(self, string: str):
        msg = re.search(r'((?P<data>.*)!(?P<checksum>[A-Z0-9]{3})(?:\$|:))', string)
        
        if msg is None:
            raise InvalidMessageFormat(f"Unable to parse message: '{string}'")
        
        self.data = msg.group('data')
        self.checksum = msg.group('checksum')
        return self
    

    def checksum(self):
        return Checksum(self)
        

    def build(self):
        self.data = [
            self.dest,
            self.src,
            *self.encode_msg_class(self.msg_class),
            self.type,
            len(payload),
            *payload,
        ]

        self.data.append(self.calc_checksum(self.data))

        return self


    def inspect(self):
        return {
            "dest": self.dest,
            "src": self.src,
            "msg_class": Constants.MSG_CLASSES.get(self.msg_class, 0)['name'],
            "msg_type": Constants.MSG_TYPES.get(self.type, f"<unknown: {self.type}>"),
            "payload": self.payload.to_dict(),
        }


    def __str__(self):
        """
        Returns hexadecimal bytestring representation of the entire message: '82 80 A4 10'
        """
        self.build()

        data = list(map(self.to_hex, self.data))

        return " ".join(data)

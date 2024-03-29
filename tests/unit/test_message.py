import unittest
from juicebox.message import Message
from juicebox.exceptions import InvalidMessageFormat
import datetime

class TestMessage(unittest.TestCase):
    def test_message_building(self):
        m = Message()
        m.time = datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
        m.offline_amperage = 20
        m.instant_amperage = 16
        print(m.build())
        print(m.inspect())
        self.assertEqual(m.build(), "CMD52324A20M16C006S001!5RE$")


    def test_message_validation(self):
        with self.assertRaises(InvalidMessageFormat):
            m = Message().from_string("g4rbl3d")


    def test_command_message_parsing(self):
        """
        Command messages are typically sent by the Cloud to the JuiceBox
        """
        raw_msg = "CMD41325A0040M040C006S638!5N5$"
        m = Message().from_string(raw_msg)
        self.assertEqual(m.payload_str, "CMD41325A0040M040C006S638")
        self.assertEqual(m.checksum_str, "5N5")
        self.assertEqual(m.checksum_str, m.checksum_computed())
        self.assertEqual(m.build(), raw_msg)

    def test_status_message_parsing(self):
        """
        Status messages are sent by the JuiceBox
        """
        raw_msg = "0910042001260513476122621631:v09u,s627,F10,u01254993,V2414,L00004555804,S01,T08,M0040,C0040,m0040,t29,i75,e00000,f5999,r61,b000,B0000000!55M:"

        m = Message().from_string(raw_msg)
        self.assertEqual(m.payload_str, "0910042001260513476122621631:v09u,s627,F10,u01254993,V2414,L00004555804,S01,T08,M0040,C0040,m0040,t29,i75,e00000,f5999,r61,b000,B0000000")
        self.assertEqual(m.checksum_str, "55M")
        self.assertEqual(m.checksum_str, m.checksum_computed())
        # self.assertEqual(m.build(), raw_msg)

    def test_message_checksums(self):
        messages = [
            'CMD41325A0040M040C006S638!5N5$', # @MrDrew514 (v09u)
            'CMD62210A20M18C006S006!31Y$',
            'CMD62228A20M15C008S048!IR4$',
            'CMD62207A20M20C244S997!R5Y$',
            'CMD62207A20M20C008S996!ZI4$',
            'CMD62201A20M20C244S981!ECD$',
            'CMD62201A20M20C006S982!QT8$',
        ]

        for message in messages:
            m = Message().from_string(message)
            print(m.inspect())

            self.assertEqual(m.checksum_str, m.checksum_computed())

if __name__ == '__main__':
    unittest.main()

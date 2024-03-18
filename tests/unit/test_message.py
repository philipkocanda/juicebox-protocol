import unittest
from juicebox.checksum import Checksum
from juicebox.message import Message
from juicebox.exceptions import InvalidMessageFormat

class TestMessage(unittest.TestCase):
    def test_message_validation(self):
      with self.assertRaises(InvalidMessageFormat):
        m = Message().from_string("g4rbl3d")

    def test_message_parsing(self):
      m = Message().from_string("CMD41325A0040M040C006S638!5N5$")
      self.assertEqual(m.data, "CMD41325A0040M040C006S638")
      self.assertEqual(m.checksum, "5N5")

if __name__ == '__main__':
    unittest.main()

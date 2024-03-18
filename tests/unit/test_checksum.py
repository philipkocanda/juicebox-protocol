import unittest
from juicebox.checksum import Checksum
from juicebox.message import Message

class TestChecksum(unittest.TestCase):
    def test_messages(self):
      messages = [
          'CMD41325A0040M040C006S638!5N5$', # @MrDrew514 (v09u)
          'CMD62227A20M15C006S046!HP1$', # does not work? outlier?
          'CMD62210A20M18C006S006!31Y$',
          'CMD62228A20M15C008S048!IR4$',
          'CMD62207A20M20C244S997!R5Y$',
          'CMD62207A20M20C008S996!ZI4$',
          'CMD62201A20M20C244S981!ECD$',
          'CMD62201A20M20C006S982!QT8$',   
      ]
      
      for message in messages:
        m = Message().from_string(message)
        print(m.data)
        print(m.checksum)

        Checksum(message).debug()
        print("-------------------------")

        # self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()

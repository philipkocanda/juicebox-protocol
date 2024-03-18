class Checksum:
    ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, payload: str) -> None:
        self.payload = payload
        pass

    def base35encode(self, number: int) -> str:
        base35 = ""

        while number > 1:
            number, i = divmod(number, 35)
            if i == 24:
                i = 35
            base35 = base35 + self.ALPHABET[i]

        return base35


    def base35decode(self, number: str) -> int:
        decimal = 0
        for i, s in enumerate(reversed(number)):
            decimal += self.ALPHABET.index(s) * (35**i)
        return decimal


    def crc(self, data: str) -> int:
        h = 0
        for s in data:
            h ^= (h << 5) + (h >> 2) + ord(s)
            h &= 0xFFFF
        return h
    

    def calculate(self) -> str:
        return self.base35encode(self.crc(self.payload))


    def valid(self, other_crc: str) -> bool:
        crc = self.crc(self.payload)
        return other_crc == self.calculate()


    def debug(self):
        check = self.payload[-4:-1]
        data = self.payload[:-5]

        print(f"Data:  \t\t{data}")

        decimal = self.base35decode(check)

        total = self.crc(data)
        base35 = self.base35encode(total)

        print(f"Check:  \t{check}")
        print(f"Decimal: \t{decimal}")
        print()
        print(f"CRC:  \t\t{total}")
        print(f"Base35: \t{base35}")

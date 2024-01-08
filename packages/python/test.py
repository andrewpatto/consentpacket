import unittest

import generated as my_lib


class ExampleTest(unittest.TestCase):
    def test_main(self):
        x = my_lib.ConsentPacket(schemaMajorVersion=1, consents=[])
        y = my_lib.ConsentPacket(schemaMajorVersion=1, consents=[])

        self.assertEqual(
            x, y
        )


if __name__ == "__main__":
    unittest.main()

import unittest

class TestStringMethods(unittest.TestCase):
    def test_strings_a(self):
        self.assertEqual('a'*2, 'aa')
        #assertEqual

    def test_string_concert(self):
        self.assertEqual("a"+"b", "ab")

    def test_upper(self):
        self.a="python"
        self.assertEqual(self.a.upper(), "PYTHON")
        self.assertTrue("PYTHON".isupper())

    def strip1(self):
        self.a=" abc "
        self.assertEqual(self.a.strip(),"abc")


if __name__ == '__main__':
    unittest.main()

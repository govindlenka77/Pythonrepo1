import unittest
from unittest53 import Student

class New(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a=20
        print(cls.a,"Start Class")

    @classmethod
    def tearDownClass(cls):
        cls.b=200
        print(cls.b,"End class")

    def tearDown(self):
        print("End")

    def setUp(self):
        print("setting")
        self.a = Student("Govind", "Lenka", 1000)
        self.b = Student("Ravi","nov",500)

    def test_mail(self):
        self.assertEqual(self.a.email,"Govind.Lenka@gmail.com")
        self.assertEqual(self.b.email,"Ravi.nov@gmail.com")

    def test_marks(self):
        self.assertGreater(self.a.marks, 10)
        self.assertGreater(self.a.marks, 20)


    def test_last(self):
        self.assertTrue(self.a.last.lower().islower())


if __name__ == '__main__':
    unittest.main()

import unittest
import os
import requester


class TestStringMethods(unittest.TestCase):

    csvUrls = []
    urls = ['http://stackoverflow.com/questions/19557801/how-to-make-a-function-that-check-if-the-csv-file-is-valid-or-not-python']
    wrongUrls = ['a','b','hi']
    fnames = ['f','g','h']

    def test_valid_url(self):
        with self.assertRaises(ValueError):
            for url in self.wrongUrls:
                requester.url_to_csv(url, self.fnames[0])

    def test_csv_url(self):
        with self.assertRaises(TypeError):
            for url in self.urls:
                requester.url_to_csv(url, self.fnames[0])




    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
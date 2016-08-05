import unittest
import os
import warnings
import requester


class TestStringMethods(unittest.TestCase):

    csv_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data']
    invalid_csv_urls = ['http://stackoverflow.com/questions/19557801/how-to-make-a-function-that-check-if-the-csv-file-is-valid-or-not-python',
                        'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data']
    wrongUrls = ['hi','www.google','www.apple.com']
    fnames = ['f','g','h']


    def assertValueError(self):
        with self.assertRaises(ValueError):
            for url in self.wrongUrls:
                requester.url_to_csv(url, self.fnames[0])

    def assertTypeError(self):
        with self.assertRaises(TypeError):
            for url in self.invalid_csv_urls:
                requester.url_to_csv(url, self.fnames[0])

    def assertWarnings(self):
        with self.assertRaises(warnings.warn(RuntimeWarning)):
            for url in self.wrongUrls:
                requester.batch_url_to_csv(url, self.fnames[0])




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
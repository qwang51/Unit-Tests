import unittest
import os
import csv
import warnings
import requester


class TestStringMethods(unittest.TestCase):

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    fname = 'pandas.csv'
    csv_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data']
    invalid_csv_urls = ['http://stackoverflow.com/questions/19557801/how-to-make-a-function-that-check-if-the-csv-file-is-valid-or-not-python',
                        'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data']
    wrongUrls = ['hi','www.google','www.apple.com']
    six_fnames = ['a','b','c','d', 'e', 'f']
    two_fnames = ['g', 'h']
    three_fnames = ['1','2','3']
    all_fnames = six_fnames + three_fnames
    duplicate_urls = [url] + [url]
    urls = csv_urls + wrongUrls

    urls_v2 = csv_urls + invalid_csv_urls
    urls_v3 = csv_urls[:3] + invalid_csv_urls + csv_urls[3:]
    all_fnames_v2 = six_fnames + two_fnames
    all_fnames_v3 = six_fnames[:3] + two_fnames + six_fnames[3:]


    def test_assertValueError(self):
        with self.assertRaises(ValueError):
            for url in self.wrongUrls:
                requester.url_to_csv(url, self.all_fnames[0])

    def test_assertTypeError(self):
        with self.assertRaises(TypeError):
            for url in self.invalid_csv_urls:
                requester.url_to_csv(url, self.all_fnames[0])

    # def test_assertWarnings(self):
    #     with self.assertRaisesRegexp(RuntimeWarning, 'Invalid url'):
    #         for url in self.wrongUrls:
    #             requester.batch_url_to_csv(url, self.fnames[0])
        # with warnings.catch_warnings(record=True) as w:
            # print w
            # warnings.simplefilter('always')
            # requester.batch_url_to_csv(self.wrongUrls, self.fnames)
            # requester.fxn()
            # assert len(w) == 1
            # assert issubclass(w[-1].category, RuntimeWarning)

    def test_number_of_files_and_urls(self):
        valid_urls = len(self.csv_urls)
        files = requester.batch_url_to_csv(self.urls, self.all_fnames)
        self.assertEqual(valid_urls, len(files))

    def test_duplicate_urls(self):
        with self.assertRaises(AssertionError):
            requester.batch_url_to_csv(self.duplicate_urls, self.two_fnames)

    def test_correct_number_of_csv(self):
        number_of_csvfiles = len(self.csv_urls)
        files = requester.batch_url_to_csv(self.urls_v2, self.all_fnames_v2)
        self.assertEqual(number_of_csvfiles, len(files))

    def test_csv_content(self):
        files = requester.batch_url_to_csv(self.csv_urls, self.six_fnames)

    def test_correct_filenames(self):
        valid_filenames = self.six_fnames
        files = requester.batch_url_to_csv(self.urls_v3, self.all_fnames_v3)
        for i in range(len(valid_filenames)):
            self.assertEqual(os.path.join(os.getcwd(),valid_filenames[i]),os.path.join(os.getcwd(),files[i]))

    def test_pandas_df_type(self):
        df = requester.url_to_df(self.url)
        self.assertEqual("<class 'pandas.core.frame.DataFrame'>", str(type(df)))

    def test_equal_rows(self):
        df = requester.url_to_df(self.csv_urls[0])
        requester.url_to_csv(self.csv_urls[0], self.fname)
        with open(self.fname, 'r') as csvfile:
            line_num = len(csvfile.readlines())
        self.assertEqual(len(df), line_num)




if __name__ == '__main__':
    unittest.main()
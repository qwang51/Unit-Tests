import unittest
import os
import warnings
import pandas as pd
import requester


class TestStringMethods(unittest.TestCase):

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    duplicate_urls = [url] + [url]
    duplicate_fnames = ['duplicate %d' % i for i in range(len(duplicate_urls))]

    csv_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
               'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data']
    invalid_csv_urls = ['http://stackoverflow.com/questions/19557801/how-to-make-a-function-that-check-if-the-csv-file-is-valid-or-not-python',
                        'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data']
    invalid_urls = ['hi','www.google','www.apple.com']

    csv_fnames = ['test%d.csv' % i for i in range(len(csv_urls))]
    invalid_urls_fnames = ['invalid url%d.csv' % i for i in range(len(invalid_urls))]
    invalid_csv_fnames = ['invalid csv%d.csv' % i for i in range(len(invalid_csv_urls))]

    csv_and_invalid_url_fnames = csv_fnames + invalid_urls_fnames
    csv_and_invalid_urls = csv_urls + invalid_urls

    csv_and_invalid_csv_urls = csv_urls[:3] + invalid_csv_urls + csv_urls[3:]
    csv_and_invalid_csv_fnames = csv_fnames[:3] + invalid_csv_fnames + csv_fnames[3:]


    def test_assertValueError(self):
        with self.assertRaises(ValueError):
            for url in self.invalid_urls:
                requester.url_to_csv(url, self.invalid_urls_fnames[0])

    def test_assertTypeError(self):
        with self.assertRaises(TypeError):
            for url in self.invalid_csv_urls:
                requester.url_to_csv(url, self.invalid_csv_fnames[0])

    def test_assertWarnings(self):
        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter('always')
            requester.batch_url_to_csv(self.invalid_csv_urls, self.invalid_csv_fnames)
            for w in warns:
                self.assertTrue(issubclass(w.category, RuntimeWarning))
        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter('always')
            requester.batch_url_to_csv(self.invalid_urls, self.invalid_urls_fnames)
            for w in warns:
                self.assertTrue(issubclass(w.category, RuntimeWarning))

    def test_number_of_files_and_urls(self):
        valid_urls = len(self.csv_urls)
        files = requester.batch_url_to_csv(self.csv_and_invalid_urls, self.csv_and_invalid_url_fnames)
        self.assertEqual(valid_urls, len(files))

    def test_duplicate_urls(self):
        with self.assertRaises(AssertionError):
            requester.batch_url_to_csv(self.duplicate_urls, self.duplicate_fnames)

    def test_correct_number_of_csv(self):
        number_of_csvfiles = len(self.csv_urls)
        files = requester.batch_url_to_csv(self.csv_and_invalid_csv_urls, self.csv_and_invalid_csv_fnames)
        self.assertEqual(number_of_csvfiles, len(files))

    def test_csv_content(self):
        files = requester.batch_url_to_csv(self.csv_urls, self.csv_fnames)
        dfs = []
        for file in files:
            df = pd.read_csv(file, header=None)
            dfs.append(df)
        for i in range(len(dfs)-1):
            if dfs[i].shape == dfs[i+1].shape:
                self.assertFalse(all(dfs[i]==dfs[i+1]))
            else:
                pass

    def test_correct_filenames(self):
        valid_filenames = self.csv_fnames
        files = requester.batch_url_to_csv(self.csv_and_invalid_csv_urls, self.csv_and_invalid_csv_fnames)
        for i in range(len(valid_filenames)):
            self.assertEqual(os.path.join(os.getcwd(),valid_filenames[i]),os.path.join(os.getcwd(),files[i]))

    def test_pandas_df_type(self):
        df = requester.url_to_df(self.csv_urls[0])
        self.assertEqual("<class 'pandas.core.frame.DataFrame'>", str(type(df)))

    def test_equal_rows(self):
        df = requester.url_to_df(self.csv_urls[0])
        requester.url_to_csv(self.csv_urls[0], self.csv_fnames[0])
        with open(self.csv_fnames[0], 'r') as csvfile:
            line_num = len(csvfile.readlines())
        self.assertEqual(len(df), line_num)


if __name__ == '__main__':
    unittest.main()
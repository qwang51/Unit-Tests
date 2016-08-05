import urllib2
import pandas as pd
import warnings
import os
import csv


def url_to_csv(url, fname):
    """
    Takes a URL to a CSV file, downloads it, and saves it to a file.
    :param url: A url
    :param fname: file name to save the data in the url
    :return: None
    """
    try:
        connection = urllib2.urlopen(url)
    except IOError:
        raise ValueError, 'Invalid url'
    else:
        data = connection.read()
        with open(fname, 'wb') as file:
            file.write(data)
        with open(fname, 'r') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read())
            csvfile.seek(0)
            delimiter = dialect.delimiter
            rows = [line.split(delimiter) for line in csvfile.readlines()]
            if all([len(rows[0])==len(elem) for elem in rows]):
                return
            else:
                os.remove(os.path.join(os.getcwd(),fname))
                raise TypeError, 'Not valid csv format'


def batch_url_to_csv(urls, fnames):
    """
    Takes a list of URLs to CSV files, downloads them,
    and saves them to files given by the list of names in fnames.
    Returns a list of the full path of filenames saved.
    :param urls: list of urls
    :param fnames: list of file names
    :return: full path of filenames saved
    """
    if len(urls) == len(fnames):
        new_urls = set(urls)
        if len(urls) == len(new_urls):
            i = 0
            paths = []
            while i < len(urls):
                try:
                    connection = urllib2.urlopen(urls[i])
                except:
                    warnings.warn('URL %d skipped' %i, RuntimeWarning)
                else:
                    data = connection.read()
                    with open(fnames[i], 'wb') as csvfile:
                        csvfile.write(data)
                    paths.append(os.path.join(os.getcwd(),fnames[i]))
                    with open(fnames[i], 'r') as f:
                        dialect = csv.Sniffer().sniff(f.read())
                        f.seek(0)
                        delimiter = dialect.delimiter
                        rows = [line.split(delimiter) for line in f.readlines()]
                        if all([len(rows[0])==len(elem) for elem in rows]):
                            pass
                        else:
                            warnings.warn('File %d is not CSV format' % i, RuntimeWarning)
                            os.remove(os.path.join(os.getcwd(),fnames[i]))
                            paths.remove(os.path.join(os.getcwd(),fnames[i]))
                i += 1
            return paths
        else: raise AssertionError, "Duplicate URLs cannot be present in the parameter 'urls'."
    else:
        return 'Number of urls and fnames does not match.'


def url_to_df(url):
    """
    Takes a URL to a CSV file and returns the contents of the URL as a
    Pandas DataFrame.
    :param url: A URL
    :return: Pandas DataFrame
    """
    fname = 'pandas.csv'
    url_to_csv(url, fname)
    df = pd.read_csv(fname, header=None)
    return df



url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
f = 'pandas'

urls = ['hi',
        'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data',
       'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data',
        'http://www.h.com']
wrongUrls = ['hi','www.google','www.apple.com']
fnames = ['c1.csv','c2.csv','c3.csv','c4.csv']
wrongurl1 = 'http://www.google.com'
wrongurl2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data'
wrongurl3 = 'hi'
fname = 'a.csv'
commaURL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data'

csv_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
            'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data']
invalid_csv_urls = ['http://stackoverflow.com/questions/19557801/how-to-make-a-function-that-check-if-the-csv-file-is-valid-or-not-python',
                    'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.data']
all_urls = csv_urls + invalid_csv_urls
six_fnames = ['a','b','c','d', 'e', 'f']
two_fnames = ['g', 'h']
all_fnames = six_fnames + two_fnames
duplicate_urls = [url] + [url]
# print len(duplicate_urls)
# print batch_url_to_csv([invalid_csv_urls[0]], [six_fnames[0]])
# print batch_url_to_csv(invalid_csv_urls, two_fnames)
# print url_to_df('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
# def fxn():
#     warnings.warn("deprecated", DeprecationWarning)
#     warnings.warn("deprecated", DeprecationWarning)


# print fxn()
# with warnings.catch_warnings(record=True) as w:
#     warnings.simplefilter('always')
#     batch_url_to_csv(wrongUrls, fnames[:-1])
#     # fxn()
#     print len(w)
#     # assert len(w) == 1
#     for ww in w:
#         # print ww.category
#         print issubclass(ww.category, RuntimeWarning)

# url_to_csv(wrongurl2, fname)
# print batch_url_to_csv(urls, fnames)

# for u in urls:
#     try:
#         connection = urllib2.urlopen(u)
#     except:
#         warnings.warn('Invalid', RuntimeWarning)
#         pass
#     else:
#         print connection
# if IOError:
#     warnings.warn('Invalid URL', RuntimeWarning)
# else:
#     data = connection.read()

# url_to_csv(url, fname)

# with open('edge.csv', 'r') as csvfile:
#     s = csv.Sniffer()
#     d = s.sniff(csvfile.read())
#     csvfile.seek(0)
#     print d.delimiter
#     content = csv.reader(csvfile)
#     c = [line.split(d.delimiter) for line in csvfile.readlines()]
#     for row in c:print row
#     # for i in c[1:]:
#     #     if len(i) > len(c[0]):
#     #         print("found a data row that is longer then the header row.")
#     # blank = re.compile(r'\s*')
#     # for i in c[0]:
#     #     if blank.match(i).end() == len(i):
#     #         print("found an empty header item")
#     l = all([len(c[0])==len(row) for row in c])
#     # print l
#     if l is True:
#         charset = re.compile(r'\w*$')
#         special = True
#         for row in c:
#             # for elem in row:
#             #     if re.match(charset, elem):
#             #         # print elem
#             #         continue
#             #     else:
#             #         print elem, "has special character"
#             special = all([re.match(charset, elem) for elem in row])
#                 # if not re.match(charset, elem):
#                 #     print "Contains special character"
#                 #     break
#                 # else: print "Valid csv"
#         print special, 'specila'
#     else: print "Length not equal"

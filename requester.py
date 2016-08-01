import urllib2
import pandas as pd
import os


def url_to_csv(url, fname):
    """
    Takes a URL to a CSV file, downloads it, and saves it to a file.
    :param url: A url
    :param fname: file name to save the data in the url
    :return: None
    """
    connection = urllib2.urlopen(url)
    data = connection.read()
    with open(fname, 'wb') as csvFile:
        result = csvFile.write(data)
    return result


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
        i = 0
        paths = []
        while i < len(urls):
            url_to_csv(urls[i], fnames[i])
            paths.append(os.path.join(os.getcwd(),fnames[i]))
            i += 1
        return paths
    else:
        return 'Number of urls and fnames does not match.'


def url_to_df(url):
    """
    Takes a URL to a CSV file and returns the contents of the URL as a
    Pandas DataFrame.
    :param url: A URL
    :return: Pandas DataFrame
    """
    fname = 'test.csv'
    url_to_csv(url, fname)
    df = pd.read_csv(fname, header=None)
    return df


# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
# urls = ["https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",
        # "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"]
# r = url_to_csv(url, "test1.csv")
# fnames = ['test1.csv', 'test2.csv']
# print batch_url_to_csv(urls, fnames)
# result = url_to_df(url)
# print result
# x = url_to_csv(url, 'test.csv')
# print x
# p = pd.DataFrame.from_csv(x)
# print type(p)
# result = url_to_df(url)
# print type(result)
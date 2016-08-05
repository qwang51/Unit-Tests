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

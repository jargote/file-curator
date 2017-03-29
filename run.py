#!/usr/bin/python

import getopt
import os
import sys
import logging


def read_dir(path):
    return [os.path.join(path, f) for f in os.listdir(path)]


def only_files(dir_list):
    return [f for f in dir_list if os.path.isfile(f)]


def migrate_to_directories(path):
    for filepath in only_files(read_dir(path)):
        filename = os.path.basename(filepath)
        tmp_filename = '_{}'.format(os.path.basename(filepath))
        tmp_filepath = os.path.join(path, tmp_filename)

        print tmp_filename

        try:
            if not os.path.exists(tmp_filepath):
                os.rename(filepath, tmp_filepath)
            else:
                logging.info('temp file already exists. Skipping: {}'.format(
                    tmp_filename))

            if not os.path.isdir(filepath):
                os.mkdir(filepath)
                os.rename(tmp_filepath, os.path.join(filepath, filename))
            else:
                logging.info(
                    'target director already exists. Skipping: {}'.format(
                        file))
        except Exception as e:
            logging.error(e)

            continue


def main(argv):
    long_options = ('makedirs', )
    basedir = None

    try:
        opts, args = getopt.getopt(argv, "m:", ["makedirs="])
    except getopt.GetoptError:
        print 'run.py -m <path>'

        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-m', '--makedirs'):
            basedir = arg
            if os.path.exists(basedir):
                migrate_to_directories(basedir)
            else:
                print 'Directory does not exists: {}'.format(basedir)







if __name__ == '__main__':
    main(sys.argv[1:])

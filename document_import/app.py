#!/usr/bin/env python3
from os import listdir
from os import rename
from os import makedirs
from shutil import move
from os.path import isfile, join, exists
from word_count import word_count
from file_reader import file_reader
from database_access import database_access
import logging
import time
import os
import _thread


def main():
    counter = word_count()
    filereader = file_reader()
    db_access = database_access()
    # load folder linked to read the word documents
    if(os.environ.get('MONITOREDFOLDER') == None):
        monitoredfolder = './words/'
    else:
        monitoredfolder = os.environ.get('MONITOREDFOLDER')
    while True:

        # List all files in the folder
        onlyfiles = [f for f in listdir(
            monitoredfolder) if isfile(join(monitoredfolder, f))]
        # create log folder
        if not exists(monitoredfolder+'logs/'):
            makedirs(monitoredfolder+'logs/')
        # configure Log
        logging.basicConfig(filename=monitoredfolder +
                            'logs/document_import.log', level=logging.INFO)
        logging.info(str(len(onlyfiles)) + " New Files")
        # Process Single new File if there is one
        if len(onlyfiles) != 0:
            words = filereader.read(onlyfiles[0])
            result = counter.count(words)
            for key in result:
                # update count for each word in the dictionary of the currenct file
                db_access.add_value_to_word_count(key, result[key])

        else:
            time.sleep(60)


if __name__ == "__main__":
    time.sleep(5)
    main()

# sudo docker run --name document-import --network
# dev-net -v $(pwd)/words:/var/docs marcusbianchi/documentimport

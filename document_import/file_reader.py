#!/usr/bin/env python3
import csv
import os
from os import listdir
from os import rename
from os import makedirs
from shutil import move
from os.path import isfile, join,exists

class file_reader:
    def read(self,name):
        #load folder linked to read the word documents
        if(os.environ.get('MONITOREDFOLDER') == None):
            self.monitoredfolder = './words/'
        else:
            self.monitoredfolder = os.environ.get('MONITOREDFOLDER')
        
        #Open CSV to read it's content
        with open( self.monitoredfolder+name, encoding='utf-8', errors='ignore') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            words = []
            #read all itens of all rows
            for row in spamreader:
                for item in row:
                    #remove special characters
                    word =  ''.join(e for e in item if e.isalnum())
                    if(word is not None):
                        words.append(word)
                    else:
                        print(word)
            #create processed folder and moved processed file to it.
            if not exists( self.monitoredfolder+"processed"):
                makedirs( self.monitoredfolder+"processed")
            move( self.monitoredfolder+name,  self.monitoredfolder+"/processed/"+name)

            return words
# -*- coding: UTF-8 -*-
 
# script for splitting text files

# in order to run this, you'll need to put this file into
# the folder where your text files live and type this command:
#
#      $ python txt-split [textfile] [regular expression]

import os
import re
from sys import argv

# library of regex expressions
# \nCHAPTER [A-Z]*\n

#helper function to write to file
#string filename, original text file
#int count, section number
#string text, text to write
def write_file(filename, count, text):
 
    file_out = filename + '_' + format(count,'03d') + '.txt'
    f = open(file_out, 'w')
    print('writing ' + file_out)
    f.write(text)
    f.close()
 
#splits longer text into sections according to a regular
#expression, creates a directory, writes sections to that directory
#string file_in, filename of the longer text
def regex_split(file_in, regex):

    count = 0
    f_in = open(file_in,'r')
    path = file_in[:-4] + '_split'
    text = f_in.read()
    f_in.close()
    
    # make a new directory from the filename
    if path not in os.listdir('.'):
        os.mkdir(path)

    # split long text into array of sections
    sections = re.split(regex,text)

    for section in sections:
        if len(section) > 1:
            #write each section to a new file
            count += 1
            file_out = path + '/' + file_in[:-4]
            write_file(file_out, count, section)

if __name__ == '__main__':
 
    # takes two arguments, the filename and the regular expression
    regex_split(argv[1],argv[2])
# -*- coding: UTF-8 -*-
 
# script for splitting text files according for R's MALLET package

# Note the regular expression needs to be
# wrapped in single quotes
#
#      $ python txt-split-rmallet.py [path to textfile] [prefix] [regex]

import re
from sys import argv

# list of regular possible expressions
# \nCHAPTER [A-Z]*\n
# \n– [A-Z]*

#helper function to append sections to output file
#   string filename, original text file
#   string prefix, header for each section
#   int count, section number
#   string text, text to write
def write_file(filename, prefix, count, text):
    
    header = prefix + '_' + count
    f = open(filename, 'a')
    print('writing ' + header)
    text = text.split('\n')
    f.write('\t'.join([header,header]))
    f.write('\t')
    for line in text:
        f.write(line)
    f.write('\n')
    f.close()
 
#splits longer text into sections according to a regular
#expression, writes sections to single file
#   string file_in, filename of the longer text
#   string prefix, header for each section
#   string regex, regex expression
def regex_split(path_in,prefix,regex):

    count = 0
    f_in = open(path_in,'r')
    path_out = path_in[:-4] + '_sections.txt'

    text = f_in.read()
    f_in.close()
    
    # # split long text into array of sections
    sections = re.split(regex,text)

    for section in sections:
        if len(section) > 1:
    #         #write each section to a new file
            count += 1
            write_file(path_out, prefix, str(count), section)

if __name__ == '__main__':
 
    # outputfile, prefix, regex
    regex_split(argv[1],str(argv[2]),argv[3])
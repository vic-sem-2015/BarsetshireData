# -*- coding: UTF-8 -*-
 
# script for merging text files into a single file formatted according for R's MALLET package
#   usage:
#      $ python txt-merge-rmallet.py [folder path] [path out] [prefix]

import re, os, string
from sys import argv

# merges texts in a file folder into a single documen
#   string path_in, folder path in
#   string file_out, output filename
#   string prefix, string header prefix

def regex_merge(path_in,file_out,prefix):

    count = 1
    f_out = open(file_out, 'a')

    for file in os.listdir(path_in):

        f_in = open('/'.join([path_in,file]),'r')
        text = f_in.readlines()
        f_in.close()

        header = prefix + '_' + str(count)
        print('writing ' + file)
        
        f_out.write('\t'.join([header,header]))
        f_out.write('\t')

        #
        #   comment this line / uncomment the following if you don't want
        #   to strip punctuation
        #
        regex = re.compile('-|–|\n|[%s]' % re.escape(string.punctuation))
        # regex = re.compile('\n')

        for line in text:
            line = re.sub(regex, ' ', line)
            f_out.write(line)
        f_out.write('\n')

        count += 1

    f_out.close()

if __name__ == '__main__':
    
    if len(argv) == 4:
        # folder path, out path, prefix, regex
        regex_merge(argv[1],str(argv[2]),argv[3])
    else:
        print("ERROR : usage -- [folder path] [path out] [prefix]")

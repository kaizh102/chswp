'''
Swap Channels of the .asc format CAN log
argv[1] - input file
argv[2] - new channel mapping
        - example '321' means channel 1 2 3 re-arranged to 3 2 1  [swap 1 & 3]
        -         '213' means channel 1 2 3 re-arranged to 2 1 3  [swap 1 & 2]
'''
import pdb
import sys

InFileName = sys.argv[1]
ch_n = sys.argv[2]      #New Channel Assignment
ch = {
    '1': ch_n[0],
    '2': ch_n[1],
    '3': ch_n[2],
}

OutFileName = InFileName.split('.')
OutFileName[-2] += '_swp'
OutFileName = '.'.join(OutFileName)

with open(InFileName, "r") as infile, open(OutFileName, "w") as outfile:
    for line in infile:
        s_line = line.split()
        s_line[1] = ch.get(s_line[1], s_line[1])
        outfile.write(' '.join(s_line)+'\n')

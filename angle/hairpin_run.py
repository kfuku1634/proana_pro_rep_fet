#!/usr/local/bin/python3

import sys
import subprocess

try:
    in_file  = sys.argv[1]
except:
    print("usage: ./hairpin_run [file] [ex:132+--aa]")
else:
    f = open(in_file,mode = 'r')
    fdata = f.readlines()
    f.close()

    program='hairpin_angle'
    scop_home = "/Users/kouki/db/protein_rep/"

    for line in fdata:
        line_arr = line.split()
#   0        1   2    3     4           5       6     7     8 9   10 11      12      13       14        15    16     17     18 19  20 21
# d4wuia1    8  +++  123  Motif      Barrel   b-c-b b-a-b   p p   23 18   122-125  149-152  171-174   c.1.2.0  7    0.15     0 1    0 1

        sign = line_arr[2]
        order = line_arr[3]
        scop_id  = line_arr[0].split('/')[-1].split('.')[0]
        filename = scop_home + scop_id + ".ent"
        n_sfam = line_arr[16]
        Open_or_Barrel = line_arr[5]
        if Open_or_Barrel == "Barrel":
            continue

        if order=='132':
            strand1=line_arr[12]
            strand2=line_arr[13]
            arrange=line_arr[6].split('-')[1]+line_arr[7].split('-')[1]
        if order=='213':
            strand1=line_arr[13]
            strand2=line_arr[14]
            arrange=line_arr[7].split('-')[1]+line_arr[6].split('-')[1]

        strand1_ini, strand1_end = strand1.split('-')
        strand2_ini, strand2_end = strand2.split('-')

        command = []
        command.append(program)
        command.append(filename)
        command.append(strand1_ini)
        command.append(strand1_end)
        command.append(strand2_ini)
        command.append(strand2_end)
        command.append(n_sfam)
        subprocess.run(command)

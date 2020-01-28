#!/usr/local/bin/python3
import sys
import matplotlib.pyplot as plt

powerpoint_form = False
for i in range(len(sys.argv)):
    if(sys.argv[i] == "-o"):
        outputdir=sys.argv[i+1]
    if(sys.argv[i] == "-p"):
        powerpoint_form = True
try:
    filepath = sys.argv[1]
except:
    print("usage: ./hairpin_angle_calc [hairpin angle data] [option]")
    print("-o image output path")
else:
    f = open(filepath,mode='r')
    fdata = f.readlines()
    f.close()

    minus = 0
    plus = 0
    max_angle = 90
    min_angle = -max_angle
    bins = 45
    interval = int((max_angle - min_angle)/bins)


    left = []
    for k in range(bins):
        left.append(k)

    angle_arr = [0 for k in range(bins)]

#    0                                             1          2      3      4       5
#/Users/kouki/db/pdbstyle-2.07_unit/d1a1va1.ent  258-259   265-268   5  -8.191322  104
    for i in fdata:
        line=i.split()
        input_pdbfile = line[0]
        strand1  = line[1]
        strand2  = line[2]
        loop_len = line[3]
        n_sfam = float(line[5])
        angle  = float(line[4])

        #super family 的な数で規格し角度がどのbinに入るか
        j=0
        for i  in range(min_angle, max_angle , interval):
            if(angle >= i and angle < i + interval):
                angle_arr[j] += 1.0/n_sfam
                 #   if(angle<0):
#                print(exist_gly_angle)
#                print(no_gly_angle)
#                print("\n")
            j += 1


        if(angle < 0):
            #minus+=1.0
            minus+=1.0/n_sfam
        else:
            #plus+=1.0
            plus+=1.0/n_sfam
        #print("{} {}-{} {}".format(input_pdbfile,loop_ini,loop_end,angle))

    print("minus:{} plus:{}".format(minus,plus))

    name=filepath

    fig = plt.figure()
    #  if not powerpoint_form :
    #      plt.title("minus:{:.2f}  plus:{:.2f}".format(minus,plus))
        #plt.title("{} \n minus:{} plus:{}".format(name,minus,plus))
        #plt.title("{} ".format(name))
    plt.axvspan(22.45, 100, color='lightpink', alpha=0.8)
    plt.axvspan(-100, 22.45, color='lightskyblue', alpha=0.8)
    plt.xlim((0,45))
    label=[ i if abs(i)%5==0 else ' ' for i in range(min_angle,max_angle,round((abs(min_angle)+max_angle)/bins)) ]
    angle_arr.append(0)
    label.append(90)
    left.append(bins)
    if powerpoint_form :
        plt.bar(left,angle_arr,color = "red",tick_label= '')
        font_size = 20
        savefile = outputdir + '/' + name.split('/')[-1].split('.')[0] + '_powerpoint.pdf'
    else:
        plt.bar(left,angle_arr,color = "red",tick_label= label)
        font_size = 16
        savefile = outputdir + '/' + name.split('/')[-1].split('.')[0] + '.pdf'
    plt.tick_params(labelsize = font_size)
    plt.xlabel('angle[°]',fontsize = font_size)
    #plt.ylabel('frequency',fontsize = font_size)
    plt.tick_params(labelleft=False)
    plt.tight_layout()
    plt.savefig(savefile,format='pdf',dpi=350)

import matplotlib.pyplot as plt

def main(motif):
    #left=1jump right=hairpinr c:loop a:helix in loop
    cc=0
    ca=0
    ac=0
    aa=0

    hist=[ 0 for _ in range(4)]

    #motif=sys.argv[2]
    order=motif[0:3]
    sign =motif[3:6]

    #d1a6ja_    5  ++-  132  Motif      Open     b-c-b b-c-b   a a   7 15   73-76, 84-90, 106-113   d.112.1.1  12    0.69     -4 -1    0 -2
    with open("/Users/kouki/proana_pro_rep/protein_rep_ig_1jump.nishi", mode='r') as f:
        fdata=f.readlines()
    for i in fdata:
        line=i.split()
        weight=1/float(line[16])
        if line[3]==order and line[2]==sign:
            if   line[6+int(order[:1])-1] == 'b-c-b' and line[7-int(order[:1])+1] == 'b-c-b':
                cc+=weight
                hist[0]+=1
            elif line[6+int(order[:1])-1] == 'b-c-b' and line[7-int(order[:1])+1] == 'b-a-b':
                ca+= weight
                hist[1]+=1
            elif line[6+int(order[:1])-1] == 'b-a-b' and line[7-int(order[:1])+1] == 'b-c-b':
                hist[2]+=1
                ac+= weight
            elif line[6+int(order[:1])-1] == 'b-a-b' and line[7-int(order[:1])+1] == 'b-a-b':
                hist[3]+=1
                aa+= weight

    #  all_count=cc+ca+ac+aa
    #  all_hist=sum(hist)
    all_count=1
    all_hist=1
    data=[cc, ca, ac, aa]
    return data

if __name__ == '__main__':
    res_list=[]
    for i in ['213++-', '132+--']:
        res_arr = main(i)
        res_list.append( [ res_arr[0]+res_arr[1], res_arr[2]+res_arr[3] ] )


    res_list_rate = []
    for i in res_list:
        res_list_rate.append([i[0]/sum(i), i[1]/sum(i)])

    print(res_list_rate)
    fig = plt.figure()
    ax = plt.subplot(111)
    left = [0, 1]
    w=0.1
    plt.tick_params(labelbottom=False)
    ax.bar( left, [ res_list_rate[0][0], res_list_rate[1][0] ], color = "coral",linewidth = w)
    ax.bar( left, [ res_list_rate[0][1], res_list_rate[1][1] ], color = "royalblue", bottom=[ res_list_rate[0][0], res_list_rate[1][0] ],linewidth = w)

    plt.show()





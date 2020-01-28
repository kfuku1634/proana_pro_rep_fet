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
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    left=[ i for i in range(4)]
    data=[cc, ca, ac, aa]
    print(motif)
    print(data)
    print(hist)
    print('\n', end='')
    data=[ i/all_count for i in data]
    hist=[ i/all_hist for i in hist]
    labels=['cc', 'ca', 'ac', 'aa']
    w=0.3
    keys=globals().keys()
    ax.bar(left, data, width=w,label='number of superfamily')
    #ax.bar([i+w for i in range(4)], hist, width=w, label='number of domain')
    ax.set_title('{} arrangement'.format(motif))
    ax.set_xlabel('loop arrangement')
    ax.set_ylabel('rate')

    plt.legend()
    plt.xticks([i+w/2 for i in range(4)], labels)
    plt.tight_layout()
    plt.savefig('loop_arrangement_not_norm{}.pdf'.format(motif))

if __name__ == '__main__':
    for i in ['213++-', '213+--', '132++-', '132+--']:
        main(i)

import matplotlib.pyplot as plt
import sys

def main():
    loop_len132=[ 0 for _ in range(300)]
    loop_len213=[ 0 for _ in range(300)]

    filename=sys.argv[1]
    cutoff=int(sys.argv[2])

    with open(filename, mode='r') as f:
        fdata=f.readlines()
    for i in fdata:
        line=i.split()
        #d12asa_    8  +-+  123  Motif      Open     b-c-b b-a-b   a a   4 35   233-240, 245-254, 290-296   d.104.1.1  80    0.46     -1 -1    0 -3
        weight=1/float(line[16])
        if  line[3]=="132" and line[2]=="+--":
            loop_len132[int(line[10])] += weight
        elif line[3]=="213" and line[2]=="++-":
            loop_len213[int(line[11])] += weight

    loop_len_less132=[]
    loop_len_less213=[]

    for n in range(cutoff):
        loop_len_less132.append(sum(loop_len132[0:n]))
        loop_len_less213.append(sum(loop_len213[0:n]))

    fig=plt.figure()

    ax=fig.add_subplot(1,1,1)
    ax.plot(loop_len_less132, label='132+--')
    ax.plot(loop_len_less213, label='213++-')
    ax.legend()
    ax.grid()
    ax.set_xlabel('loop length')
    ax.set_ylabel('frequency of superfamily')

    plt.tight_layout()
    plt.savefig('dev_loop_length_cutoff.pdf')

if __name__ == '__main__':
    main()

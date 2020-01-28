import matplotlib.pyplot as plt
import sys

def main():
    c_loop_len132=[ 0 for _ in range(300)]
    c_loop_len213=[ 0 for _ in range(300)]
    a_loop_len132=[ 0 for _ in range(300)]
    a_loop_len213=[ 0 for _ in range(300)]
    filename=sys.argv[1]
    with open(filename, mode='r') as f:
        fdata=f.readlines()
    for i in fdata:
        line=i.split()
        #d12asa_    8  +-+  123  Motif      Open     b-c-b b-a-b   a a   4 35   233-240, 245-254, 290-296   d.104.1.1  80    0.46     -1 -1    0 -3
        weight=1/float(line[16])
        if  line[3]=="132" and line[2]=="+--":
            if line[6] == 'b-c-b':
                c_loop_len132[int(line[10])] += weight
            elif line[6] == 'b-a-b':
                a_loop_len132[int(line[10])] += weight
        elif line[3]=="213" and line[2]=="++-":
            if line[7] == 'b-c-b':
                c_loop_len213[int(line[11])] += weight
            elif line[7] == 'b-a-b':
                a_loop_len213[int(line[11])] += weight

    c_loop_len_less132=[]
    c_loop_len_less213=[]
    a_loop_len_less132=[]
    a_loop_len_less213=[]

    for n in range(50):
        c_loop_len_less132.append(sum(c_loop_len132[0:n]))
        c_loop_len_less213.append(sum(c_loop_len213[0:n]))
        a_loop_len_less132.append(sum(a_loop_len132[0:n]))
        a_loop_len_less213.append(sum(a_loop_len213[0:n]))

    fig=plt.figure()

    c_ax=fig.add_subplot(2,1,1)
    c_ax.plot(c_loop_len_less132, label='132+--')
    c_ax.plot(c_loop_len_less213, label='213++-')
    c_ax.set_title('not helix in loop')
    c_ax.legend()
    c_ax.grid()
    c_ax.set_xlabel('loop length')
    c_ax.set_ylabel('frequency of superfamily')

    a_ax=fig.add_subplot(2,1,2)
    a_ax.plot(a_loop_len_less132, label='132+--')
    a_ax.plot(a_loop_len_less213, label='213++-')
    a_ax.set_title('helix in jump loop')
    a_ax.legend()
    a_ax.grid()
    a_ax.set_xlabel('loop and helix length')
    a_ax.set_ylabel('frequency of superfamily')

    plt.tight_layout()
    plt.savefig('anal_loop_helix.pdf')


if __name__ == '__main__':
    main()

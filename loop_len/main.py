import matplotlib.pyplot as plt
import sys
import numpy as np

def main():
    loop_len132_ac=[ 0 for _ in range(300)]
    loop_len132_cc=[ 0 for _ in range(300)]
    loop_len213_ac=[ 0 for _ in range(300)]
    loop_len213_cc=[ 0 for _ in range(300)]

    filename=sys.argv[1]
    cutoff=int(sys.argv[2])
    print('cutoff: {}'.format(cutoff))

    with open(filename, mode='r') as f:
        fdata=f.readlines()
    for i in fdata:
        line=i.split()
        #d12asa_    8  +-+  123  Motif      Open     b-c-b b-a-b   a a   4 35   233-240, 245-254, 290-296   d.104.1.1  80    0.46     -1 -1    0 -3
        weight=1/float(line[16])
        if    line[3]=="132" and line[2]=="++-" and line[6]=='b-a-b' and line[7]=='b-c-b':
            loop_len132_ac[int(line[10])] += weight
        elif  line[3]=="132" and line[2]=="++-" and line[6]=='b-c-b' and line[7]=='b-c-b':
            loop_len132_cc[int(line[10])] += weight
        elif  line[3]=="213" and line[2]=="+--" and line[7]=='b-a-b' and line[6]=='b-c-b':
            loop_len213_ac[int(line[11])] += weight
        elif  line[3]=="213" and line[2]=="+--" and line[7]=='b-c-b' and line[6]=='b-c-b':
            loop_len213_cc[int(line[11])] += weight


    fig=plt.figure()
    ax_ac=fig.add_subplot(211)
    loop_len213_cc= np.array(loop_len213_cc)/sum(loop_len213_cc)
    loop_len213_ac= np.array(loop_len213_ac)/sum(loop_len213_ac)
    loop_len132_cc= np.array(loop_len132_cc)/sum(loop_len132_cc)
    loop_len132_ac= np.array(loop_len132_ac)/sum(loop_len132_ac)

    print(np.argmax(loop_len132_ac+loop_len213_ac))

    ax_ac.plot(loop_len132_ac[:cutoff], label='132++-')
    ax_ac.plot(loop_len213_ac[:cutoff], label='213+--')

    ax_cc=fig.add_subplot(212)
    ax_cc.plot(loop_len132_cc[:cutoff], label='132++-')
    ax_cc.plot(loop_len213_cc[:cutoff], label='213+--')

    ax_cc.set_xlabel('cc loop length')
    ax_ac.set_xlabel('ac loop length')
    for i in [ax_ac, ax_cc]:
        i.legend()
        i.grid()
        i.set_ylabel('frequency of superfamily')

    plt.title('loop length cutoff {}'.format(cutoff))
    plt.tight_layout()
    plt.savefig('1jump_not_helix_loop_len_cotoff{}.pdf'.format(cutoff))

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]
cutoff   = int(sys.argv[2])
with open(filename,mode='r') as f:
    fdata=f.readlines()

strand_helix_loop_arr=[0 for _ in range(200)]
helix_strand_loop_arr=[0 for _ in range(200)]
helix_length_arr     =[0 for _ in range(200)]

sum_n_fam=0
for i in fdata:
    line=i.split()
    if(len(line)!=6):
        continue

    n_sfam     = int(line[1])
    strand_end = int(line[2])
    helix_ini  = int(line[3])
    helix_end  = int(line[4])
    strand_ini = int(line[5])

    strand_helix_loop = helix_ini-strand_end-1
    helix_strand_loop = strand_ini-helix_end-1
    helix_length      = helix_end-helix_ini+1

    strand_helix_loop_arr[strand_helix_loop]+=1/n_sfam
    helix_strand_loop_arr[helix_strand_loop]+=1/n_sfam
    helix_length_arr[helix_length]+=1/n_sfam

fig=plt.figure()
ax_s_h=fig.add_subplot(221)
ax_h_s=fig.add_subplot(223)
ax_h  =fig.add_subplot(222)

left=[ i for i in range(cutoff)]
ax_s_h.bar(left,strand_helix_loop_arr[0:cutoff])
ax_s_h.set_title("loop from strand to helix")
ax_s_h.set_xlabel("loop length")
ax_s_h.set_ylabel("frequency of superfamily")
ax_h_s.bar(left,helix_strand_loop_arr[0:cutoff])
ax_h_s.set_title("loop form helix to strand")
ax_h_s.set_xlabel("loop length")
ax_h_s.set_ylabel("frequency of superfamily")
ax_h.bar(left,helix_length_arr[0:cutoff])
ax_h.set_title("helix length")
ax_h.set_xlabel("helix length")
ax_h.set_ylabel("frequency of superfamily")

plt.tight_layout()
plt.savefig("{}.pdf".format(filename.split('.')[0]))

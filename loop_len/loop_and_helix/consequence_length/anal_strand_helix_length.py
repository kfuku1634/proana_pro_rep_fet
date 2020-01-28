import matplotlib.pyplot as plt
import sys
import matplotlib.ticker as ticker

loop_helix_filename = sys.argv[1]
strand_len_cutoff   = int(sys.argv[2])
with open(loop_helix_filename,mode='r') as f:
    fdata=f.readlines()

with open("/Users/kouki/proana_pro_rep/protein_rep.nishi", mode="r") as f_nishi:
    f_nishi_data=f_nishi.readlines()
dic={}
for i in fdata:
    line=i.split()
    if(len(line)!=6):
        continue

    scop_id    = line[0]
    for nishi_i in f_nishi_data:
        nishi_line=nishi_i.split()
        nishi_line_scop_id = nishi_line[0]
        nishi_line_order   = nishi_line[3]
        if nishi_line_order == "213":
            strand1 = nishi_line[13][:-1]
            strand2 = nishi_line[14]
        elif nishi_line_order == "132":
            strand1 = nishi_line[12][:-1]
            strand2 = nishi_line[13][:-1]
    strand1_len=int(strand1.split('-')[1])-int(strand1.split('-')[0])
    strand2_len=int(strand2.split('-')[1])-int(strand2.split('-')[0])
    if strand1_len <= strand_len_cutoff or strand2_len <= strand_len_cutoff:
        continue
    n_sfam     = int(line[1])
    strand_end = int(line[2])
    helix_ini  = int(line[3])
    helix_end  = int(line[4])
    strand_ini = int(line[5])

    strand_helix_loop = helix_ini-strand_end-1
    helix_strand_loop = strand_ini-helix_end-1
    helix_length      = helix_end-helix_ini+1
    print("{}   {}-{}-{} ini:{} end:{}".format(scop_id, strand_helix_loop,helix_length,helix_strand_loop, strand_end, strand_ini))

    if "{}-{}-{}".format(strand_helix_loop,helix_length,helix_strand_loop) not in dic:
        dic["{}-{}-{}".format(strand_helix_loop,helix_length,helix_strand_loop)] =1/n_sfam
    else:
        dic["{}-{}-{}".format(strand_helix_loop,helix_length,helix_strand_loop)] +=1/n_sfam

#print(dic)
#print(dic.values())
#print(dic.keys())
arr = sorted(dic.items(), key=lambda x:-x[1])
values_arr=[]
keys_arr=[]
#上から２０こ表示
cutoff_ranking=20
for n,i in enumerate(arr):
    if n==20:
        break
    keys_arr.append(i[0])
    values_arr.append(i[1])

fig=plt.figure()
ax  =fig.add_subplot(111)
ax.bar(range(len(values_arr)), values_arr, tick_label=keys_arr)
ax.set_title("loop from strand to strand")
ax.set_xlabel("loop-helix-loop length")
ax.set_ylabel("frequency of superfamily")
plt.tick_params(rotation=90)
#fig.subplots_adjust(bottom = 0.6)
#fig.subplots_adjust(top = 0.9)
plt.tight_layout()
plt.savefig("img/{}_consequence_lim{}.pdf".format(loop_helix_filename.split('.')[0].split('/')[-1], strand_len_cutoff))

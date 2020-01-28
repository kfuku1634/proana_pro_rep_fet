import matplotlib.pyplot as plt
import sys

def extract_superfamily_id(scop_id):
    superfamily_arr=[]
    for n,i in enumerate(scop_id.split('.')):
        superfamily_arr.append(i)
        if n==2:
            break
    return '.'.join(superfamily_arr)

def extract_fold_id(scop_id):
    fold_arr=[]
    for n,i in enumerate(scop_id.split('.')):
        fold_arr.append(i)
        if n==1:
            break
    return '.'.join(fold_arr)

def calc(nishi_filename, superfold_cutoff):
    fold_132_dic={}
    fold_213_dic={}
    scop_id_arr132=[]
    scop_id_arr213=[]
    with open(nishi_filename, mode='r') as f:
        fdata=f.readlines()
    for i in fdata:
        line=i.split()
        sign=line[2]
        order=line[3]
        scop_id=line[15]
        fold_id = extract_fold_id(scop_id)
        weight=1/float(line[16])
        if order=="213" and sign=="++-":
            if scop_id in scop_id_arr213:
                continue
            scop_id_arr213.append(scop_id)
            if fold_id in fold_213_dic:
                fold_213_dic[fold_id] += weight
            else:
                fold_213_dic[fold_id] = weight
        elif order=="132" and sign=="+--":
            if scop_id in scop_id_arr132:
                continue
            scop_id_arr132.append(scop_id)
            if fold_id in fold_132_dic:
                fold_132_dic[fold_id] += weight
            else:
                fold_132_dic[fold_id] = weight

    fold_132_dic_cutoff=[ [k, v] for k, v in fold_132_dic.items() if v > superfold_cutoff]
    fold_213_dic_cutoff=[ [k, v] for k, v in fold_213_dic.items() if v > superfold_cutoff]

    print(fold_132_dic_cutoff)
    print(fold_213_dic_cutoff)

    #with open("/Users/kouki/presen/pssj2019/n_sup.dat") as f:
    #    fdata=f.readlines()

    #print("132")
    #for i in fdata:
    #    line=i.split()
    #    fold_id=line[0]
    #    if fold_id in fold_132_dic.keys():
    #        print(i,end='')

    #print("213")
    #for i in fdata:
    #    line=i.split()
    #    fold_id=line[0]
    #    if fold_id in fold_213_dic.keys():
    #        print(i,end='')

if __name__ == "__main__":
    nishi_filename=sys.argv[1]
    superfold_cutoff=float(sys.argv[2])
    calc(nishi_filename,superfold_cutoff)

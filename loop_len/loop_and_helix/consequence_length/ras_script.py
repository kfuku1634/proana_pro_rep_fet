import sys
import subprocess

def show_ras_script(scop_id):
    for i in f_hoge_data:
        f_hoge_line=i.split()
        if scop_id == f_hoge_line[0]:
            strand_ini=f_hoge_line[2].split(":")[1]
            strand_end=f_hoge_line[3].split(":")[1]
            with open("tmp.ras",mode='w') as f_tmp_ras:
                f_tmp_ras.write("load {}".format("/Users/kouki/db/protein_rep/{}.ent\n".format(scop_id)))
                f_tmp_ras.write("wireframe off\n")
                f_tmp_ras.write("color group\n")
                f_tmp_ras.write("cartoon on\n")
                f_tmp_ras.write("select {} and *.cb\n".format(strand_ini))
                f_tmp_ras.write("spacefill on\n")
                f_tmp_ras.write("select {} and *.cb\n".format(strand_end))
                f_tmp_ras.write("spacefill on\n")
    print(scop_id)
    subprocess.call(["rasmol","-script","tmp.ras"])


if __name__ == "__main__":
    hoge_file_name = sys.argv[1]
    with open(hoge_file_name, mode="r") as f_hoge:
        f_hoge_data=f_hoge.readlines()
    for i in f_hoge_data:
        f_hoge_line=i.split()
        scop_id=f_hoge_line[0]
        if scop_id == "python3":
            continue
        show_ras_script(scop_id)

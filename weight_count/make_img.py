import subprocess

def make_dist( psi_or_phi ):
    freq_all        = 0
    infreq_all      = 0
    freq_motif      = 0
    freq_topology   = 0
    infreq_motif    = 0
    infreq_topology = 0

    if psi_or_phi == "psi":
        freq_filename   = "213++-.fet"
        infreq_filename = "132+--.fet"

    if psi_or_phi == "phi":
        freq_filename   = "132++-.fet"
        infreq_filename = "213+--.fet"

    for i in fdata:
        line =i.split()
        fet_filename = line[0]
        if fet_filename == freq_filename:
            freq_all        = float(line[1])
            freq_motif      = float(line[2])
            freq_topology   = float(line[3])
        if fet_filename == infreq_filename:
            infreq_all      = float(line[1])
            infreq_motif    = float(line[2])
            infreq_topology = float(line[3])

    subprocess.run( [ "bar.py", "./img/{}_dist_all.pdf".format(psi_or_phi), "{}".format(freq_all), "{}".format(infreq_all) ] )
    subprocess.run( [ "bar.py", "./img/{}_dist_motif.pdf".format(psi_or_phi), "{}".format(freq_motif), "{}".format(infreq_motif) ] )
    subprocess.run( [ "bar.py", "./img/{}_dist_topology.pdf".format(psi_or_phi), "{}".format(freq_topology), "{}".format(infreq_topology) ] )

with open("./weight.txt") as f:
    fdata=f.readlines()

make_dist("psi")
make_dist("phi")


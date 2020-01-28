import sys

filename = sys.argv[1]
with open( filename , mode='r') as f: 
    fdata =f.readlines()

pdb_files          = []
pdb_files_Motif    = []
pdb_files_Topology = []
weight             = 0
weight_Motif       = 0
weight_Topology    = 0

for i in fdata:
    line = i.split()

    pdb_file = line[0]
    Motif_or_Topology = line[4]

    if not pdb_file in pdb_files:
        pdb_files.append( pdb_file )
        weight += 1/float(line[16])

    if Motif_or_Topology == "Motif":
        if not pdb_file in pdb_files_Motif:
            pdb_files_Motif.append( pdb_file )
            weight_Motif += 1/float(line[16])

    if Motif_or_Topology == "Topology":
        if not pdb_file in pdb_files_Topology:
            pdb_files_Topology.append( pdb_file )
            weight_Topology += 1/float(line[16])

print("{} {:.4f} {:.4f} {:.4f}".format(filename[3:], weight, weight_Motif, weight_Topology))


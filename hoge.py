
R=L=N=0
for i in open( "132++-_ax.fet" ):
    line = i.split()
    chirality = line[ -5 ]
    weight=1/float(line[16])
    if ( chirality == "R" ):
        R+=weight
    elif( chirality == "L"):
        L+=weight
    else:
        N+=weight

print(R, L, N)

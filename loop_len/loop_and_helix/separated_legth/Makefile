TARGET=img/loop_and_helix_1jump_NOT_cross_ax_sepqrated.pdf img/loop_and_helix_1jump_cross_ax_separated.pdf data/loop_and_helix_1jump_cross_ax.dat data/loop_and_helix_1jump_NOT_cross_ax.dat

all:$(TARGET)

img/loop_and_helix_1jump_NOT_cross_ax_sepqrated.pdf: data/loop_and_helix_1jump_NOT_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_NOT_cross_ax.dat 25

img/loop_and_helix_1jump_cross_ax_separated.pdf: data/loop_and_helix_1jump_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_cross_ax.dat 25

data/loop_and_helix_1jump_NOT_cross_ax.dat: ~/proana_pro_rep/1jump_NOT_cross_ax.nishi ~/bin/length_loop_helix
	~/bin/length_loop_helix ~/proana_pro_rep/1jump_NOT_cross_ax.nishi >data/loop_and_helix_1jump_NOT_cross_ax.dat
data/loop_and_helix_1jump_cross_ax.dat: ~/proana_pro_rep/1jump_cross_ax.nishi ~/bin/length_loop_helix
	~/bin/length_loop_helix ~/proana_pro_rep/1jump_cross_ax.nishi >data/loop_and_helix_1jump_cross_ax.dat

clean:
	rm $(TARGET)

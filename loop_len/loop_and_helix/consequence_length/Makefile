TARGET=img/loop_and_helix_1jump_NOT_cross_ax_consequence.pdf img/loop_and_helix_1jump_cross_ax_consequence.pdf img/loop_and_helix_1jump_cross_ax_consequence_lenlim_2.pdf img/loop_and_helix_1jump_NOT_cross_ax_consequence_lenlim_2.pdf

all:$(TARGET)

img/loop_and_helix_1jump_cross_ax_consequence_lenlim_2.pdf: data/loop_and_helix_1jump_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_cross_ax.dat 2

img/loop_and_helix_1jump_NOT_cross_ax_consequence_lenlim_2.pdf: data/loop_and_helix_1jump_NOT_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_NOT_cross_ax.dat 2

img/loop_and_helix_1jump_NOT_cross_ax_consequence.pdf: data/loop_and_helix_1jump_NOT_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_NOT_cross_ax.dat 0

img/loop_and_helix_1jump_cross_ax_consequence.pdf: data/loop_and_helix_1jump_cross_ax.dat ./anal_strand_helix_length.py
	python3 anal_strand_helix_length.py data/loop_and_helix_1jump_cross_ax.dat 0

loop_and_helix_1jump_NOT_cross_ax.dat: ~/proana_pro_rep/1jump_NOT_cross_ax.nishi ~/bin/length_loop_helix
	~/bin/length_loop_helix ~/proana_pro_rep/1jump_NOT_cross_ax.nishi >loop_and_helix_1jump_NOT_cross_ax.dat
loop_and_helix_1jump_cross_ax.dat: ~/proana_pro_rep/1jump_cross_ax.nishi ~/bin/length_loop_helix
	~/bin/length_loop_helix ~/proana_pro_rep/1jump_cross_ax.nishi >loop_and_helix_1jump_cross_ax.dat
clean:
	rm $(TARGET)

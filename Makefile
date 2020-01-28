TARGET=\
protein_rep_ig_1jump_cross.fet \
protein_rep_ig_1jump_not_cross.fet \
1jump_NOT_cross_ax.fet \
1jump_cross_ax.fet \
1jump_NOT_cross_cx.fet \
1jump_cross_cx.fet\
./4/protein_rep_4_ig.fet \
./2/protein_rep_2_ig.fet \
132+--_ax_L.fet

all:$(TARGET)

132+--_ax_L.fet :  132+--_ax.fet
	./make.sh

1jump_cross_cx.fet: 213++-_cx.fet 132+--_cx.fet
	cat 213++-_cx.fet 132+--_cx.fet > 1jump_cross_cx.fet

1jump_NOT_cross_cx.fet: 213+--_cx.fet 132++-_cx.fet
	cat 213+--_cx.fet 132++-_cx.fet > 1jump_NOT_cross_cx.fet

213++-_cx.fet: 213++-_cc.fet 213++-_ca.fet
	cat 213++-_cc.fet 213++-_ca.fet > 213++-_cx.fet

132+--_cx.fet:132+--_cc.fet 132+--_ca.fet
	cat 132+--_cc.fet 132+--_ca.fet > 132+--_cx.fet

213+--_cx.fet: 213+--_cc.fet 213+--_ca.fet
	cat 213+--_cc.fet 213+--_ca.fet > 213+--_cx.fet

132++-_cx.fet:132++-_cc.fet 132++-_ca.fet
	cat 132++-_cc.fet 132++-_ca.fet > 132++-_cx.fet


1jump_cross_ax.fet: 213++-_ax.fet 132+--_ax.fet
	cat 213++-_ax.fet 132+--_ax.fet > 1jump_cross_ax.fet

1jump_NOT_cross_ax.fet: 213+--_ax.fet 132++-_ax.fet
	cat 213+--_ax.fet 132++-_ax.fet > 1jump_NOT_cross_ax.fet

213++-_ax.fet: 213++-_ac.fet 213++-_aa.fet
	cat 213++-_ac.fet 213++-_aa.fet > 213++-_ax.fet

132+--_ax.fet:132+--_ac.fet 132+--_aa.fet
	cat 132+--_ac.fet 132+--_aa.fet > 132+--_ax.fet

213+--_ax.fet: 213+--_ac.fet 213+--_aa.fet
	cat 213+--_ac.fet 213+--_aa.fet > 213+--_ax.fet

132++-_ax.fet:132++-_ac.fet 132++-_aa.fet
	cat 132++-_ac.fet 132++-_aa.fet > 132++-_ax.fet

protein_rep_ig_1jump_cross.fet: protein_rep_ig_1jump.fet
	grep -e '++-  213' -e '+--  132' protein_rep_ig_1jump.fet>protein_rep_ig_1jump_cross.fet

protein_rep_ig_1jump_not_cross.fet: protein_rep_ig_1jump.fet
	grep -e '+--  213' -e '++-  132' protein_rep_ig_1jump.fet>protein_rep_ig_1jump_not_cross.fet

protein_rep_ig_1jump.fet : protein_rep_ig.fet
	grep -e '+--  213' -e '++-  213' -e '+--  132' -e '++-  132' protein_rep_ig.fet>protein_rep_ig_1jump.fet

./4/protein_rep_4_ig.fet : ./4/protein_rep_4.fet ./4/make.sh
	grep -v -e 'b-b-b' -e "b'" -e "b-ab-b" ./4/protein_rep_4.fet > ./4/protein_rep_4_ig.fet
	./4/make.sh

./2/protein_rep_2_ig.fet : ./2/protein_rep_2.fet ./2/make.sh
	grep -v -e 'b-b-b' -e "b'" -e "b-ab-b" ./2/protein_rep_2.fet > ./2/protein_rep_2_ig.fet
	./2/make.sh

protein_rep_ig.fet : protein_rep.fet 
	grep -v -e 'b-b-b' -e "b'" -e "b-ab-b" protein_rep.fet > protein_rep_ig.fet

clean:
	rm $(TARGET)

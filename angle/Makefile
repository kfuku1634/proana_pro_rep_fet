#SRC=$(shell ls ../*.nishi | grep -v "protein" | grep -v "jump")
SRC=$(shell ls ../*.fet | grep -v "protein_rep.fet" | grep -v "protein_rep_ig.fet")
TARGET_temp=$(SRC:.fet=.eps)
TARGET=$(notdir $(TARGET_temp))

.SUFFIXES: .eps .fet .dat

.PHONY: all
all : $(TARGET)

%.eps : ./data/%.dat ./hairpin_data_anal_for_simu_this_dir.py ./hairpin_run.py
	python3 hairpin_data_anal_for_simu_this_dir.py $< -o img 
	python3 hairpin_data_anal_for_simu_this_dir.py $< -o img -p

./data/%.dat : ../%.fet
	python3 hairpin_run.py $<  >$@

echo:
	@echo $(SRC)
	@echo $(TARGET)
clean:
	rm $(TARGET)

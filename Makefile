GPX_DIR = ~/Documents/jonnyrobbie-cgeo-history/*
BACKGROUND = flag
FILES = kopecky-cz-v2 kopecky-sk-v2 rekordy-cz-v2 hrady-sk-v2 hrady-cz-v2 kostely-sk-v2 kostely-cz-v2 rozhledny-cz-v2 hrady-hu-v2 jeskyne-sk-v2 summits-v2 zamky-cz-v2 tatry-v2 rozhledny-sk-v2 pivovary-cz-v2 bazalt-v2 domy-cz-v2 krize-v2 unesco-de-v2 hrady-si-v2

kopecky-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p1 -b $(BACKGROUND) $(GPX_DIR) > kopecky-cz-v2
kopecky-sk-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p2 -b $(BACKGROUND) $(GPX_DIR) > kopecky-sk-v2
rekordy-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p3 -b $(BACKGROUND) $(GPX_DIR) > rekordy-cz-v2
hrady-sk-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p4 -b $(BACKGROUND) $(GPX_DIR) > hrady-sk-v2
hrady-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p5 -b $(BACKGROUND) $(GPX_DIR) > hrady-cz-v2
kostely-sk-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p6 -b $(BACKGROUND) $(GPX_DIR) > kostely-sk-v2
kostely-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p7 -b $(BACKGROUND) $(GPX_DIR) > kostely-cz-v2
rozhledny-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p9 -b $(BACKGROUND) $(GPX_DIR) > rozhledny-cz-v2
hrady-hu-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p10 -b $(BACKGROUND) $(GPX_DIR) > hrady-hu-v2
jeskyne-sk-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p11 -b $(BACKGROUND) $(GPX_DIR) > jeskyne-sk-v2
summits-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p12 -b $(BACKGROUND) $(GPX_DIR) > summits-v2
zamky-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p13 -b $(BACKGROUND) $(GPX_DIR) > zamky-cz-v2
tatry-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p14 -b $(BACKGROUND) $(GPX_DIR) > tatry-v2
rozhledny-sk-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p15 -b $(BACKGROUND) $(GPX_DIR) > rozhledny-sk-v2
pivovary-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p16 -b $(BACKGROUND) $(GPX_DIR) > pivovary-cz-v2
bazalt-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p17 -b $(BACKGROUND) $(GPX_DIR) > bazalt-v2
domy-cz-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p18 -b $(BACKGROUND) $(GPX_DIR) > domy-cz-v2
krize-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p19 -b $(BACKGROUND) $(GPX_DIR) > krize-v2
unesco-de-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p20 -b $(BACKGROUND) $(GPX_DIR) > unesco-de-v2
hrady-si-v2: $(GPX_DIR) 
	./geopuzzle-gen.py -p21 -b $(BACKGROUND) $(GPX_DIR) > hrady-si-v2
all: $(FILES)
	cat $(FILES) > all_puzzles
clean:
	rm $(FILES) all_puzzles

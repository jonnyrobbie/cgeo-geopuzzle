#!/usr/bin/python
from xml.etree import ElementTree as ET
from pyquery import PyQuery as pq
import os, argparse, logging, urllib.request, sys, math

server = "http://www.geotrophy.net/GeoPuzzle/?puzzle="
image_names = ["kopecky-cz-v2", "kopecky-sk-v2", "rekordy-cz-v2", "hrady-sk-v2", "hrady-cz-v2", "kostely-sk-v2", "kostely-cz-v2", None, "rozhledny-cz-v2", "hrady-hu-v2", "jeskyne-sk-v2", "summits-v2", "zamky-cz-v2", "tatry-v2", "rozhledny-sk-v2", "pivovary-cz-v2", "bazalt-v2", "domy-cz-v2", "krize-v2", "unesco-de-v2", "hrady-si-v2"]
background_names = {"bw": "background2", "gray": "background4", "blue": "background6", "green": "background8", "flag": "background9"}
image_size = 72
vcount = {2: logging.DEBUG,
		  1: logging.INFO,
		  None: logging.WARNING}

# argument parser
parser = argparse.ArgumentParser(description='Generates GeoPuzzle code from C:GEO exported files. http://www.geotrophy.net/')
parser.add_argument("-p", "--puzzle", help="Selects the puzzle.", type=int, required=True)
parser.add_argument("-b", "--background", help="Selects GeoPuzzle background.", action="store", choices=["bw", "gray", "blue", "green", "flag"], default="bw")
parser.add_argument("-v", "--verbose", help="Verbose output.", action="count")
parser.add_argument('gpx', nargs='+', help="GPX files exported from c:geo")
args = parser.parse_args()

logging.basicConfig(level=vcount[args.verbose])

# puzzle page scraping
## scrape webpage
def urlname():
	return server + str(args.puzzle)

try:
	logging.info("Retrieving: %s", urlname())
	response = urllib.request.urlopen(urlname())
	logging.info("Done")
	logging.debug("HTTP Response: %s", str(response.getcode()))
except urllib.error.HTTPError:
	logging.warning("HTTP Error %s", str(sys.exc_info))
	
puzzle_page = response.read().decode('utf-8')

## parse webpage
puzzle_parse = pq(puzzle_page)
puzzle_title = puzzle_parse("#plocha .hlavni").html()
logging.info("Puzzle title: %s", puzzle_title)
try:
	table_parse = "<table>" + puzzle_parse("#form .tab.full").html() + "</table>"
except TypeError:
	logging.error("Invalid puzzle page.")
	sys.exit(1)
logging.debug(table_parse)
table_tree = ET.fromstring(table_parse)
puzzle_caches = []
puzzle_caches_title = []

for tr in table_tree:
	for a in tr.findall(".//td/a"):
		logging.debug(a.attrib["href"][18:])
		puzzle_caches.append(a.attrib["href"][18:])
	for puzzle_name in tr.findall(".//*[@class='bold']"):
		puzzle_caches_title.append(puzzle_name.text)
logging.info("Parsed caches from GeoPuzzle page:")
logging.info(puzzle_caches)
logging.info(puzzle_caches_title)

# gpx scrapping
logging.info("Parsing C:GEO gpx files")
ns = {"tg": "http://www.topografix.com/GPX/1/0"}
found_caches = []
for filename in args.gpx:
	logging.debug(filename)
	tree = ET.parse(filename)
	gpx = tree.getroot()
	for wpt in gpx:
		if wpt.find('tg:sym', ns).text == "Geocache Found":
			found_caches.append(wpt.find('tg:name', ns).text)
logging.info("Found caches:")
logging.info(found_caches)
common_caches = set(puzzle_caches).intersection(found_caches)
logging.debug(common_caches)
logging.info("Found GeoPuzzle caches: %i",len(common_caches))

# generating code
logging.info("Generating GeoPuzzle html code...")
def coords(index):
	x = (index) % 9
	y = math.floor((index) / 9)
	return x, y

## generating common mouseover blanks
geopuzzle_code = ""
for i in range(35):
	geopuzzle_code = geopuzzle_code + "<div style=\"float:left; overflow: hidden; width:72px; height: 72px; cursor: help;\" title=\"" + puzzle_caches_title[i] + "\">&nbsp;</div>"
geopuzzle_code = "<div style=\"width: 669px; height: 305px; padding: 19px 0 0 19px;\">" + geopuzzle_code + "</div><a href=\"http://www.geotrophy.net/GeoPuzzle/?puzzle=" + str(args.puzzle) + "\" style=\"float:left; overflow: hidden; width:72px; height: 72px; cursor: pointer;\" title=\"GeoPuzzle " + str(puzzle_title) + "\">&nbsp;</a>"

## generating found caches
for cache in common_caches:
	cache_index = puzzle_caches.index(str(cache))
	logging.debug("Cache index: %i (%s)", cache_index, puzzle_caches_title[cache_index])
	x, y = coords(cache_index)
	geopuzzle_code = "<div style=\"background: transparent url(http://www.geotrophy.net/content/" + image_names[args.puzzle-1] + "/" + str(int(cache_index + 1)) + ".png) no-repeat " + str(image_size*x) + "px " + str(image_size*y) + "px \">" + geopuzzle_code + "</div>"
	
## generating the rest of the envelope
geopuzzle_code = "<h3 style=\"margin-bottom:0; padding-bottom: 0; text-align:center;\">GeoPuzzle " + str(puzzle_title) + "</h3><!-- START GP " + str(puzzle_title) + " --><div style=\"width: 688px; height: 324px;  background: transparent url(http://www.geotrophy.net/content/" + image_names[args.puzzle-1] + "/" + background_names[args.background] + ".png) no-repeat 0 0;  margin: 10px  auto;\" >" + geopuzzle_code + "</div><!-- END GP " + str(puzzle_title) + " -->"
logging.debug("Coords: ")
for i in range(35):
	logging.debug(coords(i))
print(geopuzzle_code)

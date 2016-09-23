import urllib
import urllib.request

url = 'http://battleship:8000/cacheTest/dis-v2/trees_4326_auto_thinning_kdtree/layers/0/nodes/root'

doc = urllib.request.urlopen(url).read().decode('utf-8')

print(doc)


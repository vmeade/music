#!/usr/bin/python
import sys
import urllib3
import re

http = urllib3.PoolManager()
r = http.request('GET',str(sys.argv[1]))

if r.status == 200:
	x = re.search("midiUrl&quot;:&quot;https://musescore.com/static/musescore/scoredata/gen/.*score.mid",str(r.data))
	print(x.group())
else:
	print("Bad URL")
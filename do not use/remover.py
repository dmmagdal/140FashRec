# remove all files in a folder that's too full

import sys, os

os.chdir(sys.argv[1])

directList = os.listdir()
for file in directList:
	os.remove(file)
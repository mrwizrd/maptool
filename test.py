import os
import sys
import getopt
from shutil import copyfile

# return to former state (rm !(*.old) then *.old -> *)
def revert(filepath):
	# for each file in the directory
	for file in os.listdir(filepath):
		# if we have an "oldfile" (created by add)
		if file.endswith(".old"):
			# remove the current file if one exists
			rmfile = file[0:file.rfind(".old")]
			if rmfile in os.listdir(filepath):
				os.remove(rmfile)
			# and make the oldfile the current file
			os.rename(file,rmfile)
		# if you don't have an old file... currently I don't do anything to be safe
		# you could choose to remove the file regardless... but I don't like that.

# switch curr to new (*->*.old then curr->*)
def add(filepath,mapdir):
	# for each file in the map directory / for each map we want to add
	mapname = mapdir[mapdir.rfind('/'):len(mapdir)]
	for f in os.listdir(mapdir):
		# if this file is a dds file
		if f.rfind('.dds') == len(f)-4:
			# if we are already storing an old file don't keep this one... sorry but I want to save the originals not your mistakes
			# if you ever accidentally save over the originals then you can always get them back from the 0.9.15/ directory
			if not os.path.exists(filepath+"mmap.dds.old") and os.path.exists(filepath+"mmap.dds"):
				copyfile(filepath+"mmap.dds",filepath+"mmap.dds.old")
			# and put our map there
			copyfile(mapdir+"/"+f,filepath+"mmap.dds")
		else:
			# otherwise yell at the user for being an idiot
			print "Warning! File ",f," is not a map. It won't be added. Deal with it."

def create_dirs(filepath,dirs):
	for directory in dirs:
		if not os.path.exists(filepath+"/"+directory):
			os.makedirs(filepath+"/"+directory)

def main():
	command = raw_input('Add or Revert?(a/r): ')
	wotdir = raw_input('Path to WOT: ')
	# getting the path we need
	wotdir = wotdir.replace("\\","/")+"/res_mods/0.9.15.0.1/spaces/"
	# get a list of the maps currently in game from a local file
	maps = []
	with open('maps_list.txt') as f:
		maps = f.read().splitlines()
    # create the directories if they don't already exist
	create_dirs(wotdir,maps)
    # if we want to add...
	if command == "a" or command == "A":
		# for each possible map
		for f in os.listdir("maps/"):
			# if this file is a real map (sorry about the maps/ vs maps confusion) then add it
			if f in maps:
				add(wotdir+f+"/","maps/"+f)
	# if we want to revert
	elif command == "r" or command == "R":
		# for each directory in our spaces
		for f in os.listdir(wotdir):
			# if it is a map directory
			if f in maps:
				# revert that directory
				revert(wotdir+"/"+f)
	else : 
		print "Command not recognized. Goodbye :)"

if __name__ == "__main__":
	main()
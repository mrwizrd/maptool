README
I wrote this file to be helpful to the WOT community. Feel free to adapt it in any way you want and I take no responsibility if it messes up your install or breaks your computer. This wasn't tested by a fleet of testers or software engineers. I wrote this in four hours over the course of two days. Now, onto the usage. You're going to need python 2.7 and command line tools. Run it by...
1 - navigating to the directory in command prompt
2 - typing "python test.py"
3 - when prompted for your world of tanks directory type that in. Don't add in any spaces or apostrophes or quotation marks. Just your directory. (C:/World_of_Tanks, for example) (this is case sensitive btw)
4 - I added the feature to revert your maps back to their older state. So if you add a second set of maps and decide that you hate them then you can replace them with the revert command. However, this only works if you "add" with a filled map directory as shipped. i.e.) modding it so that the minimaps are their defaults then changing the values in the sub-directories. However, if you don't want to take advantage of this feature you can always revert by copying the dds files from World_of_Tanks/res_mods/0.9.15/spaces/* into the World_of_Tanks/res_mods/0.9.15.0.1/spaces/* directory OR by just deleting the corresponding folders in the World_of_Tanks/res_mods/0.9.15.0.1/spaces/* directory.
5 - if you've selected to add then everything should be taken care of. The files should be added automagically.

Example output:
> Add or Revert?(a/r): a
> Path to WOT: C:/World_of_Tanks
> Done!

Side Note: Your maps need to be added under the correct sub-directory. And don't have multiple files in there. It'll just add whichever it reads second and put the first into "old".

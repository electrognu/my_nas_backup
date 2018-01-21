#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
import subprocess
import datetime
from shlex import split
from time import sleep

# Path variables 
# smb_p is the path where samba folder is mounted
# base_p is the path of the base storage, a folder in the usb harddisk
## f2bk is the forlder we are going to back up, this must be asked or pass like argument in script
# difdir wil be the folder where diferential back up will be stored.
# froot is the final folder where the backup will be placed and there will be a main folder that contain the actual backup, and the diferential folders 
# mf just is the name of main folder where actualized backup is in
# options are the options passed to rsync command that perform the backup
smb_p = "/home/gabriel/.tmpsmb/" 
base_p = "/media/gabriel/BackUp2/Backup_NAS18/"		
f2bk = ""							
difdir = datetime.datetime.now().strftime("%y%m%d")	
froot = ""
mf = "main"
options = ""


# Testing if smb_p directory exists, if not then create it...
if os.path.exists(smb_p):
	print("Mount path exists")
else:
	command = "mkdir " + smb_p
	a = subprocess.run(split(command))
	if a.returncode != 0:
		print("ERROR : creating mount path : " + smb_p)
		sys.exit(1)
	else :
		print("mount path created : " + smb_p)

# Take the folder passed by the user, or ask for it
if len(sys.argv) == 1:
	f2bk = input("Introduce the folder to backup : ")
else:
	f2bk = sys.argv[1]

# Setting variables froot and options	
froot = base_p + f2bk
options = "-ahv --del --progress --backup --backup-dir="+froot+"/"+difdir
			
# Testing if base_p exists if not then abort, we can not store any file.
if os.path.exists(base_p+f2bk):
	print("Backup path exists ...")
else:
	print("Backup directory do not exist in "+base_p)
	sys.exit(1)
	


# Mounting remote samba folder and launch rsync in positive case.
command = "sudo mount.cifs //192.168.8.200/" + f2bk + " " + smb_p + " -o user=gabriel"
a = subprocess.run(split(command))
if a.returncode != 0:
	print("\nRemote folder NOT mounted : " + f2bk + " " + smb_p)
	sys.exit(1)
else:
	print("\n\nRemote folder mounted ....")
	command = "rsync " + options + " " + smb_p + " " + froot + "/" +mf
	a = subprocess.run(split(command))
	if a.returncode == 0:
		print( "\n\nDone with success")
		# desmuntar samba 
		# borrar .tmpt



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
import subprocess
import datetime
from shlex import split
from time import sleep

# Path variables 
mount_path = "/home/gabriel/.tmpsmb/"		# Path where the remote samba folder is mounted  


backup_path = "/media/gabriel/BackUp2/Backup_NAS_USB/"		# Root Path for backup the folder mounted 
backup_dir = "test"							
abort = False								# If abort == True then we will not continue


incrementdir = datetime.datetime.now().strftime("%y%m%d-%H%M")	# canviar eh?
archiveroot = backup_path + backup_dir
currenti = "main"



# Testing if mount_path directory exists, if not then create it...
if os.path.exists(mount_path):
	print("Mount path exists")
else:
	command = "mkdir " + mount_path
	a = subprocess.run(split(command))
	if a.returncode != 0:
		print("ERROR : creating mount path : " + mount_path)
		sys.exit(1)
	else :
		print("mount path created : " + mount_path)
		

	
# Testing if backup_path exists if not then abort, we can not store an file.
if os.path.exists(backup_path+backup_dir):
	print("Backup path exists ...")
else:
	print("Backup directory do not exist")
	sys.exit(1)



# Experiment 1
options = "-ahv --del --progress --backup --backup-dir="+archiveroot+"/"+incrementdir


# mounting remote samba folder :
command = "sudo mount.cifs //192.168.8.200/" + backup_dir + " " + mount_path + " -o user=gabriel"
a = subprocess.run(split(command))
if a.returncode != 0:
	print("remote folder NOT mounted : " + backup_dir + " " + mount_path)
	sys.exit(1)
else:
	print("\n\nRemote folder mounted ....")
	command = "rsync " + options + " " + mount_path + " " + archiveroot + "/" +currenti
	a = subprocess.run(split(command))
	if a.returncode == 0:
		print( "\n\nRealizado con exito ")
sleep(4)


	# Que passa si no se sap contrasenya de sudo ?
	# Quins senyals en donarà el Process ... 
	# comprovar que existeix la carpeta muntada ...
	# Si no es munta be la carpeta abortar...
	
# Utilitzar "rsync per sincronitzar les carpetes"

# Explorar rsync en mode copies incrementals ...

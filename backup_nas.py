#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
from shlex import split
from time import sleep

# Path variables 
mount_path = "~/.tmpsmb/"						# Path where the remote samba folder is mounted  
backup_path = "/media/gabriel/BackUp2" 			# Root Path for backup the folder mounted 
backup_dir = "test"				


# Comprovar que el directori mount_path existeix, sin no existeix crear-lo.
# Comprovar que el backup_path existeix, sino abortar.

# muntar carpeta remota samba :
	# Que passa si no se sap contrasenya de sudo ?
	# Quins senyals en donarà el Process ... 
	# comprovar que existeix la carpeta muntada ...

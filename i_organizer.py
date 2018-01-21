#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# f2org : path to the folder to organize.
# falbum : root path where the photos will be translated.

# Organize photos by folders hicheracy of year, month, day.
# Take a list of fotos to organize.
# for each image extract time info by year month and day.
	# if no information report this image will not been moved.
	# Notification.
	# move to the folder by year month day.
		# The folder Year month day exists ?
			# Yes -> move it.
			# No -> create it and move image into.

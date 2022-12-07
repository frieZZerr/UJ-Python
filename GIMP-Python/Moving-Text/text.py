# -*- coding: utf-8 -*-

import math
import colorsys
from gimpfu import *

#	Set your project path here
YOUR_PATH = ""

width  = 350
height = 50

#	Text colors
foreground = ( 62, 146, 204, 1 )
background = ( 10, 36, 99, 1 )

#	Creates new image
def NewImage( wid, hig ):
	image = pdb.gimp_image_new( wid, hig, 0 )
	display = pdb.gimp_display_new( image )
	return image

#	Saves all the layers to a .gif file counting from the oldest one
def SaveGIF( image, file_name, delay ):
	draw = pdb.gimp_image_get_active_drawable( image )
	if not pdb.gimp_drawable_is_indexed( draw ):
		pdb.gimp_image_convert_indexed( image, 2, 0, 255, FALSE, FALSE, file_name )
	pdb.file_gif_save( image, draw, file_name, file_name, 0, 1, delay, 0 )

#	Creating new layers with every next one having it's text shifted a bit
def Text( image, text, font, font_size ):
	pdb.gimp_context_push()
	pdb.gimp_context_set_foreground( foreground )
	pdb.gimp_context_set_background( background )

	# Creating new text layer
	text_layer = pdb.gimp_text_layer_new( image, text, font, font_size, 0 )

	pdb.gimp_image_insert_layer( image, text_layer, None, 0 )
	# Setting it's size to image size and it's justification to centered
	pdb.gimp_text_layer_resize( text_layer, width, height )
	pdb.gimp_text_layer_set_justification( text_layer, 2 )
	# Alternatively we can use this:
	# pdb.gimp_layer_resize_to_image_size( text_layer )
	pdb.gimp_layer_flatten( text_layer )

	size = len( text )
	pdb.gimp_image_undo_disable( image )
	for x in range( 0, size-1 ):
		ltext = list( text )

		for y in range( 0, size-1 ):
		    ltext[y] = ltext[y+1]

		ltext[size-1] = text[0]

		text = "".join( ltext )
		text_layer = pdb.gimp_text_layer_new( image, text, font, font_size, 0 )

		pdb.gimp_image_insert_layer( image, text_layer, None, 0 )
		pdb.gimp_text_layer_resize( text_layer, width, height )
		pdb.gimp_text_layer_set_justification( text_layer, 2 )
		pdb.gimp_layer_flatten( text_layer )
	pdb.gimp_image_undo_enable( image )

img = NewImage( width, height )

#	Set your preferences
text = u" Hello World! "
font = "Lato Bold"
font_size = 50

Text( img, text, font, font_size )

frame_rate = 100

SaveGIF( img, YOUR_PATH+"/text,gif", frame_rate )

import math
import colorsys
from gimpfu import *

#	Set your project path here
YOUR_PATH = ""

#	Declaring size of the loading bar:
#		This one is horizontal but a
#		vertical one looks good aswell
width  = 400
height = 50

#	Declaring colors for the loading bar
darkgreen = ( 0, 100, 0, 1.0 )	#	Background
green = ( 0, 255, 0, 1.0 )		#	Foreground

#	Creates new image
def NewImage( wid, hig ):
	image = pdb.gimp_image_new( wid, hig, 0 )
	display = pdb.gimp_display_new( image )
	return image

#	Fills the selection on the image with pre-picked color:
#		This function creates a new layer, selects an area
#		and fills it with color
def FillRect( img, x, y, wid, hig, color ):
	layer = pdb.gimp_layer_new( img, width, height, RGBA_IMAGE, "rect", 100, 0 )
	img.add_layer( layer )
	pdb.gimp_image_select_rectangle( img, CHANNEL_OP_REPLACE, x, y, wid, hig )
	pdb.gimp_context_set_foreground( color )
	draw = pdb.gimp_image_get_active_drawable( img )
	pdb.gimp_edit_bucket_fill_full( draw, 0, 0, 100, 255, FALSE, TRUE, 0, x, y )
	pdb.gimp_selection_none( img )

#	Saves all the layers (from the oldest) to a .gif file with a given delay between each frame
def SaveGIF( image, file_name, delay ):
	draw = pdb.gimp_image_get_active_drawable( image )
	if not pdb.gimp_drawable_is_indexed( draw ):
		pdb.gimp_image_convert_indexed( image, 2, 0, 255, FALSE, FALSE, file_name )
	pdb.file_gif_save( image, draw, file_name, file_name, 0, 1, delay, 0 )

img = NewImage( width, height )
FillRect( img, 0, 0, width, height, darkgreen )

pdb.gimp_image_undo_disable

#	Number of layers to be created
lay_num = 10

#	This variable defines how fast
#		the loading bar will proceed.
i = width/lay_num

#	Filling up the selection "frame by frame":
#		Every time filling bigger selection
while i <= width:
	FillRect( img, 0, 0, i, height, green )
	i = i + ( width/lay_num )
pdb.gimp_image_undo_enable

frame_rate = 50

SaveGIF( img, YOUR_PATH+"/loading_bar.gif", frame_rate )

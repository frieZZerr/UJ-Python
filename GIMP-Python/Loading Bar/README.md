# Create your own Loading Bar with a simple script!

![Loading Bar](https://github.com/frieZZerr/GIMP-Python/blob/main/Loading%20Bar/loading_bar.gif)

### How does it work?

This python script uses ***built-in GIMP plugins*** that allow it to modify the current image. Firstly, we need to create a `new image`:

```python
def NewImage( wid, hig ):
	image = pdb.gimp_image_new( wid, hig, 0 )
	display = pdb.gimp_display_new( image )
	return image
  ```
  
  The idea is to create a bunch of `layers` that we'll fill with _2 selected colors_ where every next layer has a bit **longer** selection
  filled with one of those colors.
  
  We have to determine **how many layers** we want to create:
  
  ```python
  #	Number of layers to be created
lay_num = 10

#	This variable defines how fast
#		the loading bar will proceed.
i = width/lay_num
```

  <sup>You can change the amount of layers [here](https://github.com/frieZZerr/GIMP-Python/blob/main/Loading%20Bar/loading_bar.py#L46).</sup>
  
  Then we make a `while` loop that creates and fills ***on each layer*** selected area which is bigger every iteration.
  
  ```python
# Filling up the selection "frame by frame":
#   Every time filling bigger selection
while i <= width:
	FillRect( img, 0, 0, i, height, green )
	i = i + ( width/lay_num )
  ```
  
  You can experiment with different sizes, number of layers, colors, selections etc. to get even better results!

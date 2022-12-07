# Make your text move!

![Moving text](https://github.com/frieZZerr/GIMP-Python/blob/main/Moving-Text/text.gif)

### Let's get started

This python script uses ***built-in GIMP*** plugins that allow it to modify the current image. We start by creating a `new image`:

```python
# Creates new image
def NewImage( wid, hig ):
	image = pdb.gimp_image_new( wid, hig, 0 )
	display = pdb.gimp_display_new( image )
	return image
```

After we've created the image we specify:
- `Text`
- `Font`
- `Font Size`

<sup>You can change these variables [here](https://github.com/frieZZerr/GIMP-Python/blob/main/Moving-Text/text.py#L65).</sup>

Then we create our first `text layer` containing all the information above. The text layer is ***inserted*** into the current layer
and **tweaked** a bit by changing it's _bounding box_ and _centering the text_.

```python
# Creating new text layer
text_layer = pdb.gimp_text_layer_new( image, text, font, font_size, 0 )

# Inserting and setting it's size to image size and it's justification to centered
pdb.gimp_image_insert_layer( image, text_layer, None, 0 )
pdb.gimp_text_layer_resize( text_layer, width, height )
pdb.gimp_text_layer_set_justification( text_layer, 2 )
```

In the `for` loop we **pack** the text into a list and _shift it_ by ***1 character***. All we have to do now is repeat the steps mentioned before.

---

> You can add some _offset_ on the X/Y axis to make the text centered even more or try to make the text go from up to down.

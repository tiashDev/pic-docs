Windowed API
============

Tcl/Tk
------

lieutenant

Plotting
--------

lieutenant

Turtle
------

.. _forward:

forward *px*
   Moves the turtle (the pen) forward by *px* pixels.

.. _backward:

backward *px*
   Moves it backward by *px* pixels.

.. _right:

right *deg*
   Turns the pen right by *deg* degrees.

.. _left:

left *deg*
   Turns it left by *deg* degrees.

.. _path_begin:

path.begin, path.start, pen.down
   Starts drawing a line.

.. _path_end

path.end, pen.up
   Ends a line.

.. _reset:

reset
   Resets the program.

.. _clear:

clear
   Clears the screen.

.. _color:

color *color*
   Sets the color of the current line to *color*.

.. _fill:

fill *color*
   Fills any fillable polygon that is drawn by the turtle with the color *color*.

.. _fillcolor_start:

fillcolor.start, fillcolor.begin
   Starts filling any fillable polygon that is drawn by the turtle with the color specified by fill (see `fill <#fill>`_ above).

.. _fillcolor_end:

fillcolor.end
   Stops filling any fillable polygon that is drawn by the turtle with the color specified by fill (see `fill <#fill>`_ above).

.. _wait:

wait *secs*
   Waits for *secs* seconds.

.. _setx:

setx *x*
   Sets the X coordinate of the turtle to *x*.

.. _sety:

sety *y*
   Sets the Y coordinate of the turtle to *y*.

.. _stamp:

stamp
   Stamps a copy of the turtle onto the canvas.

.. _stamps_clear:

stamps.clear
   Clears all the stamps.

.. _speed:

speed *s*
   Sets the speed of the turtle to *s*.

.. _size:

size *s*
   Sets the width of the line to *s*.

.. _circle:

circle *r*
   Makes the turtle draw a circle with radius *r*.

.. _outline:

outline *c*
   Sets the colour of the outline of the turtle to *c*.
   
.. _hide:

hide
   Hides the turtle.
   
.. _show:

show
   Shows the turtle.
   
.. _screen_color:

screen.color *c*
   Sets the colour of the screen to *c*.
   
.. _screen_image:

screen.image *i*
   Sets the background image of the screen to *i*.
   
.. _closeonclick:

closeonclick
   Makes it so that if you click the turtle window, it will close.
   
.. _mode:

mode *m*
   Sets the header mode to *m*.
   *m* can be -
   * "standard": The default turtle heading is to the east
   * "world": The default turtle heading is specified using user-defined world coordinates (using setworldcoordinates)
   * "logo": The default turtle heading is to the north
	  
.. _goto:

goto *x* *y*
   Makes the turtle go to x *x* and y *y*.
   
.. _dot:

dot *r* *c*
   Draws a dot with radius *r* and colour *c*.
   
.. _shape:

shape *s*
   Sets the shape of the turtle to *s*.
   *s* can be -
   * arrow 
   * turtle 
   * circle 
   * square 
   * triangle 
   * classic

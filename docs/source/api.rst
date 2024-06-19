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
   """Moves the turtle (the pen) forward by *px* pixels.
   :param px: The number of pixels."""

.. _backward:

backward *px*
   """Moves it backward by *px* pixels.
   :param px: The number of pixels."""

.. _right:

right *deg*
   """Turns the pen right by *deg* degrees.
   :param deg: The number of degrees."""

.. _left:

left *deg*
   """Turns it left by *deg* degrees.
   :param deg: The number of degrees."""

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
   """Sets the color of the current line to *color*.
   :param color: The colour."""

.. _fill:

fill *color*
   """Fills any fillable polygon that is drawn by the turtle with the color *color*.
   :param color: The colour."""

.. _fillcolor_start:

fillcolor.start, fillcolor.begin
   Starts filling any fillable polygon that is drawn by the turtle with the color specified by fill (see `fill <#fill>`_ above).

.. _fillcolor_end:

fillcolor.end
   Stops filling any fillable polygon that is drawn by the turtle with the color specified by fill (see `fill <#fill>`_ above).

.. _wait:

wait *secs*
   """Waits for *secs* seconds.
   :param secs: The number of seconds."""

.. _setx:

setx *x*
   """Sets the X coordinate of the turtle to *x*.
   :param y: The Y coordinate."""

.. _sety:

sety *y*
   """Sets the Y coordinate of the turtle to *y*.
   :param y: The Y coordinate."""

.. _stamp:

stamp
   Stamps a copy of the turtle onto the canvas.

.. _stamps_clear:

stamps.clear
   Clears all the stamps.

.. _speed:

speed *s*
   """Sets the speed of the turtle to *s*.
   :param s: The speed."""

.. _size:

size *s*
   """Sets the width of the line to *s*.
   :param s: The size."""

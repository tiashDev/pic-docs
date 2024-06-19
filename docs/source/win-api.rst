Windowed API
============

Tcl/Tk
------

.. _wininit:

wininit *n*
   Initializes a window with the name *n*.

.. _wintitle:

wintitle *n* *..t*
   Gives the window with name *n* the title *..t*.

.. _loopwin:

loopwin *n*
   Loops the window with the name *n*.
   
.. _closewin:

closewin *n*
   Closes the window with the name *n*.

.. _btn:

btn *..j*
   Creates a button. *..j* is some JSON that will configure the button. 
   JSON keys:
      * name: The unique name you will use in your code to refer to the button.
      * parent: The parent window or frame.
      * text: The text on the button.
      * onclick: The code executed when the button is clicked.

.. _sbtn:

sbtn *..j*
   Creates a styled button. *..j* is some JSON that will configure the button. 
   JSON keys:
      * name: The unique name you will use in your code to refer to the button.
      * parent: The parent window or frame.
      * text: The text on the button.
      * onclick: The code executed when the button is clicked.

.. _lbl:

lbl *..j*
   Creates a label. *..j* is some JSON that will configure the label. 
   JSON keys:
      * name: The unique name you will use in your code to refer to the label.
      * parent: The parent window or frame.
      * text: The text on the label.

.. _txt:

txt *..j*
   Creates a text area. *..j* is some JSON that will configure the text area. 
   JSON keys:
      * name: The unique name you will use in your code to refer to the text.
      * parent: The parent window or frame.
      * width: The width of the text area.
      * height: The height of the text area.

Plotting
--------

.. _plot:

plot *..x* * *..y*
   Plots a plot with x-axis *..x* and y-axis *..y*.
   Overloads -
       * plot *..x* * *..y* : *s*
           Plots a plot with x-axis *..x* and y-axis *..y*. *s* is a Matplotlib format string for styling the plot.

.. _bar:

bar *..l* * *..n*
   Plots a vertical bar plot with labels *..l* and values *..n*.
   Overloads -
       * bar *..l* * *..n* : *c*
          Plots a vertical bar plot with labels *..l* and values *..n*. *c* is the colour of all the bars.

.. _barh:

barh *..l* * *..n*
   Plots a horizontal bar plot with labels *..l* and values *..n*.
   Overloads -
       * barh *..l* * *..n* : *c*
           Plots a horizontal bar plot with labels *..l* and values *..n*. *c* is the colour of all the bars.

.. _pie:

pie *..l* * *..n*
   Plots a pie with labelss *..l* and values *..n*.
   Overloads -
       * pie *..l* * *..n* : *..c*
           Plots a pie with labels *..l* and values *..n*. *..c* is a list of the colour of the slices.

.. _hist:

hist *..v*
   Plots a histogram with values *..v*.
   Overloads -
       * hist random
            Plots a histogram with random values.
       * hist random *me* *md* *mo*
            Plots a histogram with random values. The mean of the values is *me*, the median *md* and the mode *mo*.
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

.. _input:

input *..t* | *..b*
    Asks the user for input in the GUI. The window which appears has the title *..t* and body *..b*.

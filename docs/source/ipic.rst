``ipic`` - The internal Picturesque module
==========================================

``ipic.lang`` - The crown jewel
-------------------------------

.. function:: lexer(program, is_console=False, filename=None, is_artist=False)
   :module: ipic.lang
   
   The Picturesque lexer.
   
   :param program: The program to be executed.
   :param is_console: Specifies if it is in the interpreter console or not. Defaults to ``False``.
   :param filename: The filename to be executed. Defaults to ``'<console>'``.
   :param is_artist: Specifies if the file is being executed in the Artist editor.

.. function:: interpret(do, val, lineno, line, is_console, filename, is_artist)
   :module: ipic.lang
   
   The Picturesque interpreter. Used by :py:func:`ipic.lang.lexer` to execute the program. All arguments are required.
   
   :param do: The command.
   :param val: The arguments.
   :param lineno: The statement number.
   :param line: The statement.
   :param is_console: Specifies if it is in the interpreter console or not.
   :param filename: The filename to be executed.
   :param is_artist: Specifies if the file is being executed in the Artist editor.

``ipic.errors`` - Picturesque exceptions
----------------------------------------

.. class:: PicturesqueException(msg='')
   :module: ipic.errors

   The base exception for all Picturesque exceptions. Extends ``Exception``.

The other exceptions are :py:class:`ipic.errors.PicturesqueUnreconizedCommandException`, :py:class:`ipic.errors.PicturesqueUnreconizedEventException`, :py:class:`ipic.errors.PicturesqueWindowNotFoundException`, :py:class:`ipic.errors.PicturesqueInvalidWidgetException`, :py:class:`ipic.errors.PicturesqueUndefinedTkWinClassException`, :py:class:`ipic.errors.PicturesqueInvalidOSException`, and :py:class:`ipic.errors.PicturesqueInvalidURLException`.

``ipic.out`` - The PicturesqueOutputHandler class
-------------------------------------------------

.. class:: PicturesqueOutputHandler()
   :module: ipic.out

   What ``ipic.lang.out`` is an instance of.

   .. function:: bind(evt, func):

      Bind the function :py:param:`func` to the event :py:param:`evt`.
      :py:param:`evt` can be:

      * output
          Do :py:param:`func` when :py:func:`output` is called.
      * error
          Do :py:param:`func` when an error occurs.
      * onrequestclearscreen
          Do :py:param:`func` when :py:func:`requestclearscreen` is called.

   .. function:: output(text):

      Output the text :py:param:`text`.

   .. function:: error(err):

      Call the ``error`` event handler with the error :py:param:`err`.

   .. function:: requestclearscreen():

      Call the ``onrequestclearscreen`` event handler.

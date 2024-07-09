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
   
   The Picturesque interpreter. Used by `lexer() <#ipic.lang.lexer>`_ to execute the program.
   
   :param program: The program to be executed.
   :param is_console: Specifies if it is in the interpreter console or not. Defaults to ``False``.
   :param filename: The filename to be executed. Defaults to ``'<console>'``.
   :param is_artist: Specifies if the file is being executed in the Artist editor.

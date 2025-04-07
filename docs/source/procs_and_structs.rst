Procedures and Structures (and blocks in general)
#################################################

Procedures
==========

You define a procedure by using the ``proc`` command.

The code below creates a procedure with the name ``myproc``.

.. code-block:: text

      proc myproc {
         ~ code... ;
      }

Notice the lack of a semicolon after the closing brace. This is important, as it signifies that this is a block. With the semicolon, it would produce some cryptic error message. You can write whatever you want in the procedure.

.. code-block:: text

      proc myproc {
         logln hello;
         set x = 10;
      }

To call a procedure, you do the following:

.. code-block:: text

      %myproc;

To have a procedure accept arguments, you do the following:

.. code-block:: text

      proc <name> <args> {
         ~ code;
      }

where ``<name>`` is the name of the procedure, and ``<args>`` are the arguments it accepts, seperated by spaces.

To call a procedure with arguments, you just write the arguments after the name, seperated by a space.

Interlude: Scopes
=================

Procedures have scope, which means:

.. code-block:: text

      set x = 5;
      ~ x is 5;

      proc myproc {
         logln hello;
         set x = 10;
         ~ x is 10;
      }

      %myproc;

      ~ x is still 5;

Sometimes this might be what you want, but other times it might not be. Say you're making a game of some sort:

.. code-block:: text

      set score = 0;
      
      proc enemy_hit {
        set score += 10;
      }

      ~ The player hits an enemy: ;
      %enemy_hit;

      ~ score is still 0... ;

In that case, you can use ``set nonlocl`` instead.

.. code-block:: text

      set score = 0;
      
      proc enemy_hit {
        set nonlocl score += 10;
      }

      ~ The player hits an enemy: ;
      %enemy_hit;

      ~ score is now 10! ;

Structures
==========

Structures are like classes in other languages, but they are immutable (that's why they're called structs). You can create a structure by using the ``struct`` command:

.. code-block:: text

      struct mystruct {
         ~ some code... ;
      }

The following code creates an instance of a struct called ``mystruct`` with the arguments ``args`` and assigns it to ``x``:

.. code-block:: text

      &mystruct x = new args;

To define variables of the structure, you can use the var keyword inside of the structure:

.. code-block:: text

      struct mystruct {
         var x = 10;
      }

Structure Procedures
--------------------

To define procedures of the structure, you can use the ``proc`` keyword:

.. code-block:: text

      struct mystruct {
         var x = 10;
         proc myproc {
           ~ some code... ;
         }
      }

Procedures inside a structure follow the same rules that procedures outside a structure do. 
Importantly, to access the structure's name (ie. the ``x`` in ``&mystruct x = new;``), you can use the ``_name`` variable that is automatically defined at the start of every procedure in a structure:

.. code-block:: text

      struct mystruct {
         var x = 10;
         proc myproc {
           logln i am .{%_name};
         }
      }

To define/set structure variables in the procedure, you can do the following:

.. code-block:: text

      struct mystruct {
         var x = 10;
         proc myproc {
           set nonlocl .{%_name}.y = 5; ~ the nonlocl is important;
         }
      }

To call other procedures in the structure:

.. code-block:: text

      struct mystruct {
         var x = 10;
         proc myotherproc {~ some code;}
         proc myproc {
           set nonlocl .{%_name}.y = 5; ~ the nonlocl is important;
           eval %.{%_name}.myotherproc;
         }
      }

Constructors
------------

Now, one thing you will notice with all of these examples about structures is that they will break. All of them. That's because they don't have constructors. A constructor is a procedure that is called when the structure is initialized.

A constructor must have the same name as the structure (ie. the ``mystruct`` in ``&mystruct x = new;``).

.. code-block:: text

      struct mystruct {
         var x = 10;
         proc mystruct {
           set nonlocl .{%_name}.y = 20;
         }
         proc myotherproc {~ some code;}
         proc myproc {
           set nonlocl .{%_name}.y = 5; ~ the nonlocl is important;
           eval %.{%_name}.myotherproc;
         }
      }

When you create a new instance of a structure:

.. code-block:: text

      &mystruct x = new args;

Picturesque will call the constructor with the arguments you passed in:

.. code-block:: text

      %x.mystruct args;

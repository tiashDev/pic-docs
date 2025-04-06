FTP Servers
===========

Commands
--------

ftp.open *url*
   Connects to *url*. *url* should be a URL to an ftp server.

ftp.login
   Login anonymously to the connection created by ``ftp.open``.

ftp.cd *dir*
   Changes the current directory of the connection to *dir*.

ftp.lsdir
   Lists the current directory of the connection.

ftp.close
   Closes the connection.

Variables
---------

$ftp.cwd
   Gets the CWD of the connection. Only available if there is a connection.

$ftp.welcome
   Gets the welcome message of the server. Only available if there is a connection.

Example
-------

.. code-block:: text
   :caption: Interpreter Session

   Picturesque [1.0.0]
   Copyright (c) 2024.
   Type "help" for help.
   >> ~ open a connection ;ftp.open ftp.us.debian.org;
   >> ftp.login;
   230 Login successful.
   >> logln .{$ftp.cwd};
   /
   >> ftp.lsdir;
   lrwxrwxrwx    1 0        0              17 Mar 19 16:24 debian -> pub/debian/debian
   lrwxrwxrwx    1 0        0              18 Mar 19 16:24 debian-cd -> pub/debian-cdimage
   lrwxrwxrwx    1 0        0              18 Mar 19 16:24 debian-cdimage -> pub/debian-cdimage
   drwxr-xr-x    4 0        0            4096 Mar 19 16:24 pub
   -rw-r--r--    1 0        0             754 Mar 19 16:26 welcome.msg
   >> ftp.close;
   221 Goodbye.
   >> exit;

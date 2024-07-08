FTP Servers
===========

ftp.open *url*
   Connects to *url*. *url* should be a URL to an ftp server.

   .. code-block::
      :caption: Example
      
      ftp.open ftp.us.debian.org

ftp.login
   Login anonymously to the connection created by ``ftp.open``.

ftp.cd *dir*
   Changes the current directory of the connection to *dir*.

ftp.lsdir
   Lists the current directory of the connection.

ftp.close
   Closes the connection.

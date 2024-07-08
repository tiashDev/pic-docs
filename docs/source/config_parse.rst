Parsing Configuration Files
===========================

loadini *path*
   Load an INI into Picturesque. Example:

   .. code-block:: ini
      :caption: ./ex/myini.ini

      [DEFAULT]
      ServerAliveInterval = 45
      Compression = yes
      CompressionLevel = 9
      ForwardX11 = yes
      
      [forge.example]
      User = hg
      
      [topsecret.server.example]
      Port = 50022
      ForwardX11 = no

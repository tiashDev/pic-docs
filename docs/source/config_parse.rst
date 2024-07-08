Parsing Configuration Files
===========================

loadini *name* *path*
   Load an INI (*path*) into Picturesque as some variables. The base variable name is *name*. Example:

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

   .. code-block:: text
      :caption: Interpreter Session

      Picturesque [1.0.0]
      Type "help" for help.
      >> loadini myini ./ex/myini.ini
      >> logln {%myini} ;~ access the base variable
      configuration file (from loadini) -> ./EX/MYINI.INI
      sections: forge.example, topsecret.server.example
      >> logln {%myini[forge.example]} ;~ access a section
      configuration file section (from loadini) -> ./EX/MYINI.INI (forge.example)
      options: user, serveraliveinterval, compression, compressionlevel, forwardx11
      >> logln {%myini[forge.example][user]} ;~ access option from forge.example
      hg
      >> logln {%myini[forge.example][serveraliveinterval]} ;~ access option from DEFAULT
      45
      >> exit

loadcsv *name* *path*
   Load a CSV (*path*) into Picturesque as some variables. The base variable name is *name*. Example:

   .. code-block:: text
      :caption: ./ex/mycsv.csv
      
      company,surname,forename
      Foo Tech,Jones,Alice
      Top Bar Hardware,Smith,Bob
      4uxcorp,Garcia,Carlos

   .. code-block:: text
      :caption: Interpreter Session

      Picturesque [1.0.0]
      Copyright (c) 2024.
      Type "help" for help.
      >> loadcsv mycsv ./ex/mycsv.csv
      >> logln {%mycsv} ;~ the base variable
      company            surname   forename
      Foo Tech           Jones     Alice
      Top Bar Hardware   Smith     Bob
      4uxcorp            Garcia    Carlos
      >> logln {%mycsv[0]} ;~ row number 0
      company, surname, forename
      >> logln {%mycsv[1]} ;~ row number 1
      Foo Tech, Jones, Alice
      >> logln {%mycsv[1][2]} ;~ row 1, column 2
      Alice
      >> logln {%mycsv[1][2]} {%mycsv[1][1]} ;~ get a neatly formatted name
      Alice Jones
      >> exit

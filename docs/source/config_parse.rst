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
      >> loadini myini ./ex/myini.ini;
      >> logln {%myini} ;~ access the base variable;
      configuration file (from loadini) -> ./EX/MYINI.INI
      sections: forge.example, topsecret.server.example
      >> logln {%myini[forge.example]} ;~ access a section;
      configuration file section (from loadini) -> ./EX/MYINI.INI (forge.example)
      options: user, serveraliveinterval, compression, compressionlevel, forwardx11
      >> logln {%myini[forge.example][user]} ;~ access option from forge.example;
      hg
      >> logln {%myini[forge.example][serveraliveinterval]} ;~ access option from DEFAULT;
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
      >> loadcsv mycsv ./ex/mycsv.csv;
      >> logln {%mycsv} ;~ the base variable;
      company            surname   forename
      Foo Tech           Jones     Alice
      Top Bar Hardware   Smith     Bob
      4uxcorp            Garcia    Carlos
      >> logln {%mycsv[0]} ;~ row number 0;
      company, surname, forename
      >> logln {%mycsv[1]} ;~ row number 1;
      Foo Tech, Jones, Alice
      >> logln {%mycsv[1][2]} ;~ row 1, column 2;
      Alice
      >> logln {%mycsv[1][2]} {%mycsv[1][1]} ;~ get a neatly formatted name;
      Alice Jones
      >> exit

loadplistxml *name* *path*
   Load an Apple XML PList (*path*) into Picturesque as some variables. The base variable name is *name*. Example:

   .. code-block:: xml
      :caption: ./ex/myplist.plist
      
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
      <plist version="1.0">
      <dict>
              <key>aDate</key>
              <date>2024-07-06T19:07:53Z</date>
              <key>aDict</key>
              <dict>
                      <key>aFalseValue</key>
                      <false/>
                      <key>aThirdString</key>
                      <string>Mässig, Maß</string>
                      <key>aTrueValue</key>
                      <true/>
                      <key>anotherString</key>
                      <string>&lt;hello &amp; hi there!&gt;</string>
              </dict>
              <key>aFloat</key>
              <real>0.1</real>
              <key>aList</key>
              <array>
                      <string>A</string>
                      <string>B</string>
                      <integer>12</integer>
                      <real>32.1</real>
                      <array>
                              <integer>1</integer>
                              <integer>2</integer>
                              <integer>3</integer>
                      </array>
              </array>
              <key>aString</key>
              <string>Doodah</string>
              <key>anInt</key>
              <integer>728</integer>
              <key>someData</key>
              <data>
              PGJpbmFyeSBndW5rPg==
              </data>
              <key>someMoreData</key>
              <data>
              PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMgb2Yg
              YmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5IGd1
              bms+PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMg
              b2YgYmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5IGd1bms+PGxvdHMgb2YgYmluYXJ5
              IGd1bms+
              </data>
      </dict>
      </plist>

   .. code-block:: text
      :caption: Interpreter Session

      Picturesque [1.0.0]
      Copyright (c) 2024.
      Type "help" for help.
      >> loadplistxml myplist ./ex/myplist.plist;
      >> logln {%myplist} ;~ the base variable;
      configuration tree (from plist) -> ./EX/MYPLIST.PLIST (branch: MYPLIST)
      keys: aDate, aDict, aFloat, aList, aString, anInt, someData, someMoreData
      >> logln {%myplist[adate]} ;~ a date;
      2024-07-06 19:07:53
      >> logln {%myplist[adict]} ;~ a dict;
      configuration tree (from plist) -> ./EX/MYPLIST.PLIST (branch: MYPLIST[aDict])
      keys: aFalseValue, aThirdString, aTrueValue, anotherString
      >> logln {%myplist[adict][afalsevalue]} ;~ a false value;
      $false
      >> logln {%myplist[adict][athirdstring]} ;~ a string;
      Mässig, Maß
      >> logln {%myplist[adict][atruevalue]} ;~ a true value;
      $true
      >> logln {%myplist[adict][anotherstring]} ;~ another string;
      <hello & hi there!>
      >> logln {%myplist[alist]} ;~ an array;
      A, B, 12, 32.1, (1, 2, 3)
      >> logln {%myplist[alist][0]} ;~ an array item;
      A
      >> logln {%myplist[alist][1]} ;~ another array item;
      B
      >> logln {%myplist[alist][2]} ;~ and another;
      12
      >> logln {%myplist[alist][3]} ;~ and yet another;
      32.1
      >> logln {%myplist[alist][4]} ;~ a subarray;
      1, 2, 3
      >> logln {%myplist[alist][4][0]} ;~ a subarray item;
      1
      >> logln {%myplist[alist][4][2]} ;~ another subarray item;
      3
      >> logln {%myplist[alist][4][1]} ;~ and another;
      2
      >> exit;

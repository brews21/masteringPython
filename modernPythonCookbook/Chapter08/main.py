#!/usr/bin/env python3
# This sets an association between the file you're writing and Python.
'''
Triple single quote is documentation string used to define what
the python file is use for/ meant to do
'''

import sys
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)
#print "this is: ", sys.argv[1]

import random

random.seed()

my_list = ["a", "b", "c"]

d = my_list[random.randrange(len(my_list))]

print(d)


print("hello  \"world \' ")

print("""\

                   ._ o o
                   \_`-)|_
                ,""       \\
              ,"  ## |   ಠ ಠ.
            ," ##   ,-\__    `.
          ,"       /     `--._;)
        ,"     ## /
      ,"   ##    /


""")

print("""\
            .                .
            :"-.          .-";
            |:`.`.__..__.'.';|
            || :-"      "-; ||
            :;              :;
            /  .==.    .==.  \\
           :      _.--._      ;        ______________
           ; .--.' `--' `.--. :       /  Hello World \\
          :   __;`      ':__   ;      |  foo bar      |
          ;  '  '-._:;_.-'  '  :     <\\______________/
          '.       `--'       .'
           ."-._          _.-".
         .'     ""------""     `.
        /`-                    -'\\
       /`-                      -'\\
      :`-   .'              `.   -';
      ;    /                  \\    :
     :    :                    ;    ;
     ;    ;                    :    :
     ':_:.'                    '.;_;'
        :_                      _;
        ; "-._                -" :`-.     _.._
        :_          ()          _;   "--::__. `.
         \"-                  -"/`._           :
        .-"-.                 -"-.  ""--..____.'
       /         .__  __.         \\
      : / ,       / "" \       . \ ;
       "-:___..--"      "--..___;-"
       """)

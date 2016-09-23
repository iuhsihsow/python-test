1. prepare your include and src for your c++ / c programs
2. write *.i files for your c header files e.g. spklib.i
3. swig *.i then we can get spklib.py (the python version header files)
4. create setup.py if the programs contains other libs
5. run the next command in the cmd and build the pyd file.(e.g. _spklib.cp35-win_amd64.pyd)
6. then can test it 
#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


spklib_module = Extension('_spklib',
                           sources=['./include/spklib/spklib_wrap.c', 'i3p_tool.cpp', 
                           'zlib/zip.c', 'zlib/inflate.c', 'zlib/deflate.c',
                           'zlib/ioapi.c', 'zlib/zutil.c', 'zlib/crc32.c',
                           'zlib/adler32.c','zlib/gzclose.c', 'zlib/gzlib.c'
                           ,'zlib/gzread.c', 'zlib/gzwrite.c', 'zlib/infback.c',
                           'zlib/inffast.c', 'zlib/inftrees.c', 'zlib/iowin32.c',
                           'zlib/mztools.c', 'zlib/trees.c', 'zlib/uncompr.c',
                           'zlib/unzip.c', 'zlib/zip.c'],
                           library_dirs=['C:/Projects/earth/output/win_x64_release/staticlib']
                           )

setup (name = 'spklib',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [spklib_module],
       py_modules = ["spklib"],
       )
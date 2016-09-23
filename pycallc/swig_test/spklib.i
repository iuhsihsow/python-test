/* File: spklib.i */
%module spklib

%{
#define SWIG_FILE_WITH_INIT
#include "spklib.h"
%}

int package(const char* p_caches_folder, const char* p_spk_path);

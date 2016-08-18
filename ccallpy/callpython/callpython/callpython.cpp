// callpython.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Python.h"
#include "time_test.h"
//#include "time_test.c"

double test_basic(double a, double b)
{
  Py_Initialize();

  // set path very important
  PyRun_SimpleString("import sys\nsys.path.append('C:/work_home/python-test/ccallpy/callpython/callpython')");

  PyObject* pModule = PyImport_ImportModule("time_test");
  PyObject* pFunc = PyObject_GetAttrString(pModule, "return_double");
  PyObject* pArgs = PyTuple_New(1);
  PyTuple_SetItem(pArgs, 0, PyFloat_FromDouble(a));
  PyObject* pValue = PyObject_CallObject(pFunc, pArgs);
  double res = PyFloat_AsDouble(pValue);
  Py_Finalize();
  return res;
}

double test_cython(double a, double b)
{
  PyObject* tuple;
  Py_Initialize();
  PyInit_time_test();
  double res = PyFloat_AsDouble(return_double(PyFloat_FromDouble(b)));
  Py_Finalize();
  return res;
}

int main()
{
  double a = 100;
  double b = 200;

  //double res = test_basic(a, b);
  double res = test_cython(a, b);

  printf("The result is %lf\n", res);
  return 0;
}


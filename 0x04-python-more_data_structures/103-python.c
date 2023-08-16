#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
int size, i;
PyObject *item;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
long size, i;
char *string;

printf("[*] Python bytes\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);
size = size < 10 ? size + 1 : 10;
printf("  first %ld bytes:", size);
for (i = 0; i < size; i++)
{
printf(" %02hhx", string[i]);
}
printf("\n");
}

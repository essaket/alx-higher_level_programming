#include <Python.h>

/**
 * print_python_list_info - function that prints some basic info about Python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size, allocate, y;
	PyObject *PO;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (y = 0; y < size; y++)
	{
		printf("Element %d: ", y);
		PO = PyList_GetItem(p, y);
		printf("%s\n", Py_TYPE(PO)->tp_name);
	}
}

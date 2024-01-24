#include <Python.h>

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", (size < 10 ? size : 10));
    for (Py_ssize_t i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)str[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, (PyBytes_Check(item) ? "bytes" : (PyTuple_Check(item) ? "tuple" : (PyList_Check(item) ? "list" : (PyFloat_Check(item) ? "float" : (PyLong_Check(item) ? "int" : (PyUnicode_Check(item) ? "str" : "other")))))));
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}


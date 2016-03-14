
#define _XOPEN_SOURCE 600
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#define __USE_BSD
#include <termios.h>

#include <Python.h>

static PyObject *create_pty(PyObject *self, PyObject *args)
{
	/* file descriptors for master/slave */
	int fdm, fds;
	int ret;

	/* create PTY, grant permission and unlock */
	fdm = posix_openpt(O_RDWR);
	if (fdm < 0) return Py_BuildValue("i", fdm);

	ret = grantpt(fdm);
	if (ret != 0) return Py_BuildValue("i", ret);

	ret = unlockpt(fdm);
	if (ret != 0) return Py_BuildValue("i", ret);

	/* open slave PTY */
	fds = open(ptsname(fdm), O_RDWR);

	return Py_BuildValue("i", fds);
}

static PyObject *get_ptsname(PyObject *self, PyObject *args)
{
	int fd;
	char *name;

	if (!PyArg_ParseTuple(args, "i", &fd)) return NULL;

	name = ptsname(fd);

	if (!name) return NULL;

	return Py_BuildValue("s", name);
}

static PyMethodDef pty_methods[] = {
	{"create_pty", create_pty, METH_VARARGS, "Creates a PTY device"},
	{"ptsname", get_ptsname, METH_VARARGS, "Returns the pts name of device"},
	{NULL, NULL, 0, NULL}
};

void initptymod()
{
	(void) Py_InitModule("ptymod", pty_methods);
}

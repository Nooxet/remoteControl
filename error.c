#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>

#include "error.h"

void (error)(char* file, unsigned long line, const char* func, char* msg, ...)
{
	va_list		ap;
	
	va_start(ap, msg);

	fprintf(stderr, "error: in file \"%s\", line %lu"
		" in function \"%s\": ", file, line, func);

	vfprintf(stderr, msg, ap);

	va_end(ap);

	fputc('\n', stderr);
	exit(EXIT_FAILURE);
}

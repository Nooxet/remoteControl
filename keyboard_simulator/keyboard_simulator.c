#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

#include "error.h"

#define MAXSTRING	128
#define MAXKEYS		10

static Display *disp;

/**
 * press down a key
 */
bool press(unsigned int key)
{
	assert(disp != NULL);
	return XTestFakeKeyEvent(disp, key, 1, 0);
}

/**
 * release a key
 */
bool release(unsigned int key)
{
	assert(disp != NULL);
	return XTestFakeKeyEvent(disp, key, 0, 0);
}

/**
 * click (press and release) a key
 */
bool click(unsigned int key)
{
	assert(disp != NULL);
	if (!press(key)) return false;
	if (!release(key)) return false;
	XFlush(disp);
	return true;
}

bool parse(char *buffer)
{
	/* fill with zeros */
	unsigned int keys[MAXKEYS] = { NoSymbol };
	unsigned int key;
	int idx = 0;

	char *p = buffer;
	for (int i = 0, n = strlen(buffer); i <= n; i++) {
		/* delimiter found, insert key to keys array */
		if (buffer[i] == '+' || buffer[i] == '\0') {
			buffer[i] = '\0';
			
			/* get keycode */
			key = XStringToKeysym(p);
			if (key == NoSymbol) return false;
			if (idx >= MAXKEYS) return false;
			
			/* add to array */
			keys[idx++] = key;
			
			/* start of new string */
			p = &buffer[i + 1];
		}
	}

	for (int i = 0; i < MAXKEYS; i++) {
		printf("%u\n", keys[i]);
	}

	return true;
}

int main()
{
	disp = XOpenDisplay(NULL);

	if (!disp) {
		error("Failed to open display");
	}

	printf("%lu\n", NoSymbol);

	// TODO: fix vulnerability for buffer overflow
	char buffer[MAXSTRING];

	while (1) {
		scanf("%s", buffer);
		/* terminate string */
		buffer[sizeof(buffer) - 1] = '\0';
		parse(buffer);
	}

	XCloseDisplay(disp);
	return 0;
}

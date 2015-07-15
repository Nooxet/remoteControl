#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

#include "error.h"

#define NUMKEYS (10)

static Display *disp;

/**
 * press down a key
 */
void press(unsigned int key)
{
	assert(disp != NULL);
	XTestFakeKeyEvent(disp, key, 1, 0);
}

/**
 * release a key
 */
void release(unsigned int key)
{
	assert(disp != NULL);
	XTestFakeKeyEvent(disp, key, 0, 0);
}

/**
 * click (press and release) a key
 */
void click(unsigned int key)
{
	assert(disp != NULL);
	press(key);
	release(key);
	XFlush(disp);
}

bool parse(char *buffer)
{
	/* fill with zeros */
	unsigned int keys[NUMKEYS] = { NoSymbol };
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
			if (idx >= NUMKEYS) return false;
			
			/* add to array */
			keys[idx++] = key;
			
			/* start of new string */
			p = &buffer[i + 1];
		}
	}

	for (int i = 0; i < 10; i++) {
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
	char buffer[128];

	while (1) {
		scanf("%s", buffer);
		/* terminate string */
		buffer[sizeof(buffer) - 1] = '\0';
		parse(buffer);
	}

	/* keycodes defined in /usr/include/X11/keysymdef.h */
	unsigned int ctrl = XKeysymToKeycode(disp, XK_Alt_L);
	unsigned int right = XKeysymToKeycode(disp, XK_Right);

	printf("ctrl: %i\n", XK_Alt_L);
	printf("%lu\n", XStringToKeysym("Alt_L"));

	printf("ctrl: %u, right: %u\n", ctrl, right);

	sleep(2);

	press(ctrl);
	click(right);
	release(ctrl);
	XFlush(disp);

	XCloseDisplay(disp);
	return 0;
}

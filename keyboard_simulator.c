#include <stdio.h>
#include <time.h>
#include <assert.h>

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>


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

int main()
{
	disp = XOpenDisplay(NULL);

	// keycodes defined in /usr/include/X11/keysymdef.h
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

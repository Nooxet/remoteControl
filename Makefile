
CFLAGS = -Wall -Wextra -pedantic -std=c99
PYDIR = -I/usr/include/python2.7/
LDFLAGS = -lpython2.7

.PHONY: all clean ptymod

all: ptymod

keyboard_sim:
	+$(MAKE) -C keyboard_simulator/

ptymod:
	$(CC) -fPIC -shared $(PYDIR) ptymod.c -o ptymod.so $(LDFLAGS)

clean:
	+$(MAKE) clean -C keyboard_simulator/
	rm -Rf *.pyc __pycache__/ *.so

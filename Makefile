CC = clang
CFLAGS = -Wall -Wextra -pedantic -std=c99 -g
LDLIBS = -lX11 -lXtst

PROG = keyboard_simulator

OBJS = $(PROG).o error.o

.PHONY: all clean

all: $(PROG)

$(PROG): $(OBJS)

clean:
	rm -Rf *.o core $(PROG)

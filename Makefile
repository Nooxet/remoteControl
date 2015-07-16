
all:
	+$(MAKE) -C keyboard_simulator/

clean:
	+$(MAKE) clean -C keyboard_simulator/
	rm -Rf *.pyc __pycache__/

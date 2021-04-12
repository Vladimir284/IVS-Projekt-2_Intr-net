# all (přeloží projekt - včetně programu pro profiling)
	# TO-DO Neccecary ?

# pack (zabalí projekt tak, aby mohl být odevzdán)
	# TO-DO Team work - brainstorming

# clean (smaže všechny soubory, co nemají být odevzdány)
clean:
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
    	sudo apt-get remove # Name of the app
    endif
    ifeq ($(UNAME_S),Darwin)
        sudo brew uninstall # Name of the app
    endif

# test (spustí testy matematické knihovny)
test:
	pytest test_math_lib.py

# doc (spustí generování dokumentace)
doc: remove_documentation
	doxygen ../doc/Doxyfile

# run (spustí program)
run:
	python3 calc.py

# profile (spustí překlad programu pro výpočet směrodatné odchylky na profiling)
profile:
	python3 profiling.py < data.txt

remove_documentation:
	rm -rf ../latex
	rm -rf ../html
	rm -rf ../man
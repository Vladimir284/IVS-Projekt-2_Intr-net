# pack (zabalí projekt tak, aby mohl být odevzdán)
	# TO-DO Team work - brainstorming

# clean (smaže všechny soubory, co nemají být odevzdány)
clean: remove_documentation

test:
	pytest test_math_lib.py

doc: remove_documentation
	doxygen ../doc/Doxyfile
	cd ../doc/latex && $(MAKE)

run:
	python3 calc.py

profile:
	python3 profiling.py < data.txt

remove_documentation:
	rm -rf ../doc/latex
	rm -rf ../doc/html
	rm -rf ../doc/man

.PHONY : clean

# (zabalí projekt tak, aby mohl být odevzdán)
pack: pack_folder remove_packed_folder
	# TO-DO Team work - brainstorming

pack_folder: remove_packed_folder doc
	# Make main dir that will be handed
	mkdir ../../xtichy31_xsauer03_xpolas41_xmecia00
	# Copy or make the rest of the directories that need to be included to handed dir
	mkdir ../../xtichy31_xsauer03_xpolas41_xmecia00/install # TO-DO Write installator for Calculator
	cp -R ../doc ../../xtichy31_xsauer03_xpolas41_xmecia00
	rm ../../xtichy31_xsauer03_xpolas41_xmecia00/doc/Doxyfile
	rm ../../xtichy31_xsauer03_xpolas41_xmecia00/doc/intr_net_logo.png
	cp -R ../../IVS-Projekt-2_Intr-net ../../xtichy31_xsauer03_xpolas41_xmecia00
	zip ../../xtichy31_xsauer03_xpolas41_xmecia00.zip ../../xtichy31_xsauer03_xpolas41_xmecia00
	# Might not be necessary
	# clean

remove_packed_folder:
	rm -rf ../../xtichy31_xsauer03_xpolas41_xmecia00

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

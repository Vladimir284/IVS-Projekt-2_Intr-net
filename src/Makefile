.PHONY : clean

all: run

# (zabalí projekt tak, aby mohl být odevzdán)
pack: pack_folder remove_packed_folder
	# TO-DO Team work - brainstorming

pack_folder: remove_packed_folder doc
	mkdir ../../xtichy31_xsauer03_xpolas41_xmecia00
	mkdir ../../xtichy31_xsauer03_xpolas41_xmecia00/install # TO-DO Write installator for Calculator
	cp -R ../doc ../../xtichy31_xsauer03_xpolas41_xmecia00
	rm ../../xtichy31_xsauer03_xpolas41_xmecia00/doc/Doxyfile
	rm ../../xtichy31_xsauer03_xpolas41_xmecia00/doc/intr_net_logo.png
	cp -R ../../IVS-Projekt-2_Intr-net ../../xtichy31_xsauer03_xpolas41_xmecia00
	zip ../../xtichy31_xsauer03_xpolas41_xmecia00.zip ../../xtichy31_xsauer03_xpolas41_xmecia00

remove_packed_folder:
	rm -rf ../../xtichy31_xsauer03_xpolas41_xmecia00

install_mac: uninstall
	pyinstaller -n Calculator -i calc.icns -w -F --collect-all buttons_images calc.py
	cp -R buttons_images/ dist/buttons_images
	cp -R buttons_images/ dist/Calculator.app/Contents/MacOS/buttons_images

install_windows: uninstall
	pyinstaller -n Calculator -i calc.icns calc.py
	cp -R buttons_images/ dist/buttons_images

uninstall:
	rm -rf dist
	rm -rf build
	rm -rf Calculator.spec

clean: remove_documentation uninstall

test:
	pytest test_math_lib.py

doc:
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


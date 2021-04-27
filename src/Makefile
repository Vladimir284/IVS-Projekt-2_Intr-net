.PHONY : clean

all: run

# (zabalí projekt tak, aby mohl být odevzdán)
pack: history pack_folder

pack_folder: remove_packed_folder doc
	mkdir install
	cp -R ../doc doc
	rm doc/Doxyfile
	rm doc/intr_net_logo.png
	mkdir ../../xtichy31_xsauer03_xpolas41_xmecia00
	cp -R ../../IVS-Projekt-2_Intr-net ../../xtichy31_xsauer03_xpolas41_xmecia00/IVS-Projekt-2_intr-net
	mv ../../xtichy31_xsauer03_xpolas41_xmecia00 .
	mv doc xtichy31_xsauer03_xpolas41_xmecia00
	mv install xtichy31_xsauer03_xpolas41_xmecia00
	zip -r xtichy31_xsauer03_xpolas41_xmecia00.zip xtichy31_xsauer03_xpolas41_xmecia00
	mv xtichy31_xsauer03_xpolas41_xmecia00.zip ../..
	rm -rf xtichy31_xsauer03_xpolas41_xmecia00

remove_packed_folder:
	rm -rf xtichy31_xsauer03_xpolas41_xmecia00

install_windowed: uninstall
	pyinstaller -n Calculator -i calc.icns -w -F --collect-all buttons_images calc.py
	cp -R buttons_images/ dist/buttons_images

uninstall:
	rm -rf dist
	rm -rf build
	rm -rf Calculator.spec

history:
	git log --pretty=format:"%h - %an, %ar : %s" --all > ../history.txt

test:
	pytest test_math_lib.py

doc:
	doxygen ../doc/Doxyfile
	cd ../doc/latex && $(MAKE)

run:
	python3 calc.py

profile:
	python3 profiling.py < data.txt

clean: remove_documentation uninstall

remove_documentation:
	rm -rf ../doc/latex
	rm -rf ../doc/html
	rm -rf ../doc/man
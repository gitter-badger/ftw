build:
	python3 setup.py build

install:
	sudo python3 setup.py install

clean:
	rm -rfv build* dist* ftw.egg* */__pycache__* __pycache__*

clean-root:
	sudo rm -rfv /usr/local/lib/python*/dist-packages/pyftw* /usr/local/bin/ftw* build* dist* ftw.egg* */__pycache__* */*.pyc __pycache__*

version:
	echo "v1.1.1"

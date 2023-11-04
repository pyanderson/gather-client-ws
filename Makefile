.PHONY: clean-build clean-pyc clean

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "protoc - generate protobuf code"
	@echo "update_proto - update the proto file and generate protobuf code"
	@echo "dist - package"
	@echo "release - package and upload a release"

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean: clean-build clean-pyc

update_proto:
	npm i
	npm upd
	cp node_modules/@gathertown/gather-game-common/src/events.proto ./gather_client_ws/events.proto
	make protoc

protoc:
	protoc --python_out=. --mypy_out=. ./gather_client_ws/events.proto

release: dist
	twine upload -r gather-client-ws dist/*

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

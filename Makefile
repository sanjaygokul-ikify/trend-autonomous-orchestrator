# Makefile for Autonomous Orchestrator

all: build test

build:
	python -m pip install -r requirements.txt

 test:
	pytest tests
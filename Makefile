all: lint ansible tokens

ansible:
	ansible-playbook --extra-vars="env=dev" playbook/play.yaml

lint:
	ansible-lint

tokens:
	python playbook/scripts/key_tracker.py

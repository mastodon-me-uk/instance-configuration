all: lint ansible keys

ansible:
	ansible-playbook --extra-vars="env=dev" playbook/play.yaml

lint:
	ansible-lint

keys:
	python playbook/scripts/key_tracker.py

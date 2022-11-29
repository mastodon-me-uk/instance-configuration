ansible:
	ansible-playbook --extra-vars="env=dev" playbook/play.yaml

lint:
	ansible-lint

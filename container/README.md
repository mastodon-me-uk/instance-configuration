# Ansible container

_Container providing a local dev and test environment for our Ansible playbooks_

Build it:

```
make build
```

Run it:

```
make run
```

You should now have a shell on the container and be able run Ansible:

```
ansible-playbook playbook/play.yaml
```

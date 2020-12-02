ANSIBLE-ROLE-PYAZUREMODULES
===========================

Ansible role install msret msretazure azure python3 modules.

## Version
0.0.2 - This new version add latest requireemnts-azure.txt from the original repository.

## Howto use this role?
This role need to be include in a playbook. 

Call this **Galaxy** role  like this:

````bash
ansible-galaxy install -r requirements.yml 
````

Inside requirements.yml
````yaml
- src: redbeard28.pyazuremodules
````

More info => [Ansible Docs](https://docs.ansible.com/ansible-container/roles/access.html)

## Requirements

 * Ansible 2.9+


Role Variables
--------------

```yaml
---
requirements_path: "/tmp"
```

Dependencies
------------

- src: redbeard28.pip3
- src: redbeard28.python3_apt

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: redbeard28.pyazuremodules, tags: azure_requirements }


Molecule testing framework
--------------------------

You can use molecule to test this role.
```bash
image=debian tag="buster" molecule converge 
image=debian tag="buster" molecule verify 
```

Author Information
------------------

Jeremie CUADRADO[¹](mailto:info@redbeard-consulting.fr) from Redbeard-Consulting

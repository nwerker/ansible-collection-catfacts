#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: getfact
short_description: This module gets a random cat fact from your favourite cat fact api
version_added: "2.10.0"
description:
    - "This module gets a random cat fact from your favourite cat fact api"
options:
  source:
    description:
        - From which API should the fact be gathered?
    type: str
    required: false
    choices: [ 1, 2 ]
    default: 1

  validate_certs:
    description:
        - Wether or not SSL certificates should be validated
    type: bool
    required: false
    default: true
author:
- Niklas Werker (@nwerker)
'''

EXAMPLES = r'''
# Get a random cat fact from default source
- name:
  getfact:
  register: acatfact

# Get a random cat fact from specific source
- name:
  getfact:
    source: 2
  register: acatfact
'''

RETURN = r'''
original_message:
  description: The original name param that was passed in
  type: str
  returned: always
message:
  description: The output message that the test module generates
  type: str
  returned: always
'''
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import random

def get_fact(url, validate_certs):
    headers = {}
    headers['accept'] = '*/*'

    response = open_url(url, headers=headers, method="GET", validate_certs=validate_certs)

    return response

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        source=dict(type='str', required=False, default='1', choices=['1', '2']),
        validate_certs=dict(type='bool', required=False, default=True)
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
	cat_fact=''
    )


    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    cat_fact = ''


    if module.check_mode:
        module.exit_json(**result)

    if module.params['source'] == '1':
        response = get_fact('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1',  module.params['validate_certs'])
        data = json.loads(response.read().decode('utf-8'))
        cat_fact = data['text']
    elif module.params['source'] == '2':
        response = get_fact('https://catfact.ninja/fact', module.params['validate_certs'])
        cat_fact = json.loads(response.read().decode('utf-8'))['fact']
    else:
        module.fail_json(msg='Source does not fit requirements!', **result)

    result['cat_fact'] = cat_fact


    # Result should always be changed
    result['changed'] = True

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

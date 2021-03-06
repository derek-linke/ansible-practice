#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016-2018, Eric Jacob <erjac77@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: f5bigip_ltm_profile_icap
short_description: BIG-IP ltm profile icap module
description:
    - Configures an Internet Content Adaptation Protocol (ICAP) profile.
version_added: "2.4"
author:
    - "Gabriel Fortin (@GabrielFortin)"
options:
    defaults_from:
        description:
            - Specifies the profile that you want to use as the parent profile.
        default: icap
    description:
        description:
            - User defined description.
    header_from:
        description:
            - Specifies the header-from attribute to use in the ICAP header.
    host:
        description:
            - Specifies the host attribute to use the in the ICAP header.
    preview_length:
        description:
            - Specifies the ICAP data preview size.
    referer:
        description:
            - Specifies the referer attribute to use in the ICAP header.
    state:
        description:
            - Specifies the state of the component on the BIG-IP system.
        default: present
        choices: ['absent', 'present']
    uri:
        description:
            - Specifies the ICAP URI to use in the ICAP header.
    user_agent:
        description:
            - Specifies the user-agent attribute to use in the ICAP header.
requirements:
    - BIG-IP >= 12.0
    - ansible-common-f5
    - f5-sdk
'''

EXAMPLES = '''
- name: Create LTM Profile ICAP
  f5bigip_ltm_profile_icap:
    f5_hostname: 172.16.227.35
    f5_username: admin
    f5_password: admin
    f5_port: 443
    name: my_icap_profile
    partition: Common
    state: present
  delegate_to: localhost
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ansible_common_f5.base import F5_NAMED_OBJ_ARGS
from ansible_common_f5.base import F5_PROVIDER_ARGS
from ansible_common_f5.bigip import F5BigIpNamedObject


class ModuleParams(object):
    @property
    def argument_spec(self):
        argument_spec = dict(
            defaults_from=dict(type='str'),
            description=dict(type='str'),
            header_from=dict(type='str'),
            host=dict(type='str'),
            preview_length=dict(type='int'),
            referer=dict(type='str'),
            uri=dict(type='str'),
            user_agent=dict(type='str')
        )
        argument_spec.update(F5_PROVIDER_ARGS)
        argument_spec.update(F5_NAMED_OBJ_ARGS)
        return argument_spec

    @property
    def supports_check_mode(self):
        return True


class F5BigIpLtmProfileIcap(F5BigIpNamedObject):
    def _set_crud_methods(self):
        self._methods = {
            'create': self._api.tm.ltm.profile.icaps.icap.create,
            'read': self._api.tm.ltm.profile.icaps.icap.load,
            'update': self._api.tm.ltm.profile.icaps.icap.update,
            'delete': self._api.tm.ltm.profile.icaps.icap.delete,
            'exists': self._api.tm.ltm.profile.icaps.icap.exists
        }


def main():
    params = ModuleParams()
    module = AnsibleModule(argument_spec=params.argument_spec, supports_check_mode=params.supports_check_mode)

    try:
        obj = F5BigIpLtmProfileIcap(check_mode=module.check_mode, **module.params)
        result = obj.flush()
        module.exit_json(**result)
    except Exception as exc:
        module.fail_json(msg=str(exc))


if __name__ == '__main__':
    main()

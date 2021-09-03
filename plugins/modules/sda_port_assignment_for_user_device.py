#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_user_device
short_description: Resource module for Sda Port Assignment For User Device
description:
- Manage operations create and delete of the resource Sda Port Assignment For User Device.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ip:
    description: Device-ip query parameter.
    type: str
  interfaceName:
    description: InterfaceName query parameter.
    type: str
  payload:
    description: Sda Port Assignment For User Device's payload.
    suboptions:
      authenticateTemplateName:
        description: Authenticate Template Name.
        type: str
      dataIpAddressPoolName:
        description: Data Ip Address Pool Name.
        type: str
      deviceManagementIpAddress:
        description: Device Management Ip Address.
        type: str
      interfaceName:
        description: Interface Name.
        type: str
      siteNameHierarchy:
        description: Site Name Hierarchy.
        type: str
      voiceIpAddressPoolName:
        description: Voice Ip Address Pool Name.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Port Assignment For User Device reference
  description: Complete reference of the Sda Port Assignment For User Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    device_ip: string
    interfaceName: string

- name: Create
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "executionStatusUrl": "string"
    }
"""
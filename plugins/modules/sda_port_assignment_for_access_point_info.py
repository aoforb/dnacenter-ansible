#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_access_point_info
short_description: Information module for Sda Port Assignment For Access Point
description:
- Get all Sda Port Assignment For Access Point.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  device_ip:
    description:
    - Device-ip query parameter.
    type: str
  interfaceName:
    description:
    - InterfaceName query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Port Assignment For Access Point reference
  description: Complete reference of the Sda Port Assignment For Access Point object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Port Assignment For Access Point
  cisco.dnac.sda_port_assignment_for_access_point_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    device_ip: string
    interfaceName: string
  register: result

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
      "siteNameHierarchy": "string",
      "deviceManagementIpAddress": "string",
      "interfaceName": "string",
      "dataIpAddressPoolName": "string",
      "voiceIpAddressPoolName": "string",
      "scalableGroupName": "string",
      "authenticateTemplateName": "string"
    }
"""
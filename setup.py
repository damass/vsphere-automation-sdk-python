#!/usr/bin/env python

import os

from setuptools import setup

setup(name='vsphere-automation-sdk',
      version='1.86.0',
      description='VMware vSphere Automation SDK for Python',
      url='https://github.com/vmware/vsphere-automation-sdk-python',
      author='VMware, Inc.',
      license='MIT',
      packages=[],
      install_requires=[
        'lxml >= 4.3.0',
        'pyVmomi',
        'vapi-runtime @ file://localhost/{}/lib/vapi-runtime/vapi_runtime-2.44.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'vcenter-bindings @ file://localhost/{}/lib/vcenter-bindings/vcenter_bindings-4.2.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'vapi-common-client @ file://localhost/{}/lib/vapi-common-client/vapi_common_client-2.44.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'vmwarecloud-aws @ file://localhost/{}/lib/vmwarecloud-aws/vmwarecloud_aws-1.64.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'nsx-python-sdk @ file://localhost/{}/lib/nsx-python-sdk/nsx_python_sdk-4.1.2.0.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'nsx-policy-python-sdk @ file://localhost/{}/lib/nsx-policy-python-sdk/nsx_policy_python_sdk-4.1.2.0.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'nsx-vmc-policy-python-sdk @ file://localhost/{}/lib/nsx-vmc-policy-python-sdk/nsx_vmc_policy_python_sdk-4.1.2.0.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'nsx-vmc-aws-integration-python-sdk @ file://localhost/{}/lib/nsx-vmc-aws-integration-python-sdk/nsx_vmc_aws_integration_python_sdk-4.1.2.0.0-py2.py3-none-any.whl'.format(os.getcwd()),
        'vmwarecloud-draas @ file://localhost/{}/lib/vmwarecloud-draas/vmwarecloud_draas-1.23.0-py2.py3-none-any.whl'.format(os.getcwd()),
      ]
)

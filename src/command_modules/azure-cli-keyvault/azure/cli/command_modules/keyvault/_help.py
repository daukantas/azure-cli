# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long

helps['keyvault'] = """
    type: group
    short-summary: Safeguard and maintain control of keys, secrets, and certificates.
    long-summary: If you don't have the keyvault component installed, add it with `az component update --add keyvault`.
"""

helps['keyvault create'] = """
    type: command
    short-summary: Create a key vault.
    long-summary: "Default permissions are created for the current user or service principal unless the --no-self-perms flag is specified."
"""

helps['keyvault delete'] = """
    type: command
    short-summary: Delete a key vault.
"""

helps['keyvault list'] = """
    type: command
    short-summary: List key vaults.
"""

helps['keyvault show'] = """
    type: command
    short-summary: Show details of a key vault.
"""

helps['keyvault update'] = """
    type: command
    short-summary: Update the properties of a key vault.
"""

helps['keyvault key'] = """
    type: group
    short-summary: Manage keys.
"""

helps['keyvault secret'] = """
    type: group
    short-summary: Manage secrets.
"""

helps['keyvault certificate'] = """
    type: group
    short-summary: Manage certificates.
"""

helps['keyvault certificate get-default-policy'] = """
    type: command
    short-summary: Get a default policy for a self-signed certificate
    long-summary: >
        This default policy can be used in conjunction with `az keyvault create` to create a self-signed certificate.
        The default policy can also be used as a starting point to create derivative policies. \n

        Also see: https://docs.microsoft.com/en-us/rest/api/keyvault/certificates-and-policies
    examples:
        - name: Create a self-signed certificate with a the default policy
          text: >
            az keyvault create -g group-name -n vaultname -l westus --enabled-for-deployment true \\
              --enabled-for-template-deployment true

            az keyvault certificate create --vault-name vaultname -n cert1 \\
              -p "$(az keyvault certificate get-default-policy)"
"""

helps['keyvault certificate create'] = """
    type: command
    long-summary: >
        Create a Key Vault certificate. Certificates can also be used as a secrets in provisioned virtual machines.
    examples:
        - name: Create a self-signed certificate with a the default policy and add to a virtual machine
          text: >
            az keyvault certificate create --vault-name vaultname -n cert1 \\
              -p "$(az keyvault certificate get-default-policy)"

            secrets=$(az keyvault secret list-versions --vault-name vaultname \\
              -n cert1 --query "[?attributes.enabled].id" -o tsv)

            vm_secrets=$(az vm format-secret -s "$secrets") \n

            az vm create -g group-name -n vm-name --admin-username deploy  \\
              --image debian --secrets "$vm_secrets"
"""

helps['keyvault certificate pending'] = """
    type: group
    short-summary: Manage pending certificate creation operations.
"""

helps['keyvault certificate contact'] = """
    type: group
    short-summary: Manage contacts for certificate management.
"""

helps['keyvault certificate issuer'] = """
    type: group
    short-summary: Manage certificate issuer information.
"""

helps['keyvault certificate issuer admin'] = """
    type: group
    short-summary: Manage admin information for certificate issuers.
"""

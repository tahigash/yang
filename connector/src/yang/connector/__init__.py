"""yang.connector module defines a set of classes that connect to Data Model
Interfaces (DMI)

Netconf is a wrapper around the ncclient package.
Gnmi is a wrapper around the grpcio v1.12.1+ package with protobuf v3.6.0.
Restconf implementation is coming next.
"""

# metadata
__version__ = '19.7'
__author__ = (
    'Jonathan Yang <yuekyang@cisco.com>',
    'Siming Yuan <siyuan@cisco.com',
    'Myles Dear <mdear@cisco.com',
    'Michael Ott <miott@cisco.com'
)
__contact__ = 'yang-python@cisco.com'
__copyright__ = 'Cisco Systems, Inc.'


from .netconf import Netconf
from .gnmi import Gnmi

__all__ = (
    'Netconf',
    'Gnmi',
)

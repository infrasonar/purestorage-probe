from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_sorted

# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterface
# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterfaceeth
# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterfacefc


class CheckInterfaces(Check):
    key = 'interfaces'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_network_interfaces'
        data = await query(asset, local_config, config, req)

        return {
            'interfaces': [{
                'name': d.name,
                'enabled': d.enabled,  # bool
                'interface_type': d.interface_type,
                'services': opt_sorted(d.services),  # liststr
                'speed': d.speed,  # int
                'fc': getattr(d.fc, 'name', None),
                'address': getattr(d.eth, 'address', None),
                'gateway': getattr(d.eth, 'gateway', None),
                'mac_address': getattr(d.eth, 'mac_address', None),
                'mtu': getattr(d.eth, 'mtu', None),  # int
                'netmask': getattr(d.eth, 'netmask', None),
            } for d in data]
        }

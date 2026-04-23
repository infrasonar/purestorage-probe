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
        data = await query(asset, local_config, config, req, {})
        g = getattr

        return {
            'interfaces': [{
                'name': d.name,
                'enabled': g(d, 'enabled', False),  # bool
                'interface_type': g(d, 'interface_type', None),
                'services': opt_sorted(g(d, 'services', None)),  # liststr?
                'speed': g(d, 'speed', None),  # int?
                'fc': g(g(d, 'fc', None), 'name', None),
                'address': g(g(d, 'eth', None), 'address', None),
                'gateway': g(g(d, 'eth', None), 'gateway', None),
                'mac_address': g(g(d, 'eth', None), 'mac_address', None),
                'mtu': g(g(d, 'eth', None), 'mtu', None),  # int
                'netmask': g(g(d, 'eth', None), 'netmask', None),
            } for d in data]
        }

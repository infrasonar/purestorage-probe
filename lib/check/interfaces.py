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

        url = '/network-interfaces'
        data = await query(asset, local_config, config, url)

        return {
            'interfaces': [{
                'name': d['name'],
                'enabled': d.get('enabled'),  # bool
                'interface_type': d.get('interface_type'),
                'services': opt_sorted(d.get('services')),  # liststr
                'speed': d.get('speed'),  # int
                'fc': d.get('fc', {}).get('name'),

                # TODO
                # 'eth': d.get('eth'),  # object -> !!!
            } for d in data]
        }

from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterface
# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterfaceeth
# https://code.purestorage.com/py-pure-client/fa_reference.html#networkinterfacefc


async def check_interfaces(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/network-interfaces'
    data = await query(asset, asset_config, check_config, url)

    return {
        'interfaces': [{
            'name': d['name'],
            'enabled': d.get('enabled'),  # bool
            'interface_type': d.get('interface_type'),
            'services': d.get('services'),  # liststr
            'speed': d.get('speed'),  # int

            # TODO
            # 'eth': d.get('eth'),  # object
            # 'fc': d.get('fc'),  # object
        } for d in data]
    }

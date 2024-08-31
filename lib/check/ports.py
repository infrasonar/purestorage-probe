from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#port


async def check_ports(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/ports'
    data = await query(asset, asset_config, check_config, url)

    return {
        'ports': [{
            'name': d['name'],
            'iqn': d.get('iqn'),
            'nqn': d.get('nqn'),
            'portal': d.get('portal'),
            'wwn': d.get('wwn'),
            'failover': d.get('failover'),
        } for d in data]
    }

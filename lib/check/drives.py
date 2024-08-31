from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#drive


async def check_drives(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/drives'
    data = await query(asset, asset_config, check_config, url)

    return {
        'drives': [{
            'name': d['name'],
            'id': d['id'],
            'capacity': d.get('capacity'),  # int
            'details': d.get('details'),
            'protocol': d.get('protocol'),
            'status': d.get('status'),
            'type': d.get('type'),
        } for d in data]
    }

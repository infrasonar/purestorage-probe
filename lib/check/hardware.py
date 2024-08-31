from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hardware


async def check_hardware(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/hardware'
    data = await query(asset, asset_config, check_config, url)

    return {
        'hardware': [{
            'name': d['name'],
            'id': d['id'],
            'details': d.get('details'),
            'identify_enabled': d.get('identify_enabled'),  # bool
            'index': d.get('index'),  # int
            'model': d.get('model'),
            'serial': d.get('serial'),
            'slot': d.get('slot'),  # int
            'speed': d.get('speed'),  # int
            'status': d.get('status'),
            'temperature': d.get('temperature'),  # int
            'type': d.get('type'),
            'voltage': d.get('voltage'),  # int
        } for d in data]
    }

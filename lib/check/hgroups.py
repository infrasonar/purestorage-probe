from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hostgroup


async def check_hgroups(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/host-groups'
    data = await query(asset, asset_config, check_config, url)

    return {
        'hgroups': [{
            'name': d['name'],
            'id': d['id'],
            'connection_count': d.get('connection_count'),  # int
            'host_count': d.get('host_count'),  # int
            'is_local': d.get('is_local'),  # bool

            # TODO
            # 'space': d.get('space'),  # object
        } for d in data]
    }

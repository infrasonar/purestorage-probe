from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#arrayconnection
# https://code.purestorage.com/py-pure-client/fa_reference.html#throttle
# https://code.purestorage.com/py-pure-client/fa_reference.html#timewindow


async def check_connections(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/array-connections'
    data = await query(asset, asset_config, check_config, url)

    return {
        'connections': [{
            'name': d['name'],
            'id': d['id'],
            'encryption': d.get('encryption'),
            'encryption_mode': d.get('encryption_mode'),
            'management_address': d.get('management_address'),
            'replication_addresses': d.get('replication_addresses'),  # liststr
            'replication_transport': d.get('replication_transport'),
            'status': d.get('status'),
            'type': d.get('type'),
            'version': d.get('version'),
            # 'throttle': d.get('throttle'),  # object
        } for d in data]
    }

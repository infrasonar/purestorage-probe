from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#volume


async def check_volumes(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/volumes'
    data = await query(asset, asset_config, check_config, url)

    return {
        'ports': [{
            'name': d['name'],
            'id': d['id'],
            'connection_count': d.get('connection_count'),  # int
            'created': d.get('created'),  # bool
            'destroyed': d.get('destroyed'),  # bool
            'host_encryption_key_status': d.get('host_encryption_key_status'),
            'pod': d.get('pod', {}).get('name'),
            'priority': d.get('priority'),  # int
            'promotion_status': d.get('promotion_status'),
            'provisioned': d.get('provisioned'),  # int
            'requested_promotion_state': d.get('requested_promotion_state'),
            'serial': d.get('serial'),
            'source': d.get('source', {}).get('name'),
            'subtype': d.get('subtype'),
            'time_remaining': d.get('time_remaining'),  # int
            'volume_group': d.get('volume_group', {}).get('name'),

            # 'priority_adjustment': d.get('priority_adjustment'),  # object
            # 'protocol_endpoint': d.get('protocol_endpoint'),  # object
            # 'qos': d.get('qos'),  # object
            # 'space': d.get('space'),  # object
        } for d in data]
    }

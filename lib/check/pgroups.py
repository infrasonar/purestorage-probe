from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#protectiongroup


async def check_pgroups(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/protection-groups'
    data = await query(asset, asset_config, check_config, url)

    return {
        'pgroups': [{
            'name': d['name'],
            'id': d['id'],
            'destroyed': d.get('destroyed'),  # bool
            'host_count': d.get('host_count'),  # int
            'host_group_count': d.get('host_group_count'),  # int
            'is_local': d.get('is_local'),  # bool
            'pod': d.get('pod', {}).get('name'),  # str
            'retention_lock': d.get('retention_lock'),
            'source': d.get('source', {}).get('name'),  # str
            'target_count': d.get('target_count'),  # int
            'time_remaining': d.get('time_remaining'),  # int
            'volume_count': d.get('volume_count'),  # int

            # TODO
            # 'eradication_config': d.get('eradication_config'),  # object
            # 'replication_schedule': d.get('replication_schedule'),  # object
            # 'snapshot_schedule': d.get('snapshot_schedule'),  # object
            # 'source_retention': d.get('source_retention'),  # object
            # 'target_retention': d.get('target_retention'),  # object
        } for d in data]
    }

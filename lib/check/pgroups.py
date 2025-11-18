from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#protectiongroup


class CheckPgroups(Check):
    key = 'pgroups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/protection-groups'
        data = await query(asset, local_config, config, url)

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

                # SKIPPED
                # 'eradication_config': d.get('eradication_config'),  # obj
                # 'replication_schedule': d.get('replication_schedule'),  # obj
                # 'snapshot_schedule': d.get('snapshot_schedule'),  # obj
                # 'source_retention': d.get('source_retention'),  # obj
                # 'target_retention': d.get('target_retention'),  # obj
            } for d in data]
        }

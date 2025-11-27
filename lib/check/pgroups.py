from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#protectiongroup


class CheckPgroups(Check):
    key = 'pgroups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_protection_groups'
        data = await query(asset, local_config, config, req)

        return {
            'pgroups': [{
                'name': d.name,
                'destroyed': d.destroyed,  # bool
                'host_count': d.host_count,  # int
                'host_group_count': d.host_group_count,  # int
                'is_local': d.is_local,  # bool
                'pod': getattr(d.pod, 'name', None),  # str
                'retention_lock': d.retention_lock,
                'source': getattr(d.source, 'name', None),  # str
                'target_count': d.target_count,  # int
                'time_remaining': getattr(d, 'time_remaining', None),  # int?
                'volume_count': d.volume_count,  # int

                # SKIPPED
                # 'eradication_config': d.eradication_config,  # obj
                # 'replication_schedule': d.replication_schedule,  # obj
                # 'snapshot_schedule': d.snapshot_schedule,  # obj
                # 'source_retention': d.source_retention,  # obj
                # 'target_retention': d.target_retention,  # obj
            } for d in data]
        }

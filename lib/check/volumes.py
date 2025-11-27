from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_float, opt_ms_to_sec

# https://code.purestorage.com/py-pure-client/fa_reference.html#volume


class CheckVolumes(Check):
    key = 'volumes'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_volumes'
        data = await query(asset, local_config, config, req)

        return {
            'volumes': [{
                'name': d.id,
                'display_name': d.name,
                'connection_count': d.connection_count,  # int
                'created': opt_ms_to_sec(d.created),  # int
                'destroyed': d.destroyed,  # bool
                'host_encryption_key_status':
                d.host_encryption_key_status,
                'pod': getattr(d.pod, 'name', None),
                'priority': d.priority,  # int
                'promotion_status': d.promotion_status,
                'provisioned': d.provisioned,  # int
                'requested_promotion_state':
                d.requested_promotion_state,
                'serial': d.serial,
                'source': getattr(d.source, 'name', None),
                'subtype': d.subtype,
                'time_remaining': getattr(d, 'time_remaining', None),  # int?
                'volume_group': getattr(d.volume_group, 'name', None),
                'data_reduction': opt_float(
                    getattr(d.space, 'data_reduction', None)),  # int/float
                'footprint': getattr(d.space, 'footprint', None),  # int
                'shared': getattr(d.space, 'shared', None),  # int
                'snapshots': getattr(d.space, 'snapshots', None),  # int
                'system': getattr(d.space, 'system', None),  # int
                'thin_provisioning': opt_float(
                    getattr(d.space, 'thin_provisioning', None)),  # int/float
                'total_physical': getattr(d.space, 'total_physical', None),
                'total_provisioned':
                getattr(d.space, 'total_provisioned', None),  # int
                'total_reduction': opt_float(
                    getattr(d.space, 'total_reduction', None)),  # int/float
                'total_used': getattr(d.space, 'total_used', None),  # int
                'unique': getattr(d.space, 'unique', None),  # int
                'used_provisioned':
                getattr(d.space, 'used_provisioned', None),  # int
                'virtual': getattr(d.space, 'virtual', None),  # int

                # SKIP
                # 'priority_adjustment': d.priority_adjustment,  # obj
                # 'protocol_endpoint': d.protocol_endpoint,  # obj
                # 'qos': d.qos,  # obj
            } for d in data]
        }

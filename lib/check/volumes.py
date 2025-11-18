from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#volume


class CheckVolumes(Check):
    key = 'volumes'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/volumes'
        data = await query(asset, local_config, config, url)

        return {
            'ports': [{
                'name': d['name'],
                'id': d['id'],
                'connection_count': d.get('connection_count'),  # int
                'created': d.get('created'),  # bool
                'destroyed': d.get('destroyed'),  # bool
                'host_encryption_key_status':
                d.get('host_encryption_key_status'),
                'pod': d.get('pod', {}).get('name'),
                'priority': d.get('priority'),  # int
                'promotion_status': d.get('promotion_status'),
                'provisioned': d.get('provisioned'),  # int
                'requested_promotion_state':
                d.get('requested_promotion_state'),
                'serial': d.get('serial'),
                'source': d.get('source', {}).get('name'),
                'subtype': d.get('subtype'),
                'time_remaining': d.get('time_remaining'),  # int
                'volume_group': d.get('volume_group', {}).get('name'),

                # SKIP
                # 'priority_adjustment': d.get('priority_adjustment'),  # obj
                # 'protocol_endpoint': d.get('protocol_endpoint'),  # obj

                # TODO
                # 'qos': d.get('qos'),  # obj
                # 'space': d.get('space'),  # obj
            } for d in data]
        }

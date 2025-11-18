from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_sorted

# https://code.purestorage.com/py-pure-client/fa_reference.html#arrayconnection
# https://code.purestorage.com/py-pure-client/fa_reference.html#throttle
# https://code.purestorage.com/py-pure-client/fa_reference.html#timewindow


class CheckConnections(Check):
    key = 'connections'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/array-connections'
        data = await query(asset, local_config, config, url)

        return {
            'connections': [{
                'name': d['name'],
                'id': d['id'],
                'encryption': d.get('encryption'),
                'encryption_mode': d.get('encryption_mode'),
                'management_address': d.get('management_address'),
                'replication_addresses':
                opt_sorted(d.get('replication_addresses')),
                'replication_transport': d.get('replication_transport'),
                'status': d.get('status'),
                'type': d.get('type'),
                'version': d.get('version'),
                # 'throttle': d.get('throttle'),  # object
            } for d in data]
        }

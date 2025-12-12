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

        req = 'get_array_connections'
        data = await query(asset, local_config, config, req, {})

        return {
            'connections': [{
                'name': d.id,
                'local_name': d.name,
                'encryption': getattr(d, 'encryption', None),
                'encryption_mode': getattr(d, 'encryption_mode', None),
                'management_address': getattr(d, 'management_address', None),
                'replication_addresses': opt_sorted(d.replication_addresses),
                'replication_transport':
                getattr(d, 'replication_transport', None),
                'status': d.status,
                'type': d.type,
                'version': d.version,
                # 'throttle': d.throttle,  # object
            } for d in data]
        }

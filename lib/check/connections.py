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
        data = await query(asset, local_config, config, req)

        return {
            'connections': [{
                'name': d.name,
                'id': d.id,
                'encryption': d.encryption,
                'encryption_mode': d.encryption_mode,
                'management_address': d.management_address,
                'replication_addresses': opt_sorted(d.replication_addresses),
                'replication_transport': d.replication_transport,
                'status': d.status,
                'type': d.type,
                'version': d.version,
                # 'throttle': d.throttle,  # object
            } for d in data]
        }

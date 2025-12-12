from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#drive


class CheckDrives(Check):
    key = 'drives'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_drives'
        data = await query(asset, local_config, config, req, {})

        return {
            'drives': [{
                'name': d.name,
                'capacity': d.capacity,  # int
                'details': getattr(d, 'details', None),
                'protocol': getattr(d, 'protocol', None),
                'status': d.status,
                'type': d.type,
            } for d in data]
        }

from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#drive


class CheckDrives(Check):
    key = 'drives'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/drives'
        data = await query(asset, local_config, config, url)

        return {
            'drives': [{
                'name': d['name'],
                'id': d['id'],
                'capacity': d.get('capacity'),  # int
                'details': d.get('details'),
                'protocol': d.get('protocol'),
                'status': d.get('status'),
                'type': d.get('type'),
            } for d in data]
        }

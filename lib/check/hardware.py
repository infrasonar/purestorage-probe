from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hardware


class CheckHardware(Check):
    key = 'hardware'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/hardware'
        data = await query(asset, local_config, config, url)

        return {
            'hardware': [{
                'name': d['name'],
                'id': d['id'],
                'details': d.get('details'),
                'identify_enabled': d.get('identify_enabled'),  # bool
                'index': d.get('index'),  # int
                'model': d.get('model'),
                'serial': d.get('serial'),
                'slot': d.get('slot'),  # int
                'speed': d.get('speed'),  # int
                'status': d.get('status'),
                'temperature': d.get('temperature'),  # int
                'type': d.get('type'),
                'voltage': d.get('voltage'),  # int
            } for d in data]
        }

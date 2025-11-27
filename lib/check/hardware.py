from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hardware


class CheckHardware(Check):
    key = 'hardware'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_hardware'
        data = await query(asset, local_config, config, req)

        return {
            'hardware': [{
                'name': d.name,
                'details': getattr(d, 'details', None),
                'identify_enabled': getattr(d, 'identify_enabled', None),  # bool
                'index': getattr(d, 'index', None),  # int
                'model': getattr(d, 'model', None),
                'serial': getattr(d, 'serial', None),
                'slot': getattr(d, 'slot', None),  # int
                'speed': getattr(d, 'speed', None),  # int
                'status': getattr(d, 'status', None),
                'temperature': getattr(d, 'temperature', None),  # int
                'type': d.type,
                'voltage': getattr(d, 'voltage', None),  # int
            } for d in data]
        }

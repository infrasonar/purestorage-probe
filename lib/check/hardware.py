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
                'identify_enabled': d.identify_enabled,  # bool
                'index': d.index,  # int
                'model': d.model,
                'serial': d.serial,
                'slot': d.slot,  # int
                'speed': d.speed,  # int
                'status': d.status,
                'temperature': d.temperature,  # int
                'type': d.type,
                'voltage': d.voltage,  # int
            } for d in data]
        }

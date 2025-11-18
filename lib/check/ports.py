from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#port


class CheckPorts(Check):
    key = 'ports'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/ports'
        data = await query(asset, local_config, config, url)

        return {
            'ports': [{
                'name': d['name'],
                'iqn': d.get('iqn'),
                'nqn': d.get('nqn'),
                'portal': d.get('portal'),
                'wwn': d.get('wwn'),
                'failover': d.get('failover'),
            } for d in data]
        }

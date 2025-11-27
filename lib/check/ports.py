from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#port


class CheckPorts(Check):
    key = 'ports'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_ports'
        data = await query(asset, local_config, config, req)

        return {
            'ports': [{
                'name': d.name,
                'iqn': getattr(d, 'iqn', None),
                'nqn': getattr(d, 'nqn', None),
                'portal': d.portal,
                'wwn': d.wwn,
                'failover': d.failover,
            } for d in data]
        }

from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hostgroup


class CheckHgroups(Check):
    key = 'hgroups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/host-groups'
        data = await query(asset, local_config, config, url)

        return {
            'hgroups': [{
                'name': d['name'],
                'id': d['id'],
                'connection_count': d.get('connection_count'),  # int
                'host_count': d.get('host_count'),  # int
                'is_local': d.get('is_local'),  # bool

                # TODO
                # 'space': d.get('space'),  # object
            } for d in data]
        }

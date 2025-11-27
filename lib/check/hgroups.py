from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#hostgroup


class CheckHgroups(Check):
    key = 'hgroups'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_host_groups'
        data = await query(asset, local_config, config, req)

        return {
            'hgroups': [{
                'name': d.name,
                'connection_count': d.connection_count,  # int
                'host_count': d.host_count,  # int
                'is_local': d.is_local,  # bool

                # TODO: space is a total of all volumes attached to hgroup
                # 'space': d.space,  # object
            } for d in data]
        }

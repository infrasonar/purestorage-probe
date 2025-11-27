from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_sorted

# https://code.purestorage.com/py-pure-client/fa_reference.html#host


class CheckHosts(Check):
    key = 'hosts'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_hosts'
        data = await query(asset, local_config, config, req)

        return {
            'hosts': [{
                'name': d.name,
                'connection_count': d.connection_count,  # int
                'host_group': getattr(d.host_group, 'name', None),  # str
                'is_local': d.is_local,  # bool
                'iqns': opt_sorted(d.iqns),  # liststr
                'nqns': opt_sorted(d.nqns),  # liststr
                'personality': getattr(d, 'personality', None),
                'port_connectivity_details':
                getattr(d.port_connectivity, 'details', None),
                'port_connectivity_status':
                getattr(d.port_connectivity, 'status', None),
                'preferred_arrays': [
                    e.name for e in d.preferred_arrays]
                if d.preferred_arrays is not None else None,  # liststr
                'vlan': d.vlan,
                'wwns': opt_sorted(d.wwns),  # liststr

                # TODO: space is a total of all volumes attached to host
                # 'space': d.space,  # object
            } for d in data]
        }

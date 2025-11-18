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

        url = '/hosts'
        data = await query(asset, local_config, config, url)

        return {
            'hosts': [{
                'name': d['name'],
                'connection_count': d.get('connection_count'),  # int
                'host_group': d.get('host_group', {}).get('name'),  # str
                'is_local': d.get('is_local'),  # bool
                'iqns': opt_sorted(d.get('iqns')),  # liststr
                'nqns': opt_sorted(d.get('nqns')),  # liststr
                'personality': d.get('personality'),
                'port_connectivity_details':
                d.get('port_connectivity', {}).get('details'),
                'port_connectivity_status':
                d.get('port_connectivity', {}).get('status'),
                'preferred_arrays': [
                    e['name'] for e in d['preferred_arrays']]
                if d.get('preferred_arrays') is not None else None,  # liststr
                'vlan': d.get('vlan'),
                'wwns': opt_sorted(d.get('wwns')),  # liststr

                # TODO
                # 'space': d.get('space'),  # object
            } for d in data]
        }

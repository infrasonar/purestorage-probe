from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#host


async def check_hosts(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/hosts'
    data = await query(asset, asset_config, check_config, url)

    return {
        'hosts': [{
            'name': d['name'],
            'connection_count': d.get('connection_count'),  # int
            'host_group': d.get('host_group', {}).get('name'),  # str
            'is_local': d.get('is_local'),  # bool
            'iqns': d.get('iqns'),  # liststr
            'nqns': d.get('nqns'),  # liststr
            'personality': d.get('personality'),
            'port_connectivity_details':
            d.get('port_connectivity', {}).get('details'),
            'port_connectivity_status':
            d.get('port_connectivity', {}).get('status'),
            'preferred_arrays': [
                e['name'] for e in d['preferred_arrays']]
            if d.get('preferred_arrays') is not None else None,  # liststr
            'vlan': d.get('vlan'),
            'wwns': d.get('wwns'),  # liststr

            # TODO
            # 'chap': d.get('chap'),  # object
            # 'space': d.get('space'),  # object
        } for d in data]
    }

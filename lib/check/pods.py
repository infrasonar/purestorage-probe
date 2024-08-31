from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#pod


async def check_pods(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/pods'
    data = await query(asset, asset_config, check_config, url)

    return {
        'pods': [{
            'name': d['name'],
            'id': d['id'],
            'array_count': d.get('array_count'),  # int
            'arrays': [e['status'] for e in d['arrays']]
            if d.get('arrays') is not None else None,  # liststr
            'destroyed': d.get('destroyed'),  # bool
            'failover_preferences': [
                e['name'] for e in d['failover_preferences']]
            if d.get('failover_preferences') is not None else None,  # liststr
            'footprint': d.get('footprint'),  # int
            'link_source_count': d.get('link_source_count'),  # int
            'link_target_count': d.get('link_target_count'),  # int
            'mediator': d.get('mediator'),
            'mediator_version': d.get('mediator_version'),
            'promotion_status': d.get('promotion_status'),
            'quota_limit': d.get('quota_limit'),  # int
            'requested_promotion_state': d.get('requested_promotion_state'),
            'source': d.get('source', {}).get('name'),
            'time_remaining': d.get('time_remaining'),  # int

            # TODO
            # 'eradication_config': d.get('eradication_config'),  # object
            # 'space': d.get('space'),  # object
        } for d in data]
    }

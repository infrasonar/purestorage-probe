from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#pod


class CheckPods(Check):
    key = 'pods'
    unchanged_eol = 0

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_pods'
        data = await query(asset, local_config, config, req)

        return {
            'pods': [{
                'name': d.name,
                'id': d.id,
                'array_count': d.array_count,  # int
                'arrays': [e.status for e in d.arrays]
                if d.arrays is not None else None,  # liststr
                'destroyed': d.destroyed,  # bool
                'failover_preferences': [
                    e.name for e in d.failover_preferences]
                if d.failover_preferences is not None
                else None,  # liststr
                'footprint': d.footprint,  # int
                'link_source_count': d.link_source_count,  # int
                'link_target_count': d.link_target_count,  # int
                'mediator': d.mediator,
                'mediator_version': d.mediator_version,
                'promotion_status': d.promotion_status,
                'quota_limit': d.quota_limit,  # int
                'requested_promotion_state':
                d.requested_promotion_state,
                'source': getattr(d.source, 'name', None),
                'time_remaining': getattr(d, 'time_remaining', None),  # int?

                # SKIP
                # 'eradication_config': d.eradication_config,  # object
                # 'space': d.space,  # object
            } for d in data]
        }

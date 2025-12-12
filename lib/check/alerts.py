from datetime import datetime, timedelta, UTC
from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_ms_to_sec

# https://code.purestorage.com/py-pure-client/fa_reference.html#alert
# https://code.purestorage.com/swagger/redoc/fa2.49-api-reference.html#tag/Alerts/paths/~1api~12.49~1alerts/get  # nopep8


class CheckAlerts(Check):
    key = 'alerts'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_alerts'
        days = config.get('alert_history_days', 7)
        datestr = (
            datetime.now(UTC) - timedelta(days=days)
        ).isoformat(sep='T', timespec='seconds')
        kwargs = {'filter': f'created > "{datestr}"'}
        data = await query(asset, local_config, config, req, kwargs)

        return {
            'alerts': [{
                'name': d.id,
                'actual': d.actual,  # str
                'category': d.category,  # str
                'closed': opt_ms_to_sec(getattr(d, 'closed', None)),  # int?
                'code': d.code,  # int
                'component_name': getattr(d, 'component_name', None),  # str
                'component_type': getattr(d, 'component_type', None),  # str
                'created': opt_ms_to_sec(d.created),  # int
                'description': getattr(d, 'description', None),  # str
                'expected': d.expected,  # str
                'flagged': d.flagged,  # bool
                'issue': getattr(d, 'issue', None),  # str
                'knowledge_base_url': getattr(
                    d, 'knowledge_base_url', None),  # str
                'severity': d.severity,  # str
                'state': d.state,  # str
                'summary': d.summary,  # str
                'updated': opt_ms_to_sec(getattr(d, 'updated', None)),  # int?
            } for d in data]
        }

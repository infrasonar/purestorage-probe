import time
from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query
from ..utils import opt_ms_to_sec

# https://code.purestorage.com/py-pure-client/fa_reference.html#certificate


def is_valid(vfrom: int | None, vto: int | None) -> bool | None:
    if vfrom is None or vto is None:
        # if vfrom is not None:
        #     now = int(time.time())
        #     return vfrom < now
        # if vto is not None:
        #     now = int(time.time())
        #     return now < vto
        return
    now = int(time.time()) * 1000
    return vfrom < now < vto



class CheckCertificates(Check):
    key = 'certificates'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = 'get_certificates'
        data = await query(asset, local_config, config, req)

        return {
            'certificates': [{
                'name': d.name,
                'common_name': getattr(d, 'common_name', None),
                'country': getattr(d, 'country', None),
                'email': getattr(d, 'email', None),
                'issued_by': d.issued_by,
                'issued_to': d.issued_to,
                'key_size': d.key_size,  # int
                'locality': getattr(d, 'locality', None),
                'organization': getattr(d, 'organization', None),
                'organizational_unit': getattr(d, 'organizational_unit', None),
                'state': getattr(d, 'state', None),
                'status': d.status,
                'valid_from': opt_ms_to_sec(getattr(d, 'valid_from', None)),
                'valid_to': opt_ms_to_sec(getattr(d, 'valid_to', None)),  # int
                'is_valid': is_valid(d.valid_from, d.valid_to),
            } for d in data]
        }

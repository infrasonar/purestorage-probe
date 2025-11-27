import time
from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#certificate


def is_valid(vfrom: int | None, vto: int | None) -> bool | None:
    if vfrom is None or vto is None:
        return
    now = int(time.time())
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
                'common_name': d.common_name,
                'country': d.country,
                'email': d.email,
                'issued_by': d.issued_by,
                'issued_to': d.issued_to,
                'key_size': d.key_size,  # int
                'locality': d.locality,
                'organization': d.organization,
                'organizational_unit': d.organizational_unit,
                'state': d.state,
                'status': d.status,
                'valid_from': d.valid_from,  # int
                'valid_to': d.valid_to,  # int
                'is_valid': is_valid(d.valid_from, d.valid_to),
            } for d in data]
        }

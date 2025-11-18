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

        url = '/certificates'
        data = await query(asset, local_config, config, url)

        return {
            'certificates': [{
                'name': d['name'],
                'certificate': d.get('certificate'),
                'common_name': d.get('common_name'),
                'country': d.get('country'),
                'email': d.get('email'),
                'intermediate_certificate': d.get('intermediate_certificate'),
                'issued_by': d.get('issued_by'),
                'issued_to': d.get('issued_to'),
                'key_size': d.get('key_size'),  # int
                'locality': d.get('locality'),
                'organization': d.get('organization'),
                'organizational_unit': d.get('organizational_unit'),
                'state': d.get('state'),
                'status': d.get('status'),
                'valid_from': d.get('valid_from'),  # int
                'valid_to': d.get('valid_to'),  # int
                'is_valid': is_valid(d.get('valid_from'), d.get('valid_to')),
            } for d in data]
        }

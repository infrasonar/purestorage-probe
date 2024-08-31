from libprobe.asset import Asset
from ..query import query

# https://code.purestorage.com/py-pure-client/fa_reference.html#certificate


async def check_certificates(
        asset: Asset,
        asset_config: dict,
        check_config: dict):

    url = '/certificates'
    data = await query(asset, asset_config, check_config, url)

    # TODO add is_valid, expires_in metrics like tcp-probe?
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
        } for d in data]
    }

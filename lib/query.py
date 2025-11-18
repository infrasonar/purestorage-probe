from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from typing import List, Dict


async def query(
        asset: Asset,
        local_config: dict,
        config: dict,
        route: str) -> List[Dict]:

    address = config.get('address')
    if not address:
        address = asset.name
    username = local_config.get('username')
    password = local_config.get('password')
    if None in (username, password):
        raise CheckException('missing credentials')

    # TODO
    return []

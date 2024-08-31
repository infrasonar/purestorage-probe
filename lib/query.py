import aiohttp
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from typing import List, Dict


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        route: str) -> List[Dict]:

    address = check_config.get('address')
    if not address:
        address = asset.name
    username = asset_config.get('username')
    password = asset_config.get('password')
    if None in (username, password):
        raise CheckException('missing credentials')

    # TODO
    return []

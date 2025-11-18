from collections import defaultdict
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from pypureclient import flasharray
from pypureclient.exceptions import PureError
from .version import __version__


USER_AGENT = f'InfraSonarPureStorageProbe/{__version__}'

CONN_CACHE: dict[tuple[int, str, str], flasharray.Client] = \
    defaultdict(flasharray.Client)


async def get_client(
        asset: Asset,
        local_config: dict,
        config: dict) -> flasharray.Client:

    address = config.get('address')
    if not address:
        address = asset.name
    token = local_config.get('secret')
    if token is None:
        raise CheckException('missing credentials')

    conn = CONN_CACHE.get((asset.id, address, token))
    if conn:
        return conn

    try:
        conn = flasharray.Client(
            target=address,
            api_token=token,
            user_agent=USER_AGENT,
        )
    except PureError:
        raise ConnectionError('Unable to connect')
    else:
        CONN_CACHE[(asset.id, address, token)] = conn
    return conn

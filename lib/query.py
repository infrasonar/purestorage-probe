import asyncio
from collections import defaultdict
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from pypureclient import flasharray
from pypureclient.exceptions import PureError
from typing import Any
from .version import __version__


USER_AGENT = f'InfraSonarPureStorageProbe/{__version__}'

# TODO do we need asset.id in key?
CONN_CACHE: dict[tuple[int, str, str], flasharray.Client] = \
    defaultdict(flasharray.Client)


async def get_client(
        asset: Asset,
        address: str,
        token: str) -> flasharray.Client:

    conn = CONN_CACHE.get((asset.id, address, token))
    if conn:
        return conn

    try:
        conn = flasharray.Client(
            target=address,
            api_token=token,
            auto_pagination_limit=2000,
            user_agent=USER_AGENT,
        )
    except PureError:
        raise CheckException('Unable to connect')
    else:
        CONN_CACHE[(asset.id, address, token)] = conn
        return conn


async def _query(
        asset: Asset,
        address: str,
        token: str,
        req: str):

    client = await get_client(asset, address, token)
    fun = getattr(client, req, None)
    if fun is None:
        raise CheckException(f'Unknown request `{req}`')

    return fun()


async def query(
        asset: Asset,
        local_config: dict,
        config: dict,
        req: str) -> list[Any]:

    address = config.get('address')
    if not address:
        address = asset.name
    token = local_config.get('secret')
    if token is None:
        raise CheckException('Missing credentials')

    result = await asyncio.get_running_loop().run_in_executor(
        None,
        _query,
        asset,
        address,
        token,
        req,
    )
    if isinstance(result, flasharray.ErrorResponse):
        status_code = result.status_code  # type: ignore
        raise CheckException(f'Invalid response status {status_code}')

    return result.items  # type: ignore

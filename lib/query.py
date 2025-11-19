import asyncio
import threading
from collections import defaultdict
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from pypureclient import flasharray
from pypureclient.exceptions import PureError
from typing import Any
from .version import __version__


USER_AGENT = f'InfraSonarPureStorageProbe/{__version__}'

# TODO do we need asset.id in key?
_cache: dict[
    tuple[str, str],
    flasharray.Client] = defaultdict(flasharray.Client)  # type: ignore

_lock = threading.Lock()


def get_client(
        address: str,
        token: str) -> flasharray.Client:  # type: ignore

    conn = _cache.get((address, token))
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
        _cache[(address, token)] = conn
        return conn


def _query(
        address: str,
        token: str,
        req: str):

    with _lock:
        client = get_client(address, token)

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
        address,
        token,
        req,
    )
    if isinstance(result, flasharray.ErrorResponse):
        status_code = result.status_code  # type: ignore
        raise CheckException(f'Invalid response status {status_code}')

    return result.items  # type: ignore

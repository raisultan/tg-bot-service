from typing import Any

import httpx

from config import settings


class GatewayAPIDriver:
    _api_root_url: str = settings.GW_ROOT_URL

    api_key: str = settings.GW_API_KEY
    logger: Any

    class Route:
        USERS: str = '/users'

    @classmethod
    async def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    async def tg_user_create(cls, name: str, chat_id: str) -> httpx.Response:
        url = await cls._build_url(cls.Route.USERS)

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                headers={'x-api-key': cls.api_key},
                data={'name': name, 'chat_id': chat_id},
            )

        return resp

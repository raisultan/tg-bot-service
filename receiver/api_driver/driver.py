import logging
from typing import Optional, Union
from json import JSONDecodeError

import httpx

from config import settings

from .logger import gateway_api_driver_logger_init


class GatewayAPIDriver:
    _api_root_url: str = settings.GW_ROOT_URL
    _api_key: str = settings.GW_API_KEY

    logger: logging.Logger = gateway_api_driver_logger_init()

    class LoggerMsgTemplates:
        REQUEST: str = 'REQUEST: url: {url} headers: {headers} body: {body}'
        RESPONSE: str = (
            'RESPONSE: status_code: {status_code} url: {url} headers: {headers} '
            'body: {body} error: {error}'
        )

    class Route:
        USERS: str = '/users'

    @classmethod
    async def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    async def tg_user_create(cls, name: str, chat_id: int) -> httpx.Response:
        url = await cls._build_url(cls.Route.USERS)
        headers = {'x-api-key': cls._api_key}
        data = {'name': name, 'chat_id': chat_id}

        cls._log_request(url, headers, data)

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                headers=headers,
                data=data,
            )

        try:
            resp_body = resp.json()
            error = None
        except JSONDecodeError as exc:
            resp_body = None
            error = str(exc)

        cls._log_response(resp.url, resp.status_code, resp.headers, resp_body, error)

        return resp

    @classmethod
    def _log_request(cls, url: str, headers: dict[str, str], body: dict) -> None:
        cls.logger.info(
            msg=cls.LoggerMsgTemplates.REQUEST.format(
                url=url,
                headers=headers,
                body=body,
            )
        )

    @classmethod
    def _log_response(
            cls,
            url: Optional[httpx.URL],
            status_code: int,
            headers: dict[str, str],
            body: Union[None, dict, str] = None,
            error: Optional[str] = None,
    ) -> None:
        cls.logger.info(
            msg=cls.LoggerMsgTemplates.RESPONSE.format(
                url=url,
                status_code=status_code,
                headers=headers,
                body=body,
                error=error,
            )
        )

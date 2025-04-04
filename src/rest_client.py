import typing as t
from logging import getLogger
from json import dumps

import httpx

from constants import DEFAULT_OK_CODES
from exceptions import TimeoutException, NetworkError, HttpError, ApplicationError, exception_handler


class RestClient:

    def __init__(self, url: str, headers: dict = {}):
        self.url = url
        self.headers = headers
        self.logger = getLogger("RestClient")

    @exception_handler((TimeoutException, NetworkError, HttpError), ApplicationError)
    def __call__(self, params) -> dict[str, t.Any]:
        response = httpx.get(
            self.url,
            params=params,
            headers=self.headers,
        )

        if response.status_code not in DEFAULT_OK_CODES:
            raise HttpError(response.status_code)

        return response.json()

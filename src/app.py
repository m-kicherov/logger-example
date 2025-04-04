import os
from time import sleep
from logging import Logger, getLogger, basicConfig
from uuid import uuid4

from rest_client import RestClient
from exceptions import ApplicationError, exception_handler
from constants import DEFAULT_REST_HEADERS, DEFAULT_URL, DEFAULT_LOGGER_FORMAT



if __name__ == "__main__":
    basicConfig(level='DEBUG', **DEFAULT_LOGGER_FORMAT)
    logger: Logger = getLogger("Application logger")
    rest = RestClient(DEFAULT_URL, DEFAULT_REST_HEADERS)
    while True:
        uuid = uuid4()
        logger.error(f'1 example uud {uuid}')
        for city in ['Moscow', 'London']:
            resp = rest(params={'key': os.environ['API_KEY'], 'q': city, 'aqi': 'no'})
            logger.warning(resp)
            sleep(5)
        logger.error(f'2 example uud {uuid}')

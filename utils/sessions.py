import os
from utils.requests_helper import BaseSession


def reqres() -> BaseSession:
    reqres_api = os.getenv('reqres_url')
    return BaseSession(base_url=reqres_api)
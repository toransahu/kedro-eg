import requests
import logging

from kedroeg.settings import conf_parameters


logger = logging.getLogger(__name__)


def list_users() -> dict:
    reqres_api = conf_parameters.get("reqres_api")
    conf_parameters["sample"] = True
    api = f"{reqres_api}/users?page=1"
    logger.info(f"GET {api}")
    logger.error(f"GET {api}")
    r = requests.get(api)
    return r.json()

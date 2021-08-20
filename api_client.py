import logging
import time

import requests
import slumber

log = logging.getLogger(__name__)


class APISession(requests.Session):
    """Logging wrapper around requests session"""
    def request(self, method, url, **kwargs):
        start = time.time()
        response = super().request(method, url, **kwargs)
        duration = int(1000 * (time.time() - start))
        log.info(
            "[AM-Vision API] %s %s %s %dms",
            method, url, response.status_code, duration
        )
        if 400 <= response.status_code <= 499:
            log.warning("AMvision Error message: %s", response.content)
        return response


class APIClient(slumber.API):
    def __init__(self, url, token):
        super().__init__(url, session=APISession())
        # add authentication header to slumber's default api client
        self._store['session'].auth = None
        self._store['session'].headers['Authorization'] = "Token " + token

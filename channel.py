import json

import requests


class Channel(object):
    """
    A channel resource contains information about a YouTube channel.
    """

    _URL = "https://www.googleapis.com/youtube/v3/channels"
    _PARAMS = ""
    _RESPONSE = ""

    def __init__(self, id, part, key, **kwargs):
        for k, v in kwargs.items():
            if self._not_empty(v):
                self._PARAMS += "{}={}&".format(
                    k, self._clean(v)
                )

        self._PARAMS += "id={}&part={}&key={}".format(
            id, self._clean(part), key
        )

        req = requests.get(self._url())
        self._RESPONSE = json.loads(req.content)

    @staticmethod
    def _clean(val):
        return str(val).replace(" ", "")

    @staticmethod
    def _not_empty(val):
        return str(val).strip() != ""

    def _url(self):
        return "{}?{}".format(self._URL, self._PARAMS)

    def data(self):
        error = self._RESPONSE.get('error', None)
        if error:
            raise Exception(error.get('message'))

        return self._RESPONSE["items"]

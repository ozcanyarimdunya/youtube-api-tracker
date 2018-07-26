import json

import requests


class Search(object):
    """
    A search result contains information about a YouTube video, channel,
    or playlist that matches the search parameters specified in an API request.
    While a search result points to a uniquely identifiable resource, like a video,
    it does not have its own persistent data.
    """

    _URL = "https://www.googleapis.com/youtube/v3/search"
    _PARAMS = ""
    _RESPONSE = ""

    def __init__(self, q, part, key, **kwargs):
        for k, v in kwargs.items():
            if self._not_empty(v):
                self._PARAMS += "{}={}&".format(
                    k, self._clean(v)
                )

        self._PARAMS += "q={}&part={}&key={}".format(
            q, self._clean(part), key
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

        result = []
        for k in self._RESPONSE["items"]:
            res = k["id"]
            res["channelId"] = k["snippet"]["channelId"]
            result.append(res)

        return result

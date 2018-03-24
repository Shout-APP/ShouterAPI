import urllib.parse
import urllib.request
import urllib.response


SHOUT_ENDPOINT = "https://shout-app.tk/shouter"


class Shouter:
    def __init__(self, api_token: str) -> None:
        self.api_token = api_token

    def shout(self, message: str) -> urllib.response:
        message = message.encode('UTF-8')
        query = "apiToken={}&message={}".format(self.api_token, urllib.parse.quote(message))
        url = "{}/shout?{}".format(SHOUT_ENDPOINT, query)

        response = urllib.request.urlopen(url)

        return response

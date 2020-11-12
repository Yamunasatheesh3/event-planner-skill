from requests import HTTPError
from mycroft.api import DeviceApi
from oauth2client import client

class MycroftTokenCredentials(client.AccessTokenCredentials):
    def __init__(self, cred_id):
        self.cred_id = cred_id
        d = self.get_credentials()
        super().__init__(d['access_token'], d['user_agent'])

    def get_credentials(self):
        retry = False
        try:
            d = DeviceApi().get_oauth_token(self.cred_id)
        except HTTPError:
            retry = True
        if retry:
            d = DeviceApi().get_oauth_token(self.cred_id)
        return d

    def _refresh(self, http):
        d = self.get_credentials()
        self.access_token = d['access_token']

from .app import UebApp as app


#testing_server_auth = ('tian', 'gan#2016')
hs_name = app.get_custom_setting('hs_name')
hs_password = app.get_custom_setting('hs_password')
hydrods_name = app.get_custom_setting('hydrods_name')
hydrods_password = app.get_custom_setting('hydrods_password')
client_id = app.get_custom_setting('client_id')
client_secret = app.get_custom_setting('client_secret')
#token = {u'access_token': u'JwDCWUNl5VfycL9186IDfuWEjVNCcj', u'token_type': u'Bearer', u'expires_in': 2592000, u'refresh_token': u'6Jix1kb5ZoAg7n7x8Rl1H6Ymi5frHa', u'scope': u'read write'}
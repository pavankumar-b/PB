from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="kZP69NJ8FNNx5tYABhtY5fu65"
consumer_secret="nWPdXF3XWSQ5E4fb5C8acJgDfJniJnpWKCEphEBaHsReZgQdeA"
access_token="250688662-D2RbQUtIY3AzpL7pIDU0Lynapx9cUO4CUCAg0xCe"
access_token_secret="UMNbOzXMThEhvt4lNDRB8rG0PGzhNUKBKTVtppmO6DSsj"

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    x = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, x)
    stream.filter(track=['android'])

import tweepy

import datetime
from datetime import timedelta

  
Consumer_key = "------"
Consumer_secret = "------"
Access_token = "-------"
Access_secret = "-------"

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True) 

status_list = api.home_timeline(count = 100)
  
for status in api.home_timeline():
    print("ツイートのID\t", status.id)
    print("ツイートした時間\t", status.created_at + timedelta(hours=+9))
    print("ツイート本文\t", status.text)
    print("ユーザ名\t", status.user.name)
    print("スクリーンネーム\t", status.user.screen_name)
    print("フォロー数\t", status.user.friends_count)
    print("フォロワー数\t", status.user.followers_count)
    print("概要（自己紹介が書かれているやつ）\t", status.user.description)
    print("-"*30)

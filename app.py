from wsgiref.simple_server import make_server
import tweepy
import datetime
from datetime import timedelta 
import json
from wsgiref.util import request_uri
import urllib.parse 
 
def app(environ, start_response):
  status = '200 OK'
  headers = [
    ('Content-type', 'application/json; charset=utf-8'),
    ('Access-Control-Allow-Origin', '*'),
  ]  
  start_response(status, headers)
  
  Consumer_key = "------------"
  Consumer_secret = "-------------"
  Access_token = "--------------"
  Access_secret = "-------------"

  auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
  auth.set_access_token(Access_token, Access_secret)

  api = tweepy.API(auth, wait_on_rate_limit = True)

  dict =  {} 
  for status in api.home_timeline(count=1):
    print("ツイート本文\t", status.text)
    dict["text"] = status.text
  #print(dict["text"])  

  url = request_uri(environ,include_query=True)
  
  qs = urllib.parse.urlparse(url).query
  #print("THIS_IS_QUERY"+str(qs))
 
  qs_d = urllib.parse.parse_qs(qs)
  #print("THIS_IS_DICT_OF_QUERY"+str(qs_d))

  for i in qs_d.keys():
      print(i)
      if i == "index":
          print("THIS_IS_QUERY"+str(qs))
          print("THIS_IS_DICT_OF_QUERY"+str(qs_d))
          print(qs_d["index"][0])
          i = int(qs_d["index"][0])
          print(type(i))
          print("ここから本文:"+status.text)
          print("スライスした本文:"+status.text[i:])


  return [json.dumps(dict).encode("utf-8")]

with make_server('', 3000, app) as httpd:
  print("Serving on port 3000..")
  httpd.serve_forever()

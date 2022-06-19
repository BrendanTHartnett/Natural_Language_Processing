import os
import pandas as pd
from datetime import date

#set timelframe #
today = date.today ()
end_date = today
print(end_date)


#SEARCH BY TOPIC ####
#set topic and max_results
search_term = 'Tufts'
from_date = '2022-05-01'
max_results = 100


#Scrape tweets mentioning "tufts" #
os.system(f"snscrape --since {from_date} twitter-search '{search_term} until:{end_date}' > result-tweets.txt")

if os.stat("result-tweets.txt").st_size == 0:
    counter = 0
else:
    df = pd.read_csv('result-tweets.txt', names=['link'])
    counter = df.size
    
print('Number of tweets: '+ str(counter))


#SEARCH BY USERNAME ####
user_name = "BrendanHartnett"
user_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-user '{user_name}' > user-tweets.txt"

os.system(user_tweets)
if os.stat("user-tweets.txt").st_size == 0:
  print('No Tweets found')
else:
  df = pd.read_csv('user-tweets.txt', names=['content'])
  for row in df['content'].iteritems():
    print(row)

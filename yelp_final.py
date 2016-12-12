from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEYS'],
    consumer_secret=os.environ['CONSUMER_SECRETS'],
    token=os.environ['TOKEN'],
    token_secret= os.environ['TOKEN_SECRET'])


client = Client(auth)


def get_food_place(place, term):
	params = {
    'term': term,
    'lang': 'en'}
	x = 0
	response = client.search(place, **params)
	
	phone_book = {}
	

	for bus in response.businesses:
		x = x + 1
		phone_book.update({bus.name:bus.display_phone})
		print ("#{0} {1}".format(x, bus.name))
		if x == 3:
			break
	return phone_book

city = input("What city are you interested in? ")
doing = input("What are you looking for(Food, restaraunts, anything. ")
city = "{}".format(city)
doing = "{}".format(doing)
phone_book = (get_food_place(city, doing))
new_book = sorted(phone_book.items())
print (new_book)

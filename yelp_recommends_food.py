from flask import Flask, render_template, request
import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEYS'],
    consumer_secret=os.environ['CONSUMER_SECRETS'],
    token=os.environ['TOKEN'],
    token_secret= os.environ['TOKEN_SECRET'])

client = Client(auth)

app = Flask(__name__)

@app.route("/")






def city_weather():
	doing = request.values.get("doing")
	city = request.values.get("city")
	businesses = None
	if city != None:

		businesses = (get_food_place(city, doing))
		
	return render_template('city_yelper.html',
                           doing=doing, city=city, businesses=businesses)


def get_food_place(place,term):

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

#	return render_template('about.html')

# name(orange) is the assignment inside 
# the templates, name(white), is the variable 




if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port)

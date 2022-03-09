from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request
import urllib.parse


app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def weather():
	if request.method == 'POST':
		city = urllib.parse.quote_plus(request.form['city'])
	else:
		# default to Chicago
		city = 'Chicago'

	api = "74fc0701ed1b6c34a5933795f3b1d5b5"

	# source contain json data from api
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api + '&units=imperial').read()

	# converting JSON data to a dictionary
	list_of_data = json.loads(source)

	# data for variable list_of_data
	data = {
		"country_code": str(list_of_data['sys']['country']),
		"city_name": str(list_of_data['name']),
		"weather_stat": str(list_of_data['weather'][0]['description']),
		"temp": str(list_of_data['main']['temp']) + '°F',
		"pressure": str(list_of_data['main']['pressure']) + ' hPa',
		"humidity": str(list_of_data['main']['humidity']) + '%',
		"wind_speed": str(list_of_data['wind']['speed']) + ' meters/sec',
		"iconcode": str('http://openweathermap.org/img/w/' + list_of_data['weather'][0]['icon'] + '.png')
	}

	print(data)
	return render_template('index.html', data = data)


if __name__ == '__main__':
	app.run()

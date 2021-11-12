from flask import Flask,jsonify,request
from json import load

with open('data/countries.json') as countries_json:
    countries_data=load(countries_json)

app = Flask(__name__)

# root directory
@app.route('/', methods=['GET'])
def home_page():  # put application's code here
    return "<h1>Countries API</h1><p>This site is a prototype API for countries information.</p>"

# localhost/countries_api/countries
# A route to return all of the available entries in our catalog.
@app.route('/countries_api/all_countries', methods=['GET'])
def api_all():
    return jsonify(countries_data)

# localhost/countries_api/countries?country_code=TR
# 127.0.0.1:5000/countries_api/countries?country_code=TR
# Finding Specific Resources
@app.route('/countries_api/countries', methods=['GET'])
def api_country_code():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'country_code' in request.args:
        country_code = request.args['country_code']
    else:
        return "Error: No country_code field provided. Please specify an valid country_code."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for country in countries_data:
        if country['country_code'] == country_code:
            results.append(country)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
if __name__ == '__main__':
    app.run()

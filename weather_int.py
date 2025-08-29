from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API Key and Base URL
API_KEY = "98057c5b85e8b1d8e052e7dbddb5ae05"
URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template("index.html", weather=None)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')  # Get city name from query parameter
    if not city:
        return render_template("index.html", weather=None)  # Return to the form if no city is provided

    # Make the API request to OpenWeatherMap
    response = requests.get(URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    
    if response.status_code != 200:
        return render_template("index.html", weather=None)  # No data if request failed

    # Process the response
    data = response.json()

    if data.get("cod") != 200:  # If city is not found
        return render_template("index.html", weather=None)
    
    return render_template("index.html", weather=data)

if __name__ == "__main__":
    app.run(debug=True)

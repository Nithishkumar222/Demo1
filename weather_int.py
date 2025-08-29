from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# API detail
CITY = "Patna"
API_KEY = "98057c5b85e8b1d8e052e7dbddb5ae05"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"



@app.route('/')
def home():
    return "Welcome to the Weather API!"

@app.route('/weather')
def weather():
    response = requests.get(URL)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    data = response.json()

   
    return render_template("index.html", weather=data)

if __name__ == "__main__":
    app.run(debug=True)

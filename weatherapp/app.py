from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "e7e9227b5fb9a926ac33de256fab338c"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city").strip()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                icon_code = data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": icon_url
                }
            else:
                weather = {"error": f"City not found or request failed. ({response.status_code})"}
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

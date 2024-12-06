
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        # Formulardaten abrufen
        user_id = request.form["userId"]
        title = request.form["title"]
        completed = request.form["completed"] == "true"

        # API-Aufruf
        api_url = "https://jsonplaceholder.typicode.com/todos"
        payload = {
            "userId": int(user_id),
            "title": title,
            "completed": completed
        }
        try:
            api_response = requests.post(api_url, json=payload)
            response = api_response.json()
        except Exception as e:
            response = {"error": str(e)}

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

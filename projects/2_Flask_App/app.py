from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Sunny, App is running in Docker!"

@app.route("/about")
def about():
    return "Simple app is running inside a docker container"

@app.route("/contact")
def contact():
    return "Contact Sunny"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
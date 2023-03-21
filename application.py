from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello python awesome azure app service!\n"

if __name__ == "__main__":
    #run flask app
    app.run(host='0.0.0.0', port=80)

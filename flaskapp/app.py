from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    temperature_data = []
    time = []
    with open("reading.embs") as file:
        data = file.readlines()
        #print data
        for i in data:
            temperature_data.append(i.split('\t')[1])
            time.append(i.split('\t')[0])
    return render_template("temperature.html", temperature_data=temperature_data, time=time)

if __name__ == "__main__":
    app.run(debug=True)


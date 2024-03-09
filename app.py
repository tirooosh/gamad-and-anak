from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)


# Your existing Python logic for connecting names
def connect_names_in_circle():
    with open("names.txt", "r", encoding="utf-8") as file:  # Assuming UTF-8 encoding
        names = file.read().splitlines()
    random.shuffle(names)
    connections = ["{} - {}".format(name, names[(i + 1) % len(names)]) for i, name in enumerate(names)]
    return connections


# Route to trigger the name connections and return as JSON
@app.route('/get-names')
def get_names():
    connections = connect_names_in_circle()
    return jsonify(connections)


# Serve an HTML page
@app.route('/')
def home():
    return render_template_string(open('index.html').read())


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from definition import projectPath, newLine
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/init', methods=['GET', 'POST'])
def init():

    if 'toto' in request.form:
        dataset_name = request.form['toto']

    else:
        dataset_name = "pima-indians-diabetes.csv"

    import data_reader
    dataset = data_reader.reader(dataset_name)

    return render_template('init.html', value2=dataset)


@app.route('/result', methods=['GET', 'POST'])
def result():

    global projectPath
    global newLine

    projectPath = request.form['Pass']

    if projectPath == "a":

        projectpath = request.form['projectFilepath']
        n_l = request.form['New_Line']

        newline = n_l
        projectPath = projectpath
        newLine = newline

        import keras_first_network
        animal = keras_first_network.ml_script(projectpath, newline)

        projectPath = ""

    elif projectPath != "a":

        import keras_first_network
        newLine = "123"
        animal = keras_first_network.ml_script(projectPath, newLine)

    return render_template('result.html', value=animal)

@app.route('/result/graph', methods=['POST'])
def graph():

    return render_template("graph.html")
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


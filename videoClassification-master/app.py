from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask import Flask, request, make_response
import RunPythonFile
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Route that will trigger the scrape function
@app.route("/", methods = ['POST'])
def predict():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    fileName = request.form.get('video')
    modelName = request.form.get('model1')

    print('filename = ', fileName)
    print('modelName = ', modelName)

    results = RunPythonFile.predict(modelName,fileName)
    #results = {'height':20}

    print(results)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

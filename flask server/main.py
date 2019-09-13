import os
import io
import base64
from flask import Flask, jsonify, request,render_template
from matplotlib import pyplot as plt
import base64
import pickle

app = Flask(__name__)



@app.route('/Housing',methods=['GET'])
def getHousingPredictions():
    #Load the saved model
    print("Loading the model...")
    loaded_model = None
    months_ahead = 79 + int(request.args['months'])
    clf = 'Housing.pk'
    with open(clf,'rb') as f:
        loaded_model = pickle.load(f)
    print("The model has been loaded...doing predictions now...")
    img = io.BytesIO()
    fig = plt.figure()
    fig = loaded_model.plot_predict(1,months_ahead)
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    graph_url = 'data:image/png;base64,{}'.format(graph_url)
    return render_template('index.html', graph = graph_url, name = "Housing")

@app.route('/Intoxicants',methods=['GET'])
def getIntoxicantsPredictions():
    #Load the saved model
    print("Loading the model...")
    loaded_model = None
    months_ahead = 79 + int(request.args['months'])
    clf = 'intoxicants.pk'
    with open(clf,'rb') as f:
        loaded_model = pickle.load(f)
    print("The model has been loaded...doing predictions now...")
    img = io.BytesIO()
    fig = plt.figure()
    fig = loaded_model.plot_predict(1,months_ahead)
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    graph_url = 'data:image/png;base64,{}'.format(graph_url)
    return render_template('index.html', graph = graph_url, name = "Intoxicants")

@app.route('/Food',methods=['GET'])
def getFoodPredictions():
    #Load the saved model
    print("Loading the model...")
    loaded_model = None
    months_ahead = 79 + request.args['months']
    clf = 'Food.pk'
    with open(clf,'rb') as f:
        loaded_model = pickle.load(f)
    print("The model has been loaded...doing predictions now...")
    img = io.BytesIO()
    fig = plt.figure()
    fig = loaded_model.plot_predict(1,months_ahead)
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    graph_url = 'data:image/png;base64,{}'.format(graph_url)
    return render_template('index.html', graph = graph_url, name = "Food and Beverages")

@app.route('/')
def home():
    return render_template('subindex.html')

if __name__ == '__main__':
    app.run(debug=True)
import os
import io
import base64
import pandas as pd
from flask import Flask, jsonify, request,render_template
import matplotlib.pylab as plt
import base64
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
def getPredictions():
    #Load the saved model
    print("Loading the model...")
    loaded_model = None
    clf = 'model_v1.pk'
    with open(clf,'rb') as f:
        loaded_model = pickle.load(f)
    print("The model has been loaded...doing predictions now...")
    img = io.BytesIO()
    fig = plt.figure()
    fig = loaded_model.plot_predict(1,95)
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    graph_url = 'data:image/png;base64,{}'.format(graph_url)
    return render_template('index.html', graph = graph_url)
if __name__ == '__main__':
    app.run()
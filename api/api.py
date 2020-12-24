








            json_ = request.json
            prediction = list(lr.predict(query))
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            return jsonify({'prediction': str(prediction)})
            return jsonify({'trace': traceback.format_exc()})
        except:
        port = 12345 # If you don't provide any port the port will be set to 12345
        port = int(sys.argv[1]) # This is for a command-line input
        print ('Train the model first')
        return ('No model here to use')   b,99
        try:
    app.run(port=port, debug=True)
    else:
    except:
    if lr:
    lr = joblib.load("model.pkl") # Load "model.pkl"
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    print ('Model loaded')
    try:
# Dependencies
# Your API definition
@app.route('/predict', methods=['POST'])
app = Flask(__name__)
def predict():
from flask import Flask, request, jsonify
if __name__ == '__main__':
import joblib
import numpy as np
import pandas as pd
import traceback
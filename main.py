import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
import joblib
import numpy as np

load_dotenv('.env') # load everything from .env file 

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

app = FastAPI()

model_filename = 'voting_classifier.joblib'
loaded_model = joblib.load(filename=model_filename)
print(f"ML model '{model_filename}' loaded successfully.")
iris_data = load_iris()
iris_target_names = iris_data.target_names

class Iris(BaseModel):
    petal_length: float
    petal_width: float
    sepal_length: float
    sepal_width: float

@app.post('/iris')
async def iris_predict(data: Iris):
    # feed this data into ml model
    # and send the response back to the client
    features = np.array([
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]
    ])
    prediction_index = loaded_model.predict(features)[0]
    predicted_species = iris_target_names[prediction_index]
    return {
        'message': 'Prediction successful',
        'predicted_species': predicted_species
    }

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', reload = True)
